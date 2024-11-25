from unfold.admin import ModelAdmin
from ..models import FilmModel
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from ..forms import FilmForm


class FilmAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ["__str__"]
    form = FilmForm
    autocomplete_fields = ["genre", "category"]


admin.site.register(FilmModel, FilmAdmin)
