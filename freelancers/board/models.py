from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Posting(models.Model):
    author = models.ForeignKey(User, null=True, blank=True, related_name='author')
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=1000, default = " ")
    chosen = models.ForeignKey(User, null=True, blank=True, related_name='chosen')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
      
class Response(models.Model):
    author = models.ForeignKey(User, null=True, blank=True)
    theposting = models.ForeignKey(Posting, null=True, blank=True)
    body = models.CharField(max_length=1000, default = " ")
        