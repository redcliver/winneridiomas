# Generated by Django 2.2.4 on 2019-11-05 03:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia', '0002_auto_20191104_2220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alunomodel',
            name='data_nascimento',
        ),
        migrations.AddField(
            model_name='alunomodel',
            name='dataNasc',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 5, 3, 22, 36, 370304, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='alunomodel',
            name='liberacao',
            field=models.CharField(choices=[('1', 'Ativo'), ('2', 'Bloqueado'), ('3', 'Inativo')], default=1, max_length=1),
        ),
    ]
