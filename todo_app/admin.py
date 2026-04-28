from django.contrib import admin

from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ("title", "scheduled_at", "location", "updated_at")
    search_fields = ("title", "location")
    list_filter = ("scheduled_at", "updated_at")
