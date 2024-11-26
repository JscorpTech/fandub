from modeltranslation.translator import TranslationOptions, translator

from ..models import FilmModel


class FilmTranslation(TranslationOptions):
    fields = (
        "name",
        "desc",
    )


translator.register(FilmModel, FilmTranslation)
