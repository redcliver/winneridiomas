# Generated by Django 2.2.4 on 2020-03-10 10:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia', '0028_auto_20200310_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cidademodel',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 10, 10, 58, 0, 329331, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='colaboradormodel',
            name='dataNasc',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 10, 10, 58, 0, 329724, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='perguntamodel',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 10, 10, 58, 0, 331774, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='respostamodel',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 10, 10, 58, 0, 331506, tzinfo=utc)),
        ),
    ]