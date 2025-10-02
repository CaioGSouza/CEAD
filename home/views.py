from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Curso
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  # Esta linha é essencial
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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

def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso! Faça login.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'home/cadastro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login realizado com sucesso!')
                return redirect('home')
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
        else:
            messages.error(request, 'Formulário inválido.')
    else:
        form = AuthenticationForm()
    return render(request, 'home/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Você saiu da conta.')
    return redirect('home')