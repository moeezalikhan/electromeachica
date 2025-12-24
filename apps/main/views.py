from django.shortcuts import render
from django.db.models import Q
from apps.projects.models import Project
from apps.main.models import Brochure, Banner, OurClient

## views.py
def home(request):
    banners = Banner.objects.filter(is_active=True).order_by('priority')
    latest_projects = Project.objects.all().order_by('-created_at')[:6]

    # URL mapping view ke andar
    category_urls = {
        'textile': 'textile_sector',
        'chemicals': 'chemicals',
        'FMCG': 'fmcg',
        'Cement': 'cement',
        'TEST_BENCH': 'testing_benches',
        'EDUCATIONAL_TRAINERS': 'educational_trainers',
        'INDUSTRIAL_TRAINERS': 'industrial_trainers',
        'OTHERS': 'market_sector',
        
    }

    our_clients = OurClient.objects.filter(is_active=True).order_by('priority')


    for banner in banners:
        banner.url = category_urls.get(banner.category, 'market_sector') # pyright: ignore[reportAttributeAccessIssue]

    context = {
        "latest_projects": latest_projects,
        "banners": banners,
        "clients": our_clients
    }
    return render(request, 'home/index.html', context=context)


def brochure(request):
    search_query = request.GET.get('q', '').strip()
    if search_query:
        brochures = Brochure.objects.filter(
            (Q(title__icontains=search_query) | Q(description__icontains=search_query)) & Q(is_active=True)
        )
    else:
        brochures = Brochure.objects.filter(is_active=True)
    context = {
        "brochures": brochures,
        "search_query": search_query
    }
    return render(request, 'home/brochure.html', context=context)