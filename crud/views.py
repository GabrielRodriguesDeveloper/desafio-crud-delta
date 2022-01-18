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
    try:
        produto = Produtos.objects.get(pk=produto_id)
    except:
        messages.add_message(request, messages.ERROR, "O produto não existe, tente colocar um id existente")
        return redirect('produtos')

    return render(request, 'crud/ver_produto.html', {'produto' : produto})


def ver_categoria(request, categoria_id):
    try:
        categoria = Categoria.objects.get(pk=categoria_id)
    except:
        messages.add_message(request, messages.ERROR, "A categoria não existe, tente colocar um id existente")
        return redirect('categorias')

    return render(request, 'crud/ver_categoria.html', {'categoria' : categoria})



def editar_produto(request, produto_id):
    try:
        produto = Produtos.objects.get(pk=produto_id)
        form = ProdutosForm(instance=produto)
    except:
        messages.add_message(request, messages.ERROR, "O produto não existe, tente colocar um id existente")
        return redirect("produtos")
    return render(request, 'crud/produtos_form.html', {'produto' : produto, 'form' : form})


def editar_categoria(request, categoria_id):
    try:
        categoria = Categoria.objects.get(pk=categoria_id)
        form = CategoriaForm(instance=categoria)
    except:
        messages.add_message(request, messages.ERROR, "A categoria não existe, tente colocar um id existente")
        return redirect("categorias")

    return render(request, 'crud/categorias_form.html', {'categoria' : categoria, 'form' : form})


def produto_update(request, produto_id):
    try:
        produto = Produtos.objects.get(pk=produto_id)
        form = ProdutosForm(request.POST or None, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produtos')
    except:
        messages.add_message(request, messages.ERROR, "Você está tentando atualizar um produto inexistente, tente colocar um id existente")
        return redirect("produtos")

    return redirect('index')


def categoria_update(request, categoria_id):
    try:
        categoria = Categoria.objects.get(pk=categoria_id)
        form = CategoriaForm(request.POST or None, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categorias')
    except:
        messages.add_message(request, messages.ERROR, "Você está tentando atualizar uma categoria inexistente, tente colocar um id existente")
        return redirect("categorias")

    return redirect('index')


def deletar_produto(request, produto_id):
    try:
        produto = Produtos.objects.get(pk=produto_id)
        produto.delete()
    except:
        messages.add_message(request, messages.ERROR, "Você está tentando deletar um produto inexistente, tente colocar id existente")
        return redirect('produtos')

    return redirect('produtos')



def deletar_categoria(request, categoria_id):
    try:
        categoria = Categoria.objects.get(pk=categoria_id)
        categoria.delete()
    except:
        messages.add_message(request, messages.ERROR, "A categoria não pode ser deletada, pois está sendo utilizada em um produto ou não existe")
        return redirect('categorias')
        
    return redirect('categorias')