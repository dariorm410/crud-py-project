from django.db import models

# Create your models here.
class Livros(models.Model):
    capa = models.ImageField()
    titulo = models.CharField(max_length=70)
    autor = models.CharField(max_length=70)
    editora = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)
    ano_ed = models.IntegerField()


class Clientes(models.Model):
    nome = models.CharField(max_length=70)
    contato = models.CharField(max_length=15)
    CPF = models.CharField(max_length= 11)
    endereco = models.CharField(max_length= 40)
    flamenguista = models.BooleanField()
    onepiece = models.BooleanField()


class Vendedor(models.Model):
    nome = models.CharField(max_length=70)
    contato = models.CharField(max_length=15)
    CPF = models.CharField(max_length= 11)
    endereco = models.CharField(max_length= 40)
    PIS = models.CharField(max_length= 11)


    
