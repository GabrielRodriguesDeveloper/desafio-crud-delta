from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('produtos/', views.produtos, name="produtos"),
    path('categorias/', views.categorias, name="categorias"),
    path('produtos/produtos_form/', views.produtos_form, name="produtos_form"),
    path('categorias/categoria_form/', views.categoria_form, name="categoria_form"),
    path('cria_produtos/', views.cria_produtos, name="cria_produtos"),
    path('cria_categorias/', views.cria_categorias, name="cria_categorias"),
    path('produtos/ver_produto/<int:produto_id>', views.ver_produto, name="ver_produto"),
    path('categorias/ver_categoria<int:categoria_id>', views.ver_categoria, name="ver_categoria"),
    path('editar_produto/<int:produto_id>', views.editar_produto, name="editar_produto"),
    path('editar_categoria/<int:categoria_id>', views.editar_categoria, name="editar_categoria"),
    path('produto_update/<int:produto_id>', views.produto_update, name="produtoUpdate"),
    path('deletar_produto/<int:produto_id>', views.deletar_produto, name="deletar_produto"),
    path('deletar_categoria/<int:categoria_id>', views.deletar_categoria, name="deletar_categoria"),
]