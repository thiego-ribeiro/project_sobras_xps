from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_sobras, name='lista_sobras'),
    path('cadastrar/', views.cadastrar_sobra, name='cadastrar_sobra'),
    path('doar/<int:id>/', views.marcar_como_doado, name='marcar_como_doado'),
]
