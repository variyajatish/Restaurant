from django.contrib import admin
from django.urls import path
from .views import Home, AddUser, About, ViewUser , ChefData, ChefPart, Chefsinfo, GalleryImg
from django.conf import settings  
from django.conf.urls.static import static   

urlpatterns = [ 
    path('', Home),
    path('add', AddUser),
    path('about', About),
    path('view', ViewUser),
    path('data',ChefData),
    path('part',ChefPart),
    path('info',Chefsinfo),
    path('gallery',GalleryImg),
]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  

