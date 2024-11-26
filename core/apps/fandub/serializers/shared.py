from rest_framework import serializers

from ..models import BannerModel, CommentModel, GenreModel


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


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = [
            "id",
            "text",
        ]
