from django.urls import path
from . import views

app_name='Blog'

urlpatterns= [
   path('', views.blog_create, name='blogcreate'),
   path('blogsection/', views.blog_section, name='blogsection'),
]
