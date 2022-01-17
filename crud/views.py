from django.shortcuts import render, redirect
from crud.form import ProdutosForm, CategoriaForm
from .models import Produtos, Categoria
from django.contrib import messages


def index(request):
    return render(request, 'crud/index.html')


def produtos(request):
    produtos = Produtos.objects.all()
    return render(request, 'crud/produtos.html', {'produtos' : produtos})


def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'crud/categorias.html', {'categorias' : categorias})


def produtos_form(request):
    produtos = ProdutosForm()
    return render(request, 'crud/produtos_form.html', {'form' : produtos})


def categoria_form(request):
    categorias = CategoriaForm()
    return render(request, 'crud/categorias_form.html', {'form' : categorias})


def cria_produtos(request):
    produtos_form = ProdutosForm(request.POST or None)
    if produtos_form.is_valid():
        produtos_form.save()
        return redirect('index')


def cria_categorias(request):
    categorias_form = CategoriaForm(request.POST or None)
    if categorias_form.is_valid():
        categorias_form.save()
        return redirect('index')

    return redirect('index')


def ver_produto(request, produto_id):
    produto = Produtos.objects.get(pk=produto_id)

    return render(request, 'crud/ver_produto.html', {'produto' : produto})


def ver_categoria(request, categoria_id):
    categoria = Categoria.objects.get(pk=categoria_id)

    return render(request, 'crud/ver_categoria.html', {'categoria' : categoria})



def editar_produto(request, produto_id):
    produto = Produtos.objects.get(pk=produto_id)
    form = ProdutosForm(instance=produto)
    return render(request, 'crud/produtos_form.html', {'produto' : produto, 'form' : form})


def editar_categoria(request, categoria_id):
    categoria = Categoria.objects.get(pk=categoria_id)
    form = CategoriaForm(instance=categoria)
    return render(request, 'crud/categorias_form.html', {'categoria' : categoria, 'form' : form})


def produto_update(request, produto_id):
    produto = Produtos.objects.get(pk=produto_id)
    form = ProdutosForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect('index')
    return redirect('index')


def deletar_produto(request, produto_id):
    produto = Produtos.objects.get(pk=produto_id)
    produto.delete()
    return redirect('produtos')


def deletar_categoria(request, categoria_id):
    categoria = Categoria.objects.get(pk=categoria_id)
    try:
        categoria.delete()
    except:
        messages.add_message(request, messages.ERROR, "A categoria não pode ser deletada, pois está sendo utilizada em um produto")
        return redirect('categorias')
    return redirect('categorias')