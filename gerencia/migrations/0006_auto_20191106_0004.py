# Generated by Django 2.2.4 on 2019-11-06 03:04

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gerencia', '0005_auto_20191105_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunomodel',
            name='dataNasc',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 6, 3, 4, 30, 732024, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='colaboradorModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liberacao', models.CharField(choices=[('1', 'Ativo'), ('2', 'Bloqueado'), ('3', 'Inativo')], default=1, max_length=1)),
                ('nome', models.CharField(blank=True, max_length=300, null=True)),
                ('sobrenome', models.CharField(blank=True, max_length=400, null=True)),
                ('email', models.CharField(blank=True, max_length=300, null=True)),
                ('cpf', models.CharField(blank=True, max_length=14, null=True)),
                ('rg', models.CharField(blank=True, max_length=15, null=True)),
                ('endereco', models.CharField(blank=True, max_length=400, null=True)),
                ('numero', models.CharField(blank=True, max_length=5, null=True)),
                ('bairro', models.CharField(blank=True, max_length=200, null=True)),
                ('cidade', models.CharField(blank=True, max_length=200, null=True)),
                ('estado', models.CharField(blank=True, max_length=2, null=True)),
                ('cep', models.CharField(blank=True, max_length=9, null=True)),
                ('telefone', models.CharField(blank=True, max_length=14, null=True)),
                ('celular', models.CharField(blank=True, max_length=14, null=True)),
                ('dataNasc', models.DateTimeField(default=datetime.datetime(2019, 11, 6, 3, 4, 30, 733089, tzinfo=utc))),
                ('user', models.OneToOneField(on_delete='models.CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='classeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liberacao', models.CharField(choices=[('1', 'Ativa'), ('2', 'Bloqueada'), ('3', 'Inativa')], default=1, max_length=1)),
                ('nome', models.CharField(blank=True, max_length=300, null=True)),
                ('localizacao', models.CharField(blank=True, max_length=300, null=True)),
                ('capacidade', models.CharField(blank=True, max_length=3, null=True)),
                ('email', models.CharField(blank=True, max_length=300, null=True)),
                ('cidade', models.CharField(blank=True, max_length=200, null=True)),
                ('estado', models.CharField(blank=True, max_length=2, null=True)),
                ('cep', models.CharField(blank=True, max_length=9, null=True)),
                ('user', models.OneToOneField(on_delete='models.CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]