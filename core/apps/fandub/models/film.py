from django.db import models
from django.utils.translation import gettext_lazy as _

from core.http.models import AbstractBaseModel


class FilmModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)
    image = models.ImageField(_("image"), upload_to="films-images/")
    desc = models.TextField(_("desc"))
    year = models.BigIntegerField(_("year"))
    genre = models.ManyToManyField("GenreModel")
    director = models.ForeignKey("DirectorModel", on_delete=models.CASCADE)
    category = models.ManyToManyField("CategoryModel")
    file = models.FileField(_("film"), upload_to="films/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("FilmModel")
        verbose_name_plural = _("FilmModel")
