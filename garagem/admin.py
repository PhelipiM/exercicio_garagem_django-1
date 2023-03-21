from django.contrib import admin

from .models import Categoria, Marca, Acessorio, Cor

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Acessorio)
admin.site.register(Cor)
