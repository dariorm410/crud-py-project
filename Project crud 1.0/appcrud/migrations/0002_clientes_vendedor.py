# Generated by Django 5.0.3 on 2024-04-30 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcrud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCliente', models.IntegerField()),
                ('nome', models.CharField(max_length=70)),
                ('contato', models.CharField(max_length=15)),
                ('CPF', models.CharField(max_length=11)),
                ('endereco', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idVendedor', models.IntegerField()),
                ('nome', models.CharField(max_length=70)),
                ('contato', models.CharField(max_length=15)),
                ('CPF', models.CharField(max_length=11)),
                ('endereco', models.CharField(max_length=40)),
                ('PIS', models.CharField(max_length=11)),
            ],
        ),
    ]
