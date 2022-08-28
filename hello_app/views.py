from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    text = "<h1>My Name is Vignesh Palanivel</h1>"
    return HttpResponse(text)
# Create your views here.
