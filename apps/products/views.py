from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.conf import settings
from apps.products.models import Product, Categories


# ============ All Products View ============
def products(request):
    category_id = request.GET.get('category')
    search_query = request.GET.get('q', '')

    products_qs = Product.objects.prefetch_related('images').all()

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

    @property
    def images(self):
        raise NotImplementedError

    @images.setter
    def images(self, value):
        raise NotImplementedError

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'products': page_obj.object_list,
        'category': int(category_id) if category_id else None,
        'search_query': search_query,
        'categories': Categories.objects.filter(is_active=True),  # added
    }
    return render(request, 'products/products.html', context)


# ============ Product Detail View ============
def product_detail(request, pk):
    product = get_object_or_404(Product.objects.prefetch_related('images'), pk=pk)
    images = product.images.all() # type: ignore

    # Sidebar filters
    search_query = request.GET.get('q', '').strip()
    category_id = request.GET.get('category', '').strip()

    # Related products query
    if category_id:
        related_products = Product.objects.filter(category_id=category_id).exclude(pk=product.pk).prefetch_related('images')
    else:
        related_products = Product.objects.filter(category=product.category).exclude(pk=product.pk).prefetch_related('images')

    # Optional search filter
    if search_query:
        related_products = related_products.filter(
            Q(title__icontains=search_query) |
            Q(short_description__icontains=search_query)
        )

    related_products = related_products.distinct()[:6]

    whatsapp_number = getattr(settings, 'WHATSAPP_NUMBER', '')
    whatsapp_message_template = getattr(settings, 'WHATSAPP_DEFAULT_MESSAGE', '')
    whatsapp_message = whatsapp_message_template.format(product=product.title)

    context = {
        'product': product,
        'images': images,
        'related_products': related_products,
        'search_query': search_query,
        'category': int(category_id) if category_id else None,
        'categories': Categories.objects.all(),  # added
        'whatsapp_number': whatsapp_number,
        'whatsapp_message': whatsapp_message,
    }

    return render(request, 'products/product_detail.html', context)
