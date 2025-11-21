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

def product_detail(request, pk):
    product = get_object_or_404(Product.objects.prefetch_related('images'), pk=pk)
    images = product.images.all()  # type: ignore

    # Sidebar inputs
    search_query = request.GET.get('q', '').strip()
    category = request.GET.get('category', '').strip()  # category selection from sidebar

    # ---- Base Query ----
    if category:  
        products_to_show = Product.objects.filter(category=category).prefetch_related('images')
    else:  # default: related products of current product's category
        products_to_show = Product.objects.filter(category=product.category).exclude(pk=product.pk).prefetch_related('images')

    # ---- Optional Search Filtering ----
    if search_query:
        products_to_show = products_to_show.filter(
            Q(title__icontains=search_query) |
            Q(short_description__icontains=search_query)
        )

    
    products_to_show = products_to_show.distinct()[:6]

    categories = Product.CATEGORY_CHOICES

    context = {
        'product': product,
        'images': images,
        'related_products': products_to_show,
        'categories': categories,
        'search_query': search_query,
        'category': category,
    }

    return render(request, 'products/product_detail.html', context)
