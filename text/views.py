from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'hello':'you can enter some words'})
    #return HttpResponse('Hello')

def count(request):
    return render(request, 'count.html')
