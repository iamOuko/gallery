from django.shortcuts import render,redirect
from .models import Image

# Create your views here.
def index(request):
    images = Image.objects.all()
    return render(request, 'album/index.html', {"images":images})


def search_image(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'album/search.html',{"message":message, "images":images})

    else:
        message = "Enter search item!"
        return render(request, 'album/search.html', {"message":message})