from django import forms
from . import models

# added a class here
class BlogCreate(forms.ModelForm):
    class Meta:
        model = models.Blog_mod
        fields = ['comment','name','email']


class Beta:
    pass

