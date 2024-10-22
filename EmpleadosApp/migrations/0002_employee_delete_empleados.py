# Generated by Django 5.1 on 2024-10-22 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmpleadosApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('departamento', models.CharField(max_length=100)),
                ('fecha_contratacion', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Empleados',
        ),
    ]