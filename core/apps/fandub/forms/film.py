from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from ..models import FilmModel


class FilmForm(forms.ModelForm):

    class Meta:
        model = FilmModel
        fields = "__all__"
        widgets = {
            "desc": CKEditor5Widget(),
        }
