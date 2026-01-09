from django.shortcuts import render
from django.db.models import Q
from apps.projects.models import Project
from apps.main.models import Brochure, Banner, OurClient
from django.core.paginator import Paginator


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
        brochures_qs = Brochure.objects.filter(
            (Q(title__icontains=search_query) | Q(description__icontains=search_query)) & Q(is_active=True)
        )
    else:
        brochures_qs = Brochure.objects.filter(is_active=True)

    paginator = Paginator(brochures_qs, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)    

    page_range_display = paginator.get_elided_page_range( # pyright: ignore[reportAttributeAccessIssue]
        number=page_obj.number,
        on_each_side=1, 
        on_ends=2
    )
    context = {
        
        "brochures": page_obj,
        "page_obj": page_obj,  
        "search_query": search_query,
        "page_range_display": page_range_display,
    }
    return render(request, 'home/brochure.html', context=context)