# Generated by Django 2.2.4 on 2020-03-10 17:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_testenivelamento_respostas'),
    ]

    operations = [
        migrations.CreateModel(
            name='perguntasExecutadas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('perguntaID', models.CharField(blank=True, max_length=1000, null=True)),
                ('data_cadastro', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='testenivelamento',
            name='executadas',
            field=models.ManyToManyField(to='website.perguntasExecutadas'),
        ),
    ]