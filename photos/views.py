from django.shortcuts import render
from .models import Category, Image, Location

# Create your views here.
def home(request):
    details = Category.objects.all()
    locations = Location.objects.all()
    return render(request, 'display/home.html', {'details': details, 'locations': locations})

def navbar(request):
    details = Category.objects.all()
    locations = Location.objects.all()
    return render(request, 'display/navbar.html', {'details': details, 'locations': locations})

def allphotos(request):
    photos = Image.objects.all()
    print(photos)
    return render(request, 'display/photos.html',{'photos':photos})

def categoryview(request, categoryId):
    ind_category = Category.objects.get(pk=categoryId)
    photos = Image.objects.filter(category=ind_category)
    print(photos)
    title = f'Photos in {ind_category} category'
    photocount = photos.count()
    msg = f'There are {photocount} photos in this category'
    return render(request, 'category/categoryview.html', {'photos': photos, 'title': title, 'msg': msg, 'category': ind_category})

def locationview(request, locationId):
    ind_location =Location.objects.get(id=locationId)
    photos = Image.objects.filter(location=ind_location)
    photocount =photos.count()
    msg = f'There are {photocount} photos shot in this location'
    return render(request, 'location/locationview.html', {'photos': photos, 'location': ind_location, 'msg': msg})  

def search_results(request):
    if 'term' in request.GET and request.GET["term"]:
        search_term = request.GET.get("term")
        searched_terms = Image.search_by_name(search_term)
        message = f"{search_term}"
        return render(request, 'search/search.html',{"message":message,"terms": searched_terms})
    else:
        message = "Searched term not found"
        return render(request, 'search/search.html', {"message":message})