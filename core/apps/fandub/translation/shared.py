from modeltranslation.translator import TranslationOptions, translator

from ..models import GenreModel


class GenreTranslation(TranslationOptions):
    fields = ("name",)


translator.register(GenreModel, GenreTranslation)
