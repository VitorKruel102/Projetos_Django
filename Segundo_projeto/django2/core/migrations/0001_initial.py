# Generated by Django 4.1.4 on 2022-12-06 18:13

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de Atualização')),
                ('ativo', models.DateField(default=False, verbose_name='Ativo?')),
                ('nome', models.TextField(max_length=100, verbose_name='Nome')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
                ('estoque', models.TextField(verbose_name='Estoque')),
                ('imagem', stdimage.models.StdImageField(force_min_size=False, upload_to='produtos', variations={'thumb': (124, 124)}, verbose_name='Imagem')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=100, verbose_name='Slug')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
