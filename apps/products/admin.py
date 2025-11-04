""" ============ Imports ============ """
from django.contrib import admin
from apps.products.models import Product, ProductImage


""" ========== Product Image Inline Class =========== """
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


""" =========== Product Admin =============== """
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ('title', 'category', 'availability')
