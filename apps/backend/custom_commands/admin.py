from django.contrib import admin

from  custom_commands.models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =(
        "name",
        "slug",
    )
