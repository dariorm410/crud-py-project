# Generated by Django 5.0.3 on 2024-03-14 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capa', models.ImageField(upload_to='')),
                ('titulo', models.CharField(max_length=70)),
                ('autor', models.CharField(max_length=70)),
                ('editora', models.CharField(max_length=30)),
                ('genero', models.CharField(max_length=30)),
                ('ano_ed', models.IntegerField()),
            ],
        ),
    ]
