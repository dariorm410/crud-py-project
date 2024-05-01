from django.forms import ModelForm
from appcrud.models import Livros
from appcrud.models import Cliente
from appcrud.models import Vendedor
from appcrud.models import Vendas
from appcrud.models import Item
from appcrud.models import Pedido

# Cria a classe de formulário.
class LivrosForm(ModelForm):
     class Meta:
         #o modelo toma como base o metodo LIVROS
         model = Livros
         #define os campos que estarão no formulário
         fields = ["titulo", "autor", "editora", "genero","ano_ed","preco"]

class VendedorForm(ModelForm):
     class Meta:
         #o modelo toma como base o metodo LIVROS
         model = Vendedor
         #define os campos que estarão no formulário
         fields = ["nome", "cpf", "contato", "endereco","pis"]

# Cria a classe de formulário.
class ClienteForm(ModelForm):
     class Meta:
         #o modelo toma como base o metodo LIVROS
         model = Cliente
         #define os campos que estarão no formulário
         fields = ["nome", "cpf","contato", "endereco","flamenguista"]


