from django.shortcuts import render, redirect
from .models import Photo
from django.core.files.storage import default_storage

# Create your views here.

def index(request):
    photos = Photo.objects.all()
    context = {'photos':photos}
    return render(request, 'index.html', context)

def addProduct(request):
    if request.method == "POST":
        photo = Photo()
        if len(request.FILES) != 0:
            photo.image = request.FILES['image']
            
        photo.save()
        return redirect('/')    
    return render(request, 'add.html')

def detailProduct(request, pk):
    phot = Photo.objects.get(id=pk)
    context = {'phot':phot}
    return render (request, 'detail.html', context)

def deleteProduct(request, pk):
    phot = Photo.objects.get(id=pk)
    default_storage.delete(phot.image.path)
    phot.delete()
    return redirect('/')