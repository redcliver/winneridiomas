# Generated by Django 2.2.4 on 2020-02-28 04:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia', '0012_auto_20200228_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cidademodel',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 28, 4, 52, 42, 280574, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='colaboradormodel',
            name='dataNasc',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 28, 4, 52, 42, 280574, tzinfo=utc)),
        ),
    ]
