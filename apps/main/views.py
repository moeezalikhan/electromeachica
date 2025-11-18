from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home/index.html')


def our_vision(request):
    return render(request, 'about_us/our_vision.html')


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


def textile_sector(request):
    return render(request, 'marketSectors/textile_sector.html')


def educational_trainers(request):
    return render(request, 'marketSectors/educational_trainers.html')


def industrial_trainers(request):
    return render(request, 'marketSectors/industrial_trainers.html')


def testing_benches(request):
    return render(request, 'marketSectors/testing_benches.html')


def cement(request):
    return render(request, 'marketSectors/cement.html')


def fmcg(request):
    return render(request, 'marketSectors/fmcg.html')


def chemicals(request):
    return render(request, 'marketSectors/chemicals.html')


def faqs(request):
    return render(request, 'faqs/faqs.html')


def privacy_policy(request):
    return render(request, "faqs/privacy_policy.html")
