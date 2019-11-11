# Generated by Django 2.2.4 on 2019-11-11 02:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia', '0016_auto_20191110_2320'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alunomodel',
            old_name='city',
            new_name='cidade',
        ),
        migrations.AlterField(
            model_name='alunomodel',
            name='dataNasc',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 11, 2, 20, 41, 568358, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cidademodel',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 11, 2, 20, 41, 567492, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='colaboradormodel',
            name='dataNasc',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 11, 2, 20, 41, 569589, tzinfo=utc)),
        ),
    ]
