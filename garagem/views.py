from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from garagem.models import Marca, Categoria, Cor, Acessorio, Veiculo, Modelo
from garagem.serializers import MarcaSerializer, CategoriaSerializer, CorSerializer, AcessorioSerializer
from garagem.serializers import VeiculoSerializer, VeiculoDetailSerializer, ModeloSerializer, ModeloDetailSerializer, VeiculoListSerializer 
# from rest_framework.permissions import IsAuthenticated


class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    # permission_classes = [IsAuthenticated]


class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer


class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer


class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrive"]:
            return ModeloDetailSerializer
        return ModeloSerializer


class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return VeiculoListSerializer
        elif self.action == "retrieve":
            return VeiculoDetailSerializer
        return VeiculoSerializer

