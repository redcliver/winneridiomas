# Generated by Django 2.2.4 on 2019-11-06 02:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia', '0004_auto_20191105_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunomodel',
            name='dataNasc',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 6, 2, 49, 5, 169794, tzinfo=utc)),
        ),
    ]
