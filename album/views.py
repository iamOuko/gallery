from django.shortcuts import render,redirect
from .models import Image

# Create your views here.
def index(request):
    images = Image.objects.all()
    return render(request, 'album/index.html', {"images":images})


def search_image(request):
    if 'location' in request.GET and request.GET["location"]:
        search_term = request.GET.get("location")
        images = Image.search_by_location(search_term)
        message = f"{search_term}"

        return render(request, 'album/search.html',{"message":message, "images":images})

    elif 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'album/search.html',{"message":message, "images":images})

    else:
        message = "Enter search item!"
        return render(request, 'album/search.html', {"message":message})