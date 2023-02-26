from django.shortcuts import render, redirect
from .models import Treads

def show_threads(request):
    all_threads = Treads.objects.all()
    return render(request, "main_page.html", {"posts": all_threads})

def create_thread(request):
    data = {}
    if request.method == "POST":
        title = request.POST.get("title", "")
        content = request.POST.get("content", "")
        if title and content:
            tread = Treads(title=title, content=content)
            tread.save()
            return redirect("main")

        data["title"] = title
        data["content"] = content

    return render(request, "creation_page.html", data)

def tread_view(request, tread_id: int):
    tread = Treads.objects.get(id=tread_id)
    return render(request, "thread.html", {"post": tread})

