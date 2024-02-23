from django.db import models
from django.utils.text import slugify



class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    username= models.CharField(max_length=50)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    
    

class Publicar(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.TextField(max_length=200, unique=True)
    autor = models.TextField()
    subtitulo = models.TextField()
    categoria = models.TextField()
    resumo = models.TextField()
    publicado_em = models.DateField(auto_now_add=True)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='imagens')
    slug = models.SlugField(max_length=180, unique=True, blank=True, null=True )


    def save (self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        
        return super().save(*args, **kwargs)
    
            
class Comentario(models.Model):
    post = models.ForeignKey(Publicar, related_name='comentarios', on_delete=models.PROTECT)       
    autor = models.CharField(max_length=200)
    conteudo= models.TextField() 
    publicado_em= models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-publicado_em']

