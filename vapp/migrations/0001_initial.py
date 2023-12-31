# Generated by Django 4.2.5 on 2023-10-27 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Comentario')),
                ('user', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Empresa')),
                ('born', models.IntegerField(verbose_name='Año de fundación')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='Motorcycle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Motocicleta')),
                ('born', models.IntegerField(verbose_name='Año de creación')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('maximum_speed', models.IntegerField(blank=True, null=True, verbose_name='Velocidad Maxima')),
                ('image', models.ImageField(blank=True, null=True, upload_to='vehicles/', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vapp.company')),
            ],
            options={
                'verbose_name': 'Motocicleta',
                'verbose_name_plural': 'Motocicletas',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Automóvil')),
                ('born', models.IntegerField(verbose_name='Año de creación')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('maximum_speed', models.IntegerField(blank=True, null=True, verbose_name='Velocidad Maxima')),
                ('image', models.ImageField(blank=True, null=True, upload_to='vehicles/', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vapp.company')),
            ],
            options={
                'verbose_name': 'Automóvil',
                'verbose_name_plural': 'Automóviles',
            },
        ),
    ]
