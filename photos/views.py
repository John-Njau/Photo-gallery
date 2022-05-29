from django.shortcuts import render
from .models import Category, Image, Location
# Create your views here.
def home(request):
    details = Category.objects.all()
    return render(request, 'display/home.html', {'details': details})

def navbar(request):
    details = Category.objects.all()
    locations = Location.objects.all()
    return render(request, 'display/navbar.html', {'details': details, 'locations': locations})


def allphotos(request):
    photos = Image.objects.all()
    category = Category.objects.all()
    return render(request, 'display/photos.html',{'photos':photos, 'category':category})

def image_modal(request, categoryId):
    images = Image.objects.get(id=categoryId)
    return render(request, 'display/home.html', {'images': images})
    
    
def categoryview(request, categoryId):
    category = Category.objects.get(id=categoryId)
    images = Image.objects.get(id=categoryId)
    title = f'{categoryId} category View'
    msg = f'You are accessing category {categoryId}'
    return render(request, 'display/categoryview.html', {'images': images, 'title': title, 'msg': msg, 'category': category})

def locationview(request, locationId):
    location =Location.objects.get(id=locationId)
    images = Image.objects.get(id=locationId)
    return render(request, 'display/locationview.html', {'images': images, 'location': location})    