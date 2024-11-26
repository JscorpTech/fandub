from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin

from ..forms import FilmForm
from ..models import FilmModel


class FilmAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ["__str__"]
    form = FilmForm
    autocomplete_fields = ["genre", "category"]


admin.site.register(FilmModel, FilmAdmin)
