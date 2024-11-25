from django.db import models
from core.http.models import AbstractBaseModel
from django.utils.translation import gettext_lazy as _


class BannerModel(AbstractBaseModel):
    title = models.CharField(_("title"), max_length=255)
    desc = models.TextField(_("desc"))
    is_movie = models.BooleanField(_("is movie"), default=True)
    image = models.ImageField(_("image"), upload_to="banners/")
    status = models.BooleanField(_("status"), default=True)
    trailer = models.FileField(_("trailer"), upload_to="trailers/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("BannerModel")
        verbose_name_plural = _("BannerModel")


class GenreModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("GenreModel")
        verbose_name_plural = _("GenreModel")


class DirectorModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("DirectorModel")
        verbose_name_plural = _("DirectorModel")
