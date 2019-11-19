# Generated by Django 2.2.4 on 2019-11-11 02:20

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia', '0015_auto_20191110_2319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alunomodel',
            name='cidade',
        ),
        migrations.AddField(
            model_name='alunomodel',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gerencia.cidadeModel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alunomodel',
            name='dataNasc',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 11, 2, 20, 9, 790150, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cidademodel',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 11, 2, 20, 9, 789149, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='colaboradormodel',
            name='dataNasc',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 11, 2, 20, 9, 791628, tzinfo=utc)),
        ),
    ]