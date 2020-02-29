# Generated by Django 2.2.4 on 2020-02-28 03:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0049_auto_20200227_2122'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Photo',
            new_name='imagensModel',
        ),
        migrations.RemoveField(
            model_name='eventomodel',
            name='imagem',
        ),
        migrations.AlterField(
            model_name='eventomodel',
            name='data_cadastro',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 28, 3, 40, 8, 325348, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eventomodel',
            name='data_evento',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 28, 3, 40, 8, 325348, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eventomodel',
            name='data_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 28, 3, 40, 8, 325348, tzinfo=utc)),
        ),
    ]