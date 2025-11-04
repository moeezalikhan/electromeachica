""" ============ Imports ============ """
from django.contrib import admin
from apps.projects.models import Project, ProjectImage


""" ========== Project Image Inline Class =========== """
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


""" =========== Project Admin =============== """
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]
    list_display = ('name', 'category')
