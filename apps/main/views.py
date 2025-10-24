from django.shortcuts import render

# Create your views here.
def home(request):
     return render(request, 'home/index.html' )

def our_vision(request):
     return render(request, 'about_us/our_vision.html' )

def contact_us(request):
    return render(request, 'contact_us/contact_us.html')

def projects(request):
    return render(request, 'projects/projects.html')

def products(request):
    return render(request, 'products/products.html')
def our_mission(request):
    return render(request, 'about_us/our_mission.html')


def our_team(request):
    return render(request, 'about_us/our_team.html')
