from django.shortcuts import render

# Create your views here.

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

