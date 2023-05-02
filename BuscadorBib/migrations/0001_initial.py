# Generated by Django 4.2 on 2023-05-01 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estante', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Repisa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repisa', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500)),
                ('autor', models.CharField(max_length=500)),
                ('descripcion', models.CharField(blank=True, max_length=500)),
                ('estante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BuscadorBib.estante')),
                ('repisa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BuscadorBib.repisa')),
            ],
        ),
    ]