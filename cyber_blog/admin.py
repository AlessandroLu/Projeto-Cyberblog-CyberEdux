from django.contrib import admin
from .models import Publicar, Comentario, Categoria


@admin.register(Publicar)
class PublicarAdmin(admin.ModelAdmin):
    list_display = ['autor', 'slug']

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['autor']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome_categoria']

