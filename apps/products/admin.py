""" =========== Imports ============== """

from django.contrib import admin
from django.utils.html import format_html
from .models import Categories, Product, ProductImage


# ========= Categories Admin =========
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)


# ========= ProductImage Inline =========
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:100px; height:auto; border-radius:6px;" />',
                obj.image.url
            )
        return "-"

    image_preview.short_description = "Image Preview" # pyright: ignore[reportFunctionMemberAccess]


# ========= Product Admin =========
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_image',
        'title',
        'category',
        'availability',
        'price',
        'created_at',
        'updated_at',
    )

    list_filter = ('availability', 'category')
    search_fields = ('title', 'description', 'model_number', 'part_number')
    autocomplete_fields = ('category',)
    inlines = [ProductImageInline]

    def product_image(self, obj):
        first_image = obj.images.first()
        if first_image and first_image.image:
            return format_html(
                '<img src="{}" style="width:60px; height:auto; border-radius:4px;" />',
                first_image.image.url
            )
        return "-"

    product_image.short_description = "Image" # pyright: ignore[reportFunctionMemberAccess]
