from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PerevalViewSet, UserViewSet, CoordsViewSet, LevelViewSet, ImageViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Настройки Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Sprints Factory API",
        default_version='v1',
        description="API для мобильного приложения ФСТР",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@fstr.local"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'coords', CoordsViewSet)
router.register(r'levels', LevelViewSet)
router.register(r'images', ImageViewSet)
router.register(r'pereval', PerevalViewSet, basename='pereval')

urlpatterns = [
    # Документация Swagger
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Основные API endpoints
    path('', include(router.urls)),
]