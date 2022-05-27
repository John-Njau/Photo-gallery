import re
from django.urls import re_path, path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    re_path(r'^photos/$', views.allphotos, name='photos'),
]