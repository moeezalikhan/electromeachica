
""" ============ Imports ============ """
from django.contrib import admin
from django.utils.html import format_html
from apps.teams.models import Team

""" =========== Team Admin =============== """


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'full_name', 'designation', 'active', 'priority')
    list_editable = ('active', 'priority')
    list_filter = ('designation', 'active')
    search_fields = ('full_name',)
    ordering = ('priority',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="60" style="border-radius:50%; object-fit:cover;" />', obj.image.url)
        return "No Image"

    image_preview.short_description = "Image" # pyright: ignore[reportFunctionMemberAccess]
