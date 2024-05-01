from django.db import models

# Create your models here.
class Livros(models.Model):
    idLivro = models.BigAutoField(primary_key=True)
    capa = models.ImageField()
    titulo = models.CharField(max_length=70)
    autor = models.CharField(max_length=70)
    editora = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)
    ano_ed = models.CharField(max_length=4)
    preco = models.FloatField(default=0)

class Cliente(models.Model):
    idCliente = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=70)
    cpf = models.CharField(max_length=11)
    contato = models.CharField(max_length=20)
    endereco = models.CharField(max_length=150)
    flamenguista = models.BooleanField()

class Vendedor(models.Model):
    idVendedor = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=70)
    cpf = models.CharField(max_length=11)
    contato = models.CharField(max_length=20)
    endereco = models.CharField(max_length=150)
    pis = models.CharField(max_length=11)

class Vendas(models.Model):
    idVenda = models.BigAutoField(primary_key=True)
    idCliente = models.ForeignKey("Cliente", on_delete=models.CASCADE)
    idVendedor = models.ForeignKey("Vendedor", on_delete=models.CASCADE)
    #idPedido = models.ForeignKey("Item", on_delete=models.CASCADE)

class Item(models.Model):
    idItem = models.BigAutoField(primary_key=True)
    idPedido = models.ForeignKey("Pedido", on_delete=models.CASCADE)
    idLivro = models.ForeignKey("Livros", on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    total = models.IntegerField()

class Pedido(models.Model):
    idPedido = models.BigAutoField(primary_key=True)
    idCliente = models.ForeignKey("Cliente", on_delete=models.CASCADE, default="2121")