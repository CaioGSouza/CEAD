
from django.urls import path
from . import views


urlpatterns = [
   
    path("", views.home, name='home')
]



    # Exemplo de uma URL futura para a página de detalhes de um curso
    # path('cursos/<int:curso_id>/', views.detalhe_curso, name='detalhe_curso'),
