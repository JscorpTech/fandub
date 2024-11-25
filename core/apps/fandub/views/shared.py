from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny
from ..models import BannerModel, GenreModel
from ..serializers import BannerSerializer, GenreSerializer


class BannerView(ReadOnlyModelViewSet):
    queryset = BannerModel.objects.all()
    serializer_class = BannerSerializer
    permission_classes = [AllowAny]


class GenreView(ReadOnlyModelViewSet):
    queryset = GenreModel.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [AllowAny]
