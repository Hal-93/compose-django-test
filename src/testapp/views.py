from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def root (request):
    return HttpResponse('Hello Django and Docker')

def hello_world(request):
    return render(request, 'testapp/hello.html')