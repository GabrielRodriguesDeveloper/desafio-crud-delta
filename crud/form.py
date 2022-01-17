from django.forms import ModelForm
from crud.models import Produtos, Categoria

# Create the form class.
class ProdutosForm(ModelForm):
     class Meta:
         model = Produtos
         fields = ['id', 'nome_produto', 'preco_produto', 'descricao_produto', 'categoria_id']


class CategoriaForm(ModelForm):
     class Meta:
         model = Categoria
         fields = ['id', 'nome_categoria', 'descricao_categoria']