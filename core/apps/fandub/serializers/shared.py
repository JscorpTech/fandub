from rest_framework import serializers
from ..models import BannerModel, GenreModel


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerModel
        fields = [
            "id",
            "title",
            "desc",
            "is_movie",
            "image",
            "status",
            "trailer",
        ]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenreModel
        fields = [
            "id",
            "name",
        ]
