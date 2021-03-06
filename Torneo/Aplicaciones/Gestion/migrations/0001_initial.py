# Generated by Django 3.1.2 on 2021-01-09 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id_equipo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_equipo', models.CharField(max_length=11)),
                ('estadio', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id_jugador', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=11)),
                ('apellido', models.CharField(max_length=11)),
                ('goles', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Torneo',
            fields=[
                ('Torneo_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_torneo', models.CharField(max_length=11)),
                ('equipos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('nombre_usuario', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('contrasenia', models.CharField(max_length=11)),
                ('torneos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.torneo')),
            ],
        ),
        migrations.AddField(
            model_name='equipo',
            name='jugadores',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.jugador'),
        ),
    ]
