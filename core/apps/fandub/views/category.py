from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny
from ..models import CategoryModel
from ..serializers import CategorySerializer


class CategoryView(ReadOnlyModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
