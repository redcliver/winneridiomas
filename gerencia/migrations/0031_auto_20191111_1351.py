# Generated by Django 2.2.4 on 2019-11-11 16:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia', '0030_auto_20191111_1327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alunomodel',
            old_name='cidade_id',
            new_name='cidadeEstado',
        ),
        migrations.AlterField(
            model_name='cidademodel',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 11, 16, 50, 58, 138299, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='colaboradormodel',
            name='dataNasc',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 11, 16, 50, 58, 139296, tzinfo=utc)),
        ),
    ]
