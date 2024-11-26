from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BannerView, CategoryView, CommentView, FilmView, GenreView

app_name = "fandub"


router = DefaultRouter()
router.register("banners", BannerView, basename="banners")
router.register("genre", GenreView, basename="genre")
router.register("category", CategoryView, basename="category")
router.register("film", FilmView, basename="film")
router.register("comment", CommentView, basename="comment")

urlpatterns = [
    path("", include(router.urls)),
]
