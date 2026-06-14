from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('lista/', views.lista_sobras, name='lista_sobras'),
    path('cadastrar/', views.cadastrar_sobra, name='cadastrar_sobra'),
    path('doar/<int:id>/', views.marcar_como_doado, name='marcar_como_doado'),
    path('solicitacoes/', views.solicitacoes, name='solicitacoes'),
    path('solicitar_materiais/', views.solicitar_materiais, name='solicitar_materiais'),
    path('solicitacao-sucesso/', views.solicitacao_sucesso, name='solicitacao_sucesso'),
]
