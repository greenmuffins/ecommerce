from django import forms
from django.contrib.auth.forms import UserCreationForm
from board.forms import PostingForm, UploadForm, ItemForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.list import ListView
from board.models import Posting, Response, Upload, Item
from django.utils import timezone
from django.db.models import Sum, Q
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy

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
    
class YourStore(ListView):
    template_name = "your-item-list.html"
    model = Item

class ItemList(ListView):
    template_name = "item-list.html"
    model = Item

def PostingDetails(request, the_id):
    thePost = Posting.objects.get(id = the_id)
    theResponses = Response.objects.filter(theposting__id = the_id)
    return render(request, "post-detail.html", {
        'thePost': thePost,
        'theResponses': theResponses,
        'thePostId': the_id,
    })
  
def ItemDetails(request, the_id):
    the_item = Item.objects.get(id = the_id)
    return render(request, "item-detail.html", {
        'item': the_item,
    })

def CreatePosting(request):
    the_title = request.GET.get('the_title')
    the_body = request.GET.get('the_body')
    newPost = Posting(author = request.user, title = the_title, body = the_body)
    newPost.save()    
    the_id = newPost.id
    return render(request, "home.html")

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

def upload(request):
    if request.method=="POST":
        img = UploadForm(request.POST, request.FILES)
        if img.is_valid():
            img.save() 
            return HttpResponseRedirect(reverse('upload'))
    else:
        img=UploadForm()
    images=Upload.objects.all()
    return render(request,'upload.html',{'form':img,'images':images})

def item_upload(request):
    if request.method=="POST":
        the_item = ItemForm(request.POST, request.FILES)
        if the_item.is_valid():
            load_item = the_item.save(commit=False)
            load_item.author = request.user
            load_item.save()     
            return HttpResponseRedirect(reverse('item_upload'))
    else:
        the_item=ItemForm()
    Items=Item.objects.all()
    return render(request,'item_upload.html',{'form':the_item,'items':Items})

def item_upload2(request):
    if request.method=="POST":
        the_item = ItemForm(request.POST, request.FILES)
        if the_item.is_valid():
            load_item = the_item
            load_item.author = request.user
            the_item.name = request.user.username
            the_item.save()
            return HttpResponseRedirect(reverse('item_upload'))
    else:
        the_item=ItemForm()
    Items=Item.objects.all()
    return render(request,'item_upload.html',{'form':the_item,'items':Items})