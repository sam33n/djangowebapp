from django import forms
from . import models


class BlogCreate(forms.ModelForm):
    class Meta:
        model = models.Blog_mod
        fields = ['comment','name','email']
