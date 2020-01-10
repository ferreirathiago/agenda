from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome):
    return HttpResponse('<h1>Hello World {}!</h1>'.format(nome))