""" ============= Imports =============== """
from django.shortcuts import render, get_object_or_404
from apps.products.models import Product
from django.core.paginator import Paginator
from django.db.models import Q


""" ============= All Products View =============== """
def products(request):
    category = request.GET.get('category')
    search_query = request.GET.get('q', '')

    products = Product.objects.prefetch_related('images').all()

    # Category filter
    if category:
        products = products.filter(category=category)

    # Search filter
    if search_query:
        products = products.filter(
            Q(title__icontains=search_query) |
            Q(short_description__icontains=search_query)
        )

    # Pagination (9 per page)
    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Product.CATEGORY_CHOICES

    context = {
        'page_obj': page_obj,
        'products': page_obj.object_list,
        'categories': categories,
        'category': category,
        'search_query': search_query,
    }
    return render(request, 'products/products.html', context)



""" ============= Single Product Detail View =============== """
def product_detail(request, pk):
    product = get_object_or_404(Product.objects.prefetch_related('images'), pk=pk)
    images = product.images.all()  # type: ignore

    # --- Sidebar Filters ---
    search_query = request.GET.get('q', '').strip()
    category = request.GET.get('category', '').strip()

    # --- Related products queryset ---
    related_products = Product.objects.prefetch_related('images').exclude(pk=product.pk)

    # Filter by category
    if category:
        related_products = related_products.filter(category=category)
    else:
        related_products = related_products.filter(category=product.category)

    # Filter by search query
    if search_query:
        related_products = related_products.filter(
            Q(title__icontains=search_query) |
            Q(short_description__icontains=search_query)
        )

    # Limit results
    related_products = related_products.distinct()[:6]

    categories = Product.CATEGORY_CHOICES

    context = {
        'product': product,
        'images': images,
        'related_products': related_products,
        'categories': categories,
        'search_query': search_query,
        'category': category,
    }
    return render(request, 'products/product_detail.html', context)
