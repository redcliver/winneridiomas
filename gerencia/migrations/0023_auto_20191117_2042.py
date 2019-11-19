# Generated by Django 2.2.4 on 2019-11-17 23:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia', '0022_auto_20191117_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunomodel',
            name='dataNasc',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 17, 23, 42, 43, 743152, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cidademodel',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 17, 23, 42, 43, 742368, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='colaboradormodel',
            name='dataNasc',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 17, 23, 42, 43, 744201, tzinfo=utc)),
        ),
    ]
