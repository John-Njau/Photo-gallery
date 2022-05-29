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
    print(photos)
    return render(request, 'display/photos.html',{'photos':photos})

# def image_modal(request, categoryId):
#     images = Image.objects.get(id=categoryId)
#     return render(request, 'display/home.html', {'images': images})

def locationview(request, locationId):
    location =Location.objects.get(id=locationId)
    images = Image.objects.get(id=locationId)
    return render(request, 'display/locationview.html', {'images': images, 'location': location})    

def beaches(request):
    cat_beaches = Category.objects.get(pk=3)
    beaches = Image.objects.filter(category=cat_beaches)
    return render(request,'category/beaches.html', {'beaches':beaches})

def nature(request):
    cat_nature = Category.objects.get(pk=1)
    nature = Image.objects.filter(category=cat_nature)
    return render(request,'category/nature.html', {'nature':nature})
   

def animals(request):
    cat_animals = Category.objects.get(pk=4)
    animals = Image.objects.filter(category=cat_animals)
    return render(request,'category/animals.html', {'animals':animals})


def food(request):
    cat_food = Category.objects.get(pk=4)
    food = Image.objects.filter(category=cat_food)
    return render(request,'category/food.html', {'food':food})

def technology(request):
    pass

def paintings(request):
    pass
    
# def categoryview(request):
#     ind_category = Category.objects.get(pk=3)
#     images = Image.objects.filter(category=ind_category)
#     print(images)
#     title = f'{ind_category} category View'
#     msg = f'You are accessing category {ind_category}'
#     return render(request, 'display/categoryview.html', {'images': images, 'title': title, 'msg': msg})
