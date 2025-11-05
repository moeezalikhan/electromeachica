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

def product_singal(request):
    return render(request, 'products/product-single.html')

def our_mission(request):
    return render(request, 'about_us/our_mission.html')

def our_team(request):
    return render(request, 'about_us/our_team.html')

def market_sector(request):
    return render(request, 'marketSectors/market-sectors.html')


def construction_products(request):
    return render(request, 'marketSectors/Construction-products.html')

def aero_space_service(request):
    return render(request, 'marketSectors/aero-space-services.html')

def railway_infrastructure(request):
    return render(request, 'marketSectors/railway-infrastructure.html')

def ship_building_industry(request):
    return render(request, 'marketSectors/ship-building-industry.html')

def power_energy(request):
    return render(request, 'marketSectors/power-and-energy.html')

def automative_system(request):
    return render(request, 'marketSectors/automative-system.html')

def faqs(request):
    return render(request, 'faqs/faqs.html')
