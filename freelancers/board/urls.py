from django.conf.urls import url
from django.conf.urls import include, url
from django.views.generic import TemplateView, ListView
from django.core.urlresolvers import reverse_lazy, reverse
from board import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="home.html")), 
    url(r'^register/$', views.register, name='register'),        
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='user_login'),  
    url(r'^logout$', 'django.contrib.auth.views.logout_then_login', {'login_url': reverse_lazy('user_login')}, name='user_logout'),
    url(r'^posts/$', views.PostingListView.as_view(), name='posting-list'),
    url(r'^personal-posts/$', views.PersonalPosts, name='personal-posts'),
    url(r'^new-post/$', views.PostingCreate, name='new-post'),
    url(r'^post-detail/(?P<the_id>\d+)/$', views.PostingDetails, name='post-detail'),
    url(r'^make-response/$', views.CreateResponse, name='create-response'),
    url(r'^search/$', views.search, name='search'),    
] 