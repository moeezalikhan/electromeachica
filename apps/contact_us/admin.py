from django.contrib import admin
from .models import ContactUs

# Register your models here.
@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "message", "created_at"]
    search_fields = ["name", "email", "message"]
    list_filter = ["created_at"]
    list_per_page = 25
