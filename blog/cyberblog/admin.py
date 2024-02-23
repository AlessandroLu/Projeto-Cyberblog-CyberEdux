from django.contrib import admin
from .models import Usuario, Publicar, Comentario


@admin.register(Publicar)
class PublicarAdmin(admin.ModelAdmin):
    list_display = ['autor', 'slug']

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
    
@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['autor']


