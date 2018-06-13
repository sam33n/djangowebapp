from django.shortcuts import render
from .models import Homes

def home(request):
    data = Homes.objects.all().order_by('time')
    return render(request, 'home/home.html', { 'data': data })
