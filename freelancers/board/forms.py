from django import forms
from django.contrib.auth.models import User
from django.db import models
from models import Posting

class PostingForm(forms.ModelForm):
    class Meta:
	model = Posting
	fields = ('title','body')
	