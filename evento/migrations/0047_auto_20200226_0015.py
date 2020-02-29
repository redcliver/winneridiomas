# Generated by Django 2.2.4 on 2020-02-26 03:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0046_auto_20200225_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventomodel',
            name='data_cadastro',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 26, 3, 15, 40, 204294, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eventomodel',
            name='data_evento',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 26, 3, 15, 40, 204284, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eventomodel',
            name='data_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 26, 3, 15, 40, 204268, tzinfo=utc)),
        ),
    ]