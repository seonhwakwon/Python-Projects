from django.shortcuts import render,redirect
from django.http import HttpResponse

from .forms import ContactForm
from .models import contact
# Create your views here.
def home(request):
    form = ContactForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    content = {'form': form}

    return render(request, 'portfolio/index.html', content)

def about(request):
    form = ContactForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    content = {'form': form}
    return render(request, 'portfolio/about.html',content)

def github(request):
    form = ContactForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponse("Submitted successfully")
    content = {'form': form}
    return render(request, 'portfolio/github.html',content)
