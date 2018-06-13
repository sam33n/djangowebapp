from django import forms
from . import models

class Contactform(forms.ModelForm):
    class Meta:
        model = models.ContactDetail
        fields = ['name', 'email', 'message']
