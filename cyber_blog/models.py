from django.db import models
from django.utils.text import slugify
from django.conf import settings

    
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nome_categoria = models.TextField(max_length=100)
    

class Publicar(models.Model):
    id_publicação = models.AutoField(primary_key=True)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.TextField(max_length=200, unique=True)
    subtitulo = models.TextField(max_length=100)
    categoria_publicação = models.ForeignKey(Categoria, related_name='categoria', on_delete=models.CASCADE)
    resumo = models.TextField()
    publicado_em = models.DateField(auto_now_add=True)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='imagens')
    slug = models.SlugField(max_length=180, unique=True)


    def save (self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        
        return super().save(*args, **kwargs)
    
            
class Comentario(models.Model):
    post = models.ForeignKey(Publicar, related_name='comentarios', on_delete=models.CASCADE)       
    autor =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    conteudo= models.TextField() 
    publicado_em= models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-publicado_em']
