from django.urls import path
from app_EcoBinLocator import views

urlpatterns = [
    path('', views.pagina_login, name='pagina_login'),  # URL para a página de login
    path('cadastro/', views.pagina_cadastro, name='pagina_cadastro'),  # URL para a página de cadastro
    path('home/', views.pagina_home, name='pagina_home'),  # URL para a página home.html
    path('denuncia/', views.pagina_denuncia, name='pagina_denuncia'),
    path('suporte/', views.pagina_suporte, name='pagina_suporte'),
    path('instrucoes/', views.pagina_instrucoes, name='pagina_instrucoes'),
    path('endereco/', views.pagina_endereco, name='pagina_endereco'),
    path('mapa/', views.pagina_mapa, name='pagina_mapa'),
]

