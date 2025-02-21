
from django.contrib import admin
from django.urls import path
from Shopapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('gallery/', views.image, name='gallery'),
    path('Register/', views.form, name='form'),
    path('products/', views.product, name='product'),
]
