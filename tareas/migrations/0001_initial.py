# Generated by Django 4.2.4 on 2023-08-05 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registroTareas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_tarea', models.CharField(max_length=3, unique=True)),
                ('titulo_tarea', models.CharField(max_length=50)),
                ('descripcion_tarea', models.CharField(max_length=150)),
                ('fvencimiento_tarea', models.DateField()),
                ('categoria_tarea', models.CharField(choices=[('1', 'Trabajo'), ('2', 'Hogar'), ('3', 'Estudio'), ('4', 'Otras categorías')], default='1', max_length=1)),
                ('estado_tarea', models.CharField(choices=[('1', 'Pendiente'), ('2', 'En progreso'), ('3', 'Completada')], default='1', max_length=1)),
            ],
        ),
    ]
