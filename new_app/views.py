from django.shortcuts import render
from .models import Treads

def show_threads(request):
    all_threads = Treads.objects.all()
    return render(request, "main_page.html", {"posts": all_threads})