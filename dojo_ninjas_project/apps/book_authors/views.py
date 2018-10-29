from django.shortcuts import render, redirect
from . import models

def index(request):
    return render(request, 'book_authors/index.html')
