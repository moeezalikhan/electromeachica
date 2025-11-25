from django.contrib import admin
from .models import Categories, Product, ProductImage
from django.utils.html import format_html

# ========= Categories Admin =========
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description','is_active', 'created_at', 'updated_at')
    search_fields = ('name',)
    


# ========= ProductImage Inline =========
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Image' # type: ignore

# ========= Product Admin =========
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'availability', 'created_at', 'updated_at')
    list_filter = ('availability', 'category')
    search_fields = ('title', 'short_description')
    autocomplete_fields = ['category']  # green "+" button
    readonly_fields = ['sku']
    inlines = [ProductImageInline]      # show images inline in Product admin


# ========= ProductImage Admin =========
@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image_tag', 'created_at')
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Image' # type: ignore