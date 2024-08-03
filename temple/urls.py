
from django.contrib import admin
from django.urls import path , include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('switch/',views.switch,name='switch'),
    path('',views.index,name='home'),
    path('trustees/',views.trustees,name='trustees'),
    path('livedarshan/',views.darshan,name='darshan'),
    path('templedailyseva/',views.dailyseva,name='dailyseva'),
    path('mahaabhishekh/',views.mahaabhishekh,name='mahaabhishekh'),
    path('imagegallery/',views.imagegallery,name='imagegallery'),
    path('videogallery/',views.videogallery,name='videogallery'),
    path('othergallery/',views.othergallery,name='othergallery'),
    path('poojadetails/',views.poojadetails,name='poojadetails'),
    path('donation/',views.donation,name='donation'),
    path('contact/',views.contact,name='contact'),
    path('Festivals/',views.Festivals,name='Festivals'),
    path('about/',views.about,name='about'),
    path('architecture/',views.architecture,name='architecture'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)