from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso

# Create your views here.

def home_visual(request):
    return render(request,'home/home.html')



def home(request):
    cursos = Curso.objects.all()  # Busca todos os cursos do banco de dados
    context = {'cursos': cursos}
    return render(request, 'home/home.html', context)

