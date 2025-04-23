from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PerevalViewSet, UserViewSet, CoordsViewSet, LevelViewSet, ImageViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'coords', CoordsViewSet)
router.register(r'levels', LevelViewSet)
router.register(r'images', ImageViewSet)
router.register(r'pereval', PerevalViewSet, basename='pereval')

urlpatterns = [
    path('', include(router.urls)),
]