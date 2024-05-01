"""
URL configuration for projectcrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appcrud.views import home, form, create, view, edit, update, delete, home_vendedor, form_vendedor,create_vendedor, view_vendedor, edit_vendedor, update_vendedor, delete_vendedor,clienteForm, createCliente, indexClientesTable, update_c, delete_c, edit_c,index_search,retrieve_livro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'home'), 
    path('form/', form, name = 'form'), 
    path('create/', create, name = 'create'), 
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'), 
    path('delete/<int:pk>/', delete, name='delete'),
    #VENDEDOR
    path('home_vendedor', home_vendedor, name = 'home_vendedor'), 
    path('form_vendedor/', form_vendedor, name = 'form_vendedor'), 
    path('create_vendedor/', create_vendedor, name = 'create_vendedor'), 
    path('view_vendedor/<int:pk>/', view_vendedor, name='view_vendedor'),
    path('edit_vendedor/<int:pk>/', edit_vendedor, name='edit_vendedor'),
    path('update_vendedor/<int:pk>/', update_vendedor, name='update_vendedor'), 
    path('delete_vendedor/<int:pk>/', delete_vendedor, name='delete_vendedor'),  
    #CLIENTE
    path('formCliente/', clienteForm, name = 'clienteForm'), 
    path('createCliente/', createCliente, name='createCliente'),
    path('indexClientesTable/', indexClientesTable, name = 'indexClientesTable'), 
    path('edit_c/<int:pk>/', edit_c, name='edit_c'),
    path('update_c/<int:pk>/', update_c, name='update_c'), 
    path('delete_c/<int:pk>/', delete_c, name='delete_c'),
    #VENDAS

    #ITEM
    path('index_search/', index_search, name = 'index_search'),
    path('retrieve_livro/', retrieve_livro, name='retrieve_livro'),
]
#criado os caminhos na interface
 # a chave primária, como um inteiro, é passada como parametro