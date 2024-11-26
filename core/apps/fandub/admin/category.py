from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin

from ..models import CategoryModel


class CategoryAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = [
        "__str__",
    ]
    search_fields = ["name"]


admin.site.register(CategoryModel, CategoryAdmin)
