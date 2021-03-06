# Generated by Django 2.2.4 on 2020-03-10 17:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia', '0044_auto_20200310_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cidademodel',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 10, 17, 24, 49, 382916, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='colaboradormodel',
            name='dataNasc',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 10, 17, 24, 49, 383305, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='perguntamodel',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 10, 17, 24, 49, 385391, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='respostamodel',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 10, 17, 24, 49, 385076, tzinfo=utc)),
        ),
    ]
