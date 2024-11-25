from django.db import models
from core.http.models import AbstractBaseModel
from django.utils.translation import gettext_lazy as _


class CategoryModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("CategoryModel")
        verbose_name_plural = _("CategoryModel")
