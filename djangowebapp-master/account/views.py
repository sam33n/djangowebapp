from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Home:home')
    else:
        form = UserCreationForm()
    return render(request, 'account/signup.html',{ 'form':form })


def log_in(request):
    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('Home:home')
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', { 'form': form })

def log_out(request):
    if request.method=='POST':
        logout(request)
        return redirect('Home:home')

