from django.urls import path
from . import views

app_name = 'Contact'

urlpatterns = [
      path('', views.contact, name='contact'),
      path('response/', views.response_page, name='response'),
 ]
