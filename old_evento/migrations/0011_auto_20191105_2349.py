# Generated by Django 2.2.4 on 2019-11-06 02:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0010_auto_20191105_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventomodel',
            name='data_cadastro',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 6, 2, 49, 5, 173623, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eventomodel',
            name='data_evento',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 6, 2, 49, 5, 173592, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eventomodel',
            name='data_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 6, 2, 49, 5, 173557, tzinfo=utc)),
        ),
    ]