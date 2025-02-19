from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'Home.html')

def about(request):
    return render(request,'about.html')

def image(request):
    return render(request,'gallery.html')