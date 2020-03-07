# Generated by Django 2.2.4 on 2020-03-06 11:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_indicacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='testeNivelamento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=1000)),
                ('email', models.CharField(blank=True, max_length=1000, null=True)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('data_cadastro', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
