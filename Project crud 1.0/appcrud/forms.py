from django.forms import ModelForm
from appcrud.models import Livros, Clientes, Vendedor

# Cria a classe de formulário para livros.
class LivrosForm(ModelForm):
     class Meta:
         #o modelo toma como base o metodo LIVROS
         model = Livros
         #define os campos que estarão no formulário
         fields = ["titulo", "autor", "editora", "genero","ano_ed"]


# Cria a classe de formulário para clientes.
class ClientesForm(ModelForm):
     class Meta:
         #o modelo toma como base o metodo Clientes
         model = Clientes
         #define os campos que estarão no formulário
         fields = ["nome", "contato", "CPF", "endereco","flamenguista", "onepiece"]


# Cria a classe de formulário para vendedor.
class VendedorForm(ModelForm):
     class Meta:
         #o modelo toma como base o metodo Vendedor
         model = Vendedor
         #define os campos que estarão no formulário
         fields = ["nome", "contato", "CPF", "endereco","PIS"]