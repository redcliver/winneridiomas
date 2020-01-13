# Generated by Django 2.2.4 on 2019-12-10 03:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0044_auto_20191210_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventomodel',
            name='data_cadastro',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 10, 3, 48, 38, 895825, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eventomodel',
            name='data_evento',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 10, 3, 48, 38, 895796, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eventomodel',
            name='data_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 10, 3, 48, 38, 895739, tzinfo=utc)),
        ),
    ]