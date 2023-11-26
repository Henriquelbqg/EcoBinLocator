from django.urls import path
from app_EcoBinLocator import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pagina_login, name='login'),
    path('cadastro/', views.pagina_cadastro, name='cadastro'),
    path('home/', views.pagina_home, name='home'),
    path('denuncia/', views.pagina_denuncia, name='denuncia'),
    path('suporte/', views.pagina_suporte, name='suporte'),
    path('instrucoes/', views.pagina_instrucoes, name='instrucoes'),
    path('endereco/', views.pagina_endereco, name='endereco'),
    path('mapa/', views.pagina_mapa, name='mapa'),
    path('checklist/', views.pagina_checklist, name='checklist'),
    path('produtos/', views.pagina_produtos, name='produtos')
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
