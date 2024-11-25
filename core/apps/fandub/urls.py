from django.urls import path, include
from .views import BannerView, GenreView, CategoryView, FilmView, CommentView
from rest_framework.routers import DefaultRouter

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
