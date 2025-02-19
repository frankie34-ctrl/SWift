
from django.contrib import admin
from django.urls import path
from Shopapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/', views.index),
    path('about/', views.about),
    path('gallery/', views.image),
]
