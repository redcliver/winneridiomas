# Generated by Django 2.2.4 on 2020-03-16 02:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia', '0050_merge_20200315_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cidademodel',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 2, 49, 1, 416936, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='colaboradormodel',
            name='dataNasc',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 2, 49, 1, 417804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='perguntamodel',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 2, 49, 1, 422618, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='respostamodel',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 2, 49, 1, 421962, tzinfo=utc)),
        ),
    ]
