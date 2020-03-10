# Generated by Django 2.2.4 on 2020-03-10 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia', '0044_auto_20200310_1424'),
        ('website', '0007_auto_20200310_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perguntasexecutadas',
            name='perguntaID',
        ),
        migrations.AddField(
            model_name='perguntasexecutadas',
            name='pergunta',
            field=models.ForeignKey(default=1, on_delete='models.CASCADE', to='gerencia.perguntaModel'),
            preserve_default=False,
        ),
    ]
