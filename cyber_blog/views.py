from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseBadRequest, HttpResponse
from .models import Publicar, Comentario, Categoria
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def cadastro_page(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html', {
            'username_igual': False
        })
    elif request.method == 'POST':
        username = request.POST.get('username')
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username_auth = User.objects.filter(username=username)
        email_auth = User.objects.filter(email=email)
        if username_auth:
            return render(request, 'cadastro.html', {
            'username_igual': True,
        })
        elif email_auth:
            return render(request, 'cadastro.html', {
            'email_igual': True
        })                 
        user = User.objects.create_user(username, email, password)
        user.first_name = nome
        user.last_name = sobrenome  
        user.save()
        login(request, user)
        return HttpResponseRedirect('/login')
    else:
        return HttpResponseBadRequest

@login_required(login_url='/login')    
def publicar_page(request):
    categorias = Categoria.objects.all()
    if request.method == 'GET':
        return render(request, 'publicar.html', {
            'categorias': categorias
        })
    elif request.method == 'POST':
        titulo = request.POST.get('titulo')
        subtitulo = request.POST.get('subtitulo')
        autor_id = request.POST.get('autor')
        autor = User.objects.get(pk=autor_id)
        resumo = request.POST.get('resumo')
        categoria_id = request.POST.get('categoria')
        categoria = Categoria.objects.get(pk=categoria_id)
        publicado_em = request.POST.get('publicado_em')
        conteudo = request.POST.get('conteudo')
        imagem = request.FILES['imagem']
        publicar = Publicar()
        publicar.titulo = titulo
        publicar.subtitulo = subtitulo
        publicar.autor = autor
        publicar.resumo = resumo
        publicar.categoria_publicação = categoria
        publicar.imagem = imagem
        publicar.publicado_em = publicado_em
        publicar.conteudo = conteudo  
        publicar.save()
        return HttpResponseRedirect('/home')
    else:
        return HttpResponseBadRequest

    
def home_view(request):
    return HttpResponseRedirect('/home')   

def home_page(request):
    post = Publicar.objects.order_by('-publicado_em').all()
    return render(request, 'card_post.html', { 
    'post' : post,
    })

def post_view(request, slug):
    post = Publicar.objects.get(slug=slug)
    if request.method == 'POST':
            autor_id = request.POST.get('autor')
            autor = User.objects.get(pk=autor_id)
            publicado_em = request.POST.get('publicado_em')
            conteudo = request.POST.get('conteudo')
            comentar = Comentario(autor=autor, conteudo=conteudo,publicado_em=publicado_em, post=post)
            comentar.save()
            return redirect('post', slug=post.slug)
    return render(request, 'post.html', {
        'post':post,
    })


def programação(request):
    posts = Publicar.objects.filter(categoria_publicação='1')
    return render(request, 'card_post.html', { 
    'posts' : posts,
    })

def cyber_segurança(request):
    posts = Publicar.objects.filter(categoria_publicação='2')
    return render(request, 'card_post.html', { 
    'posts' : posts,
    })

def tecnologia(request):
    posts = Publicar.objects.filter(categoria_publicação='3')
    return render(request, 'card_post.html', { 
    'posts' : posts,
    })

def vagas_de_emprego(request):
    posts = Publicar.objects.filter(categoria_publicação='4')
    return render(request, 'card_post.html', { 
    'posts' : posts,
    })

def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'incorrect_login': False
        })
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/home')
        else:
            return render(request, 'login.html', {
            'incorrect_login': True
        })
    else:
        return HttpResponseBadRequest()

@login_required(login_url='/login')    
def logout_view(request):
    logout(request)    
    return HttpResponseRedirect('/home')