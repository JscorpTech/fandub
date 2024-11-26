from rest_framework import serializers

from ..models import FilmModel
from .category import CategorySerializer
from .shared import GenreSerializer


class FilmSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    genre = GenreSerializer(many=True)

    class Meta:
        model = FilmModel
        fields = [
            "id",
            "name",
            "image",
            "desc",
            "year",
            "genre",
            "director",
            "category",
            "file",
        ]
