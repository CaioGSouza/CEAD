from django.http import HttpResponse

def teste_view(request):
    return HttpResponse('olá, bem vindo ao teste')

def abertura(request):
    return HttpResponse('bem vindo!')