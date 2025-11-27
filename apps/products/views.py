from django.shortcuts import render,redirect, get_object_or_404
from apps.products.models import Product, Categories
from django.core.paginator import Paginator
from django.db.models import Q
from django.conf import settings
from apps.products.models import Product, Categories


""" ============ All Products View ============ """
def products(request):
    category_id = request.GET.get('category')
    search_query = request.GET.get('q', '')

    products_qs = Product.objects.prefetch_related('images').filter(category__is_active=True)


    # Category filter
    if category_id:
        products_qs = products_qs.filter(category_id=category_id)

    # Search filter
    if search_query:
        products_qs = products_qs.filter(
            Q(title__icontains=search_query) |
            Q(short_description__icontains=search_query)
        )

    # Pagination (9 per page)
    paginator = Paginator(products_qs, 9)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'category': int(category_id) if category_id else None,
        'search_query': search_query,
        'categories': Categories.objects.filter(is_active=True),  # added
    }
    return render(request, 'products/products.html', context)


""" ============ Product Detail View ============ """
def product_detail(request, pk):
    product = get_object_or_404(Product.objects.prefetch_related('images'), pk=pk)
    images = product.images.all()  # type: ignore

    search_query = request.GET.get('q', '').strip()

    # Related products: only current category, excluding current product
    related_products = Product.objects.filter(
        category=product.category,
        availability=True
    ).exclude(pk=product.pk).prefetch_related('images')

    
    related_products = related_products.distinct()[:6]

    whatsapp_number = getattr(settings, 'WHATSAPP_NUMBER', '')
    whatsapp_message_template = getattr(settings, 'WHATSAPP_DEFAULT_MESSAGE', '')
    whatsapp_message = whatsapp_message_template.format(product=product.title)
    # Sidebar: all active categories
    categories = Categories.objects.filter(is_active=True)

    context = {
        'product': product,
        'images': images,
        'related_products': related_products,
        'search_query': search_query,
        'whatsapp_number': whatsapp_number,
        'whatsapp_message': whatsapp_message,
        'category': product.category,  # currently selected category # type: ignore
        'categories': categories,
    }

    return render(request, 'products/product_detail.html', context)


