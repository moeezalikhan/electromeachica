from django.contrib import admin
from django.utils.html import format_html
from apps.projects.models import Project, ProjectImage, ProjectCategory

""" ========== Project Image Inline Class =========== """
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    readonly_fields = ('image_tag',)

    # Show a thumbnail in inline form
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100 height=50" />', obj.image.url)
        return "-"
    image_tag.short_description = "Image Preview" # pyright: ignore[reportFunctionMemberAccess]


""" =========== Project Admin =============== """
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]
    list_display = ('name', 'category', 'image_count', 'first_image')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')

    # Show number of images
    def image_count(self, obj):
        return obj.images.count()
    image_count.short_description = "Images" # type: ignore

    # Show first image as a thumbnail in list view
    def first_image(self, obj):
        first = obj.images.first()
        if first and first.image:
            return format_html('<img src="{}" width="100 height=50" />', first.image.url)
        return "-"
    first_image.short_description = "Thumbnail" # type: ignore


# ========== Project Category Admin ==========
@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
