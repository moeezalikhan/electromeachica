""" ============= Imports =============== """
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from apps.projects.models import Project


""" ============= All Projects View =============== """
def projects(request):
    categories = Project.CATEGORY_CHOICES

    # Get search values
    search_query = request.GET.get('q', '').strip()
    category_filter = request.GET.get('category', '').strip()

    # Base queryset
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

    """ ============= Clean Pagination Dots =============== """
    total_pages = paginator.num_pages
    current = page_obj.number
    page_range_display = []

    # Helper to add page numbers without duplicates
    def add_page(num):
        if 1 <= num <= total_pages and num not in page_range_display:
            page_range_display.append(num)

    # Always show first 2 pages
    add_page(1)
    add_page(2)

    # Pages around current
    for num in range(current - 1, current + 2):
        add_page(num)

    # Always show last 2 pages
    add_page(total_pages - 1)
    add_page(total_pages)

    # Sort pages
    page_range_display = sorted(page_range_display)

    # Insert "..." where gaps exist
    final_range = []
    previous = None

    for num in page_range_display:
        if previous and num - previous > 1:
            final_range.append("...")
        final_range.append(num)
        previous = num

    page_range_display = final_range

    """ ============= Context =============== """
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
