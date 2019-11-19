# Generated by Django 2.2.4 on 2019-11-11 18:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia', '0031_auto_20191111_1351'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classemodel',
            old_name='cidade',
            new_name='cidadeEstado',
        ),
        migrations.RenameField(
            model_name='colaboradormodel',
            old_name='cidade',
            new_name='cidadeEstado',
        ),
        migrations.RemoveField(
            model_name='alunomodel',
            name='classe',
        ),
        migrations.AlterField(
            model_name='cidademodel',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 11, 18, 36, 2, 371566, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='colaboradormodel',
            name='dataNasc',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 11, 18, 36, 2, 372563, tzinfo=utc)),
        ),
    ]
