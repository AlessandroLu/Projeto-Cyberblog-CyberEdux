from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cyberblog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view,),
    path('login/', views.login_view, name='login'),
    path('deslogar/', views.logout_view, name="logout"),
    path('cadastro/', views.cadastro_page, name='cadastro'),
    path('home/', views.home_page, name='home'),
    path('publicar/', views.publicar_page, name='publicar'),
    path('home/<slug:slug>', views.post_view, name='post'),
    path('programação/', views.programação, name='programação'),
    path('cyber-segurança/', views.cyber_segurança, name='cyber'),
    path('tecnologia/', views.tecnologia, name='tecnologia'),
    path('vagas-de-emprego/', views.vagas_de_emprego, name='emprego')
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
