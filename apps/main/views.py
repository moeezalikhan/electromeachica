from django.shortcuts import render
from django.db.models import Q
from apps.projects.models import Project
from apps.main.models import Brochure, Banner

# Create your views here.
def home(request):

    latest_projects = Project.objects.all().order_by('-created_at')[:6]
    banners = Banner.objects.filter(is_active=True).order_by('-priority')
    
    

    context = {
        "latest_projects": latest_projects,
        "banners": banners
    }
    return render(request, 'home/index.html', context)


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


