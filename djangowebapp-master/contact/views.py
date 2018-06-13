from django.shortcuts import render, redirect
from . import forms

def contact(request):
    if request.method == 'POST':
        form = forms.Contactform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Contact:response')
    else:
        form = forms.Contactform()
    return render(request, 'contact/contact.html', { 'form': form })


def response_page(request):
    return render(request,'contact/response.html', {})
