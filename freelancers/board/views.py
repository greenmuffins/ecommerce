from django import forms
from django.contrib.auth.forms import UserCreationForm
from forms import PostingForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.list import ListView
from models import Posting, Response
from django.utils import timezone
from django.db.models import Sum, Q

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
    else:
        form = UserCreationForm()
    return render(request, "register.html", {
        'form': form,
    })
  
def PostingCreate(request):
    if request.method == 'POST':
        form = PostingForm(request.POST)
        if form.is_valid():
            Posting = form.save()
            Posting.author = request.user
            Posting.save()
    else:
        form = PostingForm(request.POST)
        
    return render(request, "new-post.html", {
        'form': form,
    })
  
class PostingListView(ListView):
    template_name = "posting-list.html"
    model = Posting
    
def PostingDetails(request, the_id):
    thePost = Posting.objects.get(id = the_id)
    theResponses = Response.objects.filter(theposting__id = the_id)
    return render(request, "post-detail.html", {
        'thePost': thePost,
        'theResponses': theResponses,
        'thePostId': the_id,
    })
  
def CreateResponse(request):
    the_id = request.GET.get('the_id')
    the_text = request.GET.get('the_text')
    thePost = Posting.objects.get(id = the_id)
    newResponse = Response(author = request.user, theposting = thePost, body = the_text)
    newResponse.save()    
    theResponses = Response.objects.filter(theposting__id = the_id)
    return render(request, "post-detail.html", {
        'thePost': thePost,
        'theResponses': theResponses,
        'thePostId': the_id,        
    })    
  
def PersonalPosts(request):
    thePosts = Response.objects.filter(theposting__author = request.user)
    return render(request, "personal-posts.html", {
        'thePosts': thePosts,
    })   
  
def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
	Posts = Posting.objects.filter( Q(title__icontains = q))
        return render(request, 'search-results.html',
            {'Posts': Posts})  