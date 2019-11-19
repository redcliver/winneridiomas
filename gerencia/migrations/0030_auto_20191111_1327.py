# Generated by Django 2.2.4 on 2019-11-11 16:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia', '0029_auto_20191111_1313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alunomodel',
            old_name='teste',
            new_name='cidade_id',
        ),
        migrations.AddField(
            model_name='classemodel',
            name='cidade',
            field=models.ForeignKey(default=1, on_delete='models.CASCADE', to='gerencia.cidadeModel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='colaboradormodel',
            name='cidade',
            field=models.ForeignKey(default=1, on_delete='models.CASCADE', to='gerencia.cidadeModel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cidademodel',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 11, 16, 27, 38, 108397, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='colaboradormodel',
            name='dataNasc',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 11, 16, 27, 38, 109391, tzinfo=utc)),
        ),
    ]