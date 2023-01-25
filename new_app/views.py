from django.shortcuts import render
from .models import Treads

def show_threads(request):
    all_threads = Treads.objects.all()
