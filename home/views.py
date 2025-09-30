from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Curso
from django.core.paginator import Paginator

# Create your views here.

def home_visual(request):
    return render(request,'home/home.html')




def home(request):
    cursos = Curso.objects.all()  # Busca todos os cursos
    search_query = request.GET.get('search', '')
    if search_query:
        cursos = cursos.filter(titulo__icontains=search_query) | cursos.filter(descricao_curta__icontains=search_query)
    
    # Ordenação por ano/mês (se data_inicio existir)
    sort_by = request.GET.get('sort', '')
    if sort_by == 'ano':
        cursos = cursos.order_by('data_inicio__year')
    elif sort_by == 'mes':
        cursos = cursos.order_by('data_inicio__month')

    paginator = Paginator(cursos, 12)  # 8 cursos por página (ajuste ao seu grid)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}  # Use page_obj para paginação
    return render(request, 'home/home.html', context)


def detalhe(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    context = {
        'curso': curso
    }
    return render(request, 'home/detalhe.html', context)

def sobre(request):
    return render(request, 'home/sobre.html')