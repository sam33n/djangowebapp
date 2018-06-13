from django.shortcuts import render, redirect
from . import forms
from .models import Blog_mod
from django.contrib.auth.decorators import login_required

@login_required(login_url='/account/login/')
def blog_create(request):
    if request.method == 'POST':
        form = forms.BlogCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Blog:blogsection')
    else:
        form = forms.BlogCreate()
    return render(request, 'blog/blog.html',{ 'form': form })


def blog_section(request):
    stories = Blog_mod.objects.all().order_by('time')
    return render(request, 'blog/blogstories.html', { 'stories':stories })
