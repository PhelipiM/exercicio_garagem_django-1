from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from garagem.models import Modelo
from garagem.serializers import ModeloSerializer, ModeloDetailSerializer

class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrive"]:
            return ModeloDetailSerializer
        return ModeloSerializer