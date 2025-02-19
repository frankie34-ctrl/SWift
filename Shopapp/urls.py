
from django.contrib import admin
from django.urls import path
from Shopapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('gallery/', views.image, name='gallery'),
]
