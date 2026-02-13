from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hi(request):
    return HttpResponse("hello this is app 2 homepage")

def hello(request):
    return HttpResponse("this is second page from app 2")