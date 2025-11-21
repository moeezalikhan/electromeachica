from django.contrib import admin
from .models import Categories, Product, ProductImage
from django.utils.html import format_html

# ========= Categories Admin =========
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)


# ========= ProductImage Inline =========
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    readonly_fields = ('image_tag', 'list_image_tag')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Image' # type: ignore

    def list_image_tag(self, obj):
        if obj.list_image:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.list_image.url)
        return "-"
    list_image_tag.short_description = 'List Image' # type: ignore


# ========= Product Admin =========
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'availability', 'created_at', 'updated_at')
    list_filter = ('availability', 'category')
    search_fields = ('title', 'short_description')
    autocomplete_fields = ['category']  # green "+" button
    inlines = [ProductImageInline]      # show images inline in Product admin


# ========= ProductImage Admin =========
@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image_tag', 'list_image_tag', 'created_at')
    readonly_fields = ('image_tag', 'list_image_tag')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Image' # type: ignore

    def list_image_tag(self, obj):
        if obj.list_image:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.list_image.url)
        return "-"
    list_image_tag.short_description = 'List Image' # type: ignore
