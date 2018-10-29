from django.shortcuts import render, redirect
from . import models

def index(request):
    return render(request, 'dojo_ninjas_app/index.html')
