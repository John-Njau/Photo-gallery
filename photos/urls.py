from django.urls import re_path, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name='home'),
    re_path(r'^photos/$', views.allphotos, name='allphotos'),
    re_path(r'^search/', views.search_results, name='search_results'),
    path('categoryview/<int:categoryId>', views.categoryview, name='categoryview'),
    path('locationview/<int:locationId>', views.locationview, name='locationview'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)