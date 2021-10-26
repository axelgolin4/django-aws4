# Generated by Django 3.2.8 on 2021-10-24 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=200, verbose_name='Apellidos')),
                ('puesto', models.CharField(max_length=200, verbose_name='Puesto')),
                ('telefono', models.CharField(max_length=200, verbose_name='Telefono')),
                ('direccion', models.CharField(max_length=200, verbose_name='Direccion')),
                ('usuario', models.CharField(max_length=200, verbose_name='Usuario')),
                ('contraseña', models.CharField(max_length=200, verbose_name='Contraseña')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'ordering': ['nombre'],
            },
        ),
    ]