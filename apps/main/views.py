from django.shortcuts import render

from apps.projects.models import Project

# Create your views here.
def home(request):
    
    latest_projets = Project.objects.all().order_by('-created_at')[:6]
    print(latest_projets)
    context = {
                "latest_projects" : latest_projets
           }
    return render(request, 'home/index.html',context=context)


