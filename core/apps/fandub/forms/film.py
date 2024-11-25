from django import forms
from ..models import FilmModel
from django_ckeditor_5.widgets import CKEditor5Widget


class FilmForm(forms.ModelForm):

    class Meta:
        model = FilmModel
        fields = "__all__"
        widgets = {
            "desc": CKEditor5Widget(),
        }
