# Generated by Django 2.2.4 on 2020-03-10 12:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia', '0041_auto_20200310_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cidademodel',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 10, 12, 11, 45, 62441, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='colaboradormodel',
            name='dataNasc',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 10, 12, 11, 45, 62835, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='perguntamodel',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 10, 12, 11, 45, 64911, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='respostamodel',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 10, 12, 11, 45, 64596, tzinfo=utc)),
        ),
    ]
