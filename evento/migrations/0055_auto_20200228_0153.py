# Generated by Django 2.2.4 on 2020-02-28 04:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0054_auto_20200228_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventomodel',
            name='data_cadastro',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 28, 4, 53, 18, 770609, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eventomodel',
            name='data_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 28, 4, 53, 18, 770609, tzinfo=utc)),
        ),
    ]
