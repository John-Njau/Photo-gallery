from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'display/home.html')

def allphotos(request):
    return render(request, 'display/photos.html')