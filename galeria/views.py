from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Feliz 7 meses bb</h1>')