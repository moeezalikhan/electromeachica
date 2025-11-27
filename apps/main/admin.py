from django.contrib import admin
from apps.main.models import Brochure

@admin.register(Brochure)
class BrochureAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'brochure', 'is_active', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('is_active', 'created_at', 'updated_at')

# Register your models here.
