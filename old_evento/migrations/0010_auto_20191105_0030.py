# Generated by Django 2.2.4 on 2019-11-05 03:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0009_auto_20191105_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventomodel',
            name='data_cadastro',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 5, 3, 30, 17, 535446, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eventomodel',
            name='data_evento',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 5, 3, 30, 17, 535420, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eventomodel',
            name='data_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 5, 3, 30, 17, 535379, tzinfo=utc)),
        ),
    ]