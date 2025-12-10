""" ============= Imports =============== """
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.core.paginator import Paginator
from apps.projects.models import Project


""" ============= All Projects View =============== """
def projects(request):
    categories = Project.CATEGORY_CHOICES

    # Get search values (CORRECT strip usage)
    search_query = request.GET.get('q', '').strip()
    category_filter = request.GET.get('category', '').strip()


    # Base queryset (with prefetch)
    qs = Project.objects.prefetch_related('images').filter(is_active=True)

    # Apply search filter
    if search_query:
        qs = qs.filter(name__icontains=search_query)

    # Apply category filter
    if category_filter:
        qs = qs.filter(category=category_filter)

    # Pagination
    paginator = Paginator(qs, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Page range display logic
    total_pages = paginator.num_pages
    current = page_obj.number
    page_range_display = []

    for num in range(1, total_pages + 1):
        if num <= 2 or num > total_pages - 1 or (current - 1 <= num <= current + 1):
            page_range_display.append(num)
        elif num == 4 and current > 5:
            page_range_display.append("...")
        elif num == total_pages - 3 and current < total_pages - 4:
            page_range_display.append("...")

    context = {
        'projects': page_obj.object_list,
        'categories': categories,
        'page_range_display': page_range_display,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'search_query': search_query,
        'category_filter': category_filter,
    }

    return render(request, 'projects/projects.html', context)

