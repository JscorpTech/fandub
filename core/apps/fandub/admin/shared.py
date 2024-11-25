from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin
from django.contrib import admin
from ..models import BannerModel, GenreModel, DirectorModel, CommentModel


class BannerAdmin(ModelAdmin):
    list_display = ["__str__"]


class GenreAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ["__str__"]
    search_fields = ["name"]


class DirectorAdmin(ModelAdmin):
    list_display = ["__str__"]


class CommentAdmin(ModelAdmin):
    list_display = ["__str__"]


admin.site.register(BannerModel, BannerAdmin)
admin.site.register(GenreModel, GenreAdmin)
admin.site.register(DirectorModel, DirectorAdmin)
admin.site.register(CommentModel, CommentAdmin)
