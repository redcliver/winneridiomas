# Generated by Django 2.2.4 on 2020-02-25 22:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia', '0002_auto_20200225_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cidademodel',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 25, 22, 5, 29, 921905, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='colaboradormodel',
            name='dataNasc',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 25, 22, 5, 29, 922904, tzinfo=utc)),
        ),
    ]
