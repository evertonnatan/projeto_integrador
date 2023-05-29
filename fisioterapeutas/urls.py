from django.urls import path
from . import views

app_name = 'fisioterapeutas'

urlpatterns = [
    path('registro/fisioterapeuta/', views.fisioterapeuta_cadastro, name='fisioterapeuta_cadastro'),
    path('registro/especialidade/', views.especialidade_cadastro, name='especialidade_cadastro'),
    path('agendar/', views.agenda_cadastro, name='agendar_consulta'),
    path('agendar/atualizar/<int:pk>/', views.agenda_atualizar, name='agendar_consulta_atualizar'),
    path('agendar/apagar/<int:pk>/', views.agenda_deletar, name='agendar_consulta_deletar'),
    path('minhas/consultas/', views.agenda_lista, name="agenda_lista"),
    path('admim/lista/fisioterapeutas/', views.fisioterapeuta_lista, name="fisioterapeutas_lista"),
    path('admim/lista/especialidades/', views.especialidade_lista, name="especialidade_lista")
    
]