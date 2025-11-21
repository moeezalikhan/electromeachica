""" ============= Imports =============== """
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from apps.projects.models import Project


""" ============= All Projects View =============== """
def projects(request):
    projects = Project.objects.prefetch_related('images').all()
    categories = Project.CATEGORY_CHOICES

    # Pagination (9 projects per page)
    paginator = Paginator(projects, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    

    context = {
        'projects': page_obj.object_list,
        'categories': categories,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
    }

    return render(request, 'projects/projects.html', context)


""" ============= Single Project Detail View =============== """
def project_detail(request, pk):
    project = get_object_or_404(Project.objects.prefetch_related('images'), pk=pk)

   
    main_image = project.main_image # type: ignore

    #  Gallery images
    gallery_images = project.images.all() # type: ignore

    #  Previous and Next projects
    prev_project = Project.objects.filter(id__lt=project.id).order_by('-id').first() # type: ignore
    next_project = Project.objects.filter(id__gt=project.id).order_by('id').first() # type: ignore

    context = {
        'project': project,
        'main_image': main_image,
        'gallery_images': gallery_images,
        'prev_project': prev_project,
        'next_project': next_project,
    }

    return render(request, 'projects/project_detail.html', context)
