from django.db import models
from django.utils.translation import gettext_lazy as _

from core.http.models import AbstractBaseModel, User


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


class CommentModel(AbstractBaseModel):
    text = models.CharField(_("text"), max_length=255)
    film = models.ForeignKey("FilmModel", on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = _("CommentModel")
        verbose_name_plural = _("CommentModel")
