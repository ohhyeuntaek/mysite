from django.shortcuts import render
from django.http import HttpResponse

def index(requset):
    return HttpResponse("hello, world. you're at the polls index.")
# Create your views here.
