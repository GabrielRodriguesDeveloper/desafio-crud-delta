# Generated by Django 4.0.1 on 2022-01-14 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_categoria', models.CharField(max_length=100)),
                ('descricao_categoria', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=100)),
                ('preco_produto', models.IntegerField()),
                ('descricao_produto', models.CharField(max_length=150)),
                ('categoria_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='crud.categoria')),
            ],
        ),
    ]
