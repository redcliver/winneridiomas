# Generated by Django 2.2.4 on 2020-03-10 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20200310_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perguntasexecutadas',
            name='pergunta',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]