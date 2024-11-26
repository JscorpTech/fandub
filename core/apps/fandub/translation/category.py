from modeltranslation.translator import TranslationOptions, translator

from ..models import CategoryModel


class CategoryTranslation(TranslationOptions):
    fields = ("name",)


translator.register(CategoryModel, CategoryTranslation)
