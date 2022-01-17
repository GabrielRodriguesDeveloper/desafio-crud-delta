from django.db import models


class Categoria(models.Model):
    nome_categoria = models.CharField(max_length = 100)
    descricao_categoria = models.CharField(max_length = 150)



class Produtos(models.Model):
    nome_produto = models.CharField(max_length = 100)
    preco_produto = models.IntegerField()
    descricao_produto = models.CharField(max_length = 150)
    categoria_id = models.ForeignKey(Categoria, on_delete = models.DO_NOTHING)
    