
from django.urls import path
from . import views


urlpatterns = [
   
    path("", views.home, name='home'),
    path("detalhe/<int:curso_id>/", views.detalhe, name='detalhe'),  # Detalhe de um curso
    path("sobre/", views.sobre, name='sobre')
]


