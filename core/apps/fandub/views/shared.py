from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet

from core.http.paginations import CustomPagination

from ..models import BannerModel, CommentModel, GenreModel
from ..permissions import CommentPermission
from ..serializers import BannerSerializer, CommentSerializer, GenreSerializer


class BannerView(ReadOnlyModelViewSet):
    queryset = BannerModel.objects.all()
    serializer_class = BannerSerializer
    permission_classes = [AllowAny]


class GenreView(ReadOnlyModelViewSet):
    queryset = GenreModel.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [AllowAny]


class CommentView(CreateModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer) -> None:
        serializer.save(user=self.request.user)

    @action(methods=["GET"], detail=True, url_name="film", url_path="film")
    def film(self, request, pk):
        queryset = self.get_queryset().filter(film_id=pk)
        pagination = CustomPagination()
        data = pagination.paginate_queryset(queryset, request)
        return pagination.get_paginated_response(self.get_serializer(data, many=True).data)

    def get_permissions(self):
        perms = []
        match self.action:
            case "destroy" | "update":
                perms.extend([IsAuthenticated, CommentPermission])
            case "create":
                perms.extend([IsAuthenticated])
        self.permission_classes = perms
        return super().get_permissions()
