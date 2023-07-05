from django.shortcuts import render

# Create your views here.
from django.shortcuts import render



from .models import Photo

from django.shortcuts import get_object_or_404, redirect, render
from .models import Photo
import os

def delete_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == 'POST':
        # Delete photo from storage
        if os.path.isfile(photo.image.path):
            os.remove(photo.image.path)
        # Delete photo from database
        photo.delete()
        return redirect('home')
    context = {'photo': photo}
    return render(request, 'delete_photo.html', context)



def home(request):
    photos = Photo.objects.all()
    return render(request, 'home.html', {'photos': photos})



def about(request):
    return render(request, 'about.html')

def rules(request):
    return render(request, 'rules.html')

from django.shortcuts import render, redirect

from .forms import PhotoForm

def upload(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PhotoForm()
    return render(request, 'upload.html', {'form': form})

