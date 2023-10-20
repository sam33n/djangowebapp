from django.shortcuts import render
from .models import About_mod

def about(request):
    datas = About_mod.objects.all()
    return render(request, 'about/about.html',{ 'datas' : datas })


# this is all about the database
