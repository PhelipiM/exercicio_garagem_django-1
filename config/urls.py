from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from garagem.views import MarcaViewSet, CategoriaViewSet, CorViewSet, AcessorioViewSet, VeiculoViewSet, ModeloViewSet

router = DefaultRouter()
router.register(r"marcas", MarcaViewSet)
router.register(r"categoria", CategoriaViewSet)
router.register(r"cor", CorViewSet)
router.register(r"acessório", AcessorioViewSet)
router.register(r"veículo", VeiculoViewSet)
router.register(r"modelo", ModeloViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
