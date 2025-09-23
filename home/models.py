from django.db import models

# Create your models here.
class HomeModels(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True,blank=True)
    completo = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.nome
    
class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descricao_curta = models.TextField(help_text="Descrição que aparece na miniatura do curso.")
    imagem = models.ImageField(upload_to='cursos/imagens/')
    # Adicione outros campos necessários aqui

    def __str__(self):
        return self.titulo