from django import forms
from django.contrib.auth.models import User
from django.db import models
from board.models import Posting, Response, Upload, Item

class PostingForm(forms.ModelForm):
    class Meta:
		model = Posting
		fields = ('title','body')
	
class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('pic','name','description','price')
