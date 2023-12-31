# Generated by Django 5.0 on 2023-12-05 10:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Colaborador",
            fields=[
                (
                    "dni_cif_colaborador",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("fech_naci_colaborador", models.DateField()),
                ("nombre_colaborador", models.CharField(max_length=50)),
                ("apellidos_colaborador", models.CharField(max_length=100)),
                ("direccion_colaborador", models.CharField(max_length=50)),
                ("localidad_colaborador", models.CharField(max_length=50)),
                ("cpostal_colaborador", models.CharField(max_length=5)),
                ("provincia_colaborador", models.CharField(max_length=30)),
                ("telefono1_colaborador", models.CharField(max_length=15)),
                ("telefono2_colaborador", models.CharField(max_length=15)),
                ("email1_colaborador", models.CharField(max_length=100)),
                ("email2_colaborador", models.CharField(max_length=100)),
                ("cc_banc_colaborador", models.CharField(max_length=25)),
                ("es_recibir_revista_obs", models.CharField(max_length=50)),
                ("anios_premio", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Estacion",
            fields=[
                (
                    "ind_estacion",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("nom_estacion", models.CharField(max_length=50)),
                ("localidad_estacion", models.CharField(max_length=50)),
                ("provincia_estacion", models.CharField(max_length=30)),
                ("comarca_estacion", models.CharField(max_length=30)),
                (
                    "altitud_estacion",
                    models.DecimalField(decimal_places=2, max_digits=7),
                ),
                ("ubicacion_estacion", models.CharField(max_length=50)),
                ("es_activa_ubicacion", models.CharField(max_length=2)),
                ("fecha_alta_estaion", models.DateField()),
                ("fecha_baja_estaion", models.DateField()),
                ("fecha_ultima_revision", models.DateField()),
                ("cod_mod_auto_estacion", models.CharField(max_length=50)),
                ("longitud_estacion", models.CharField(max_length=50)),
                ("latitud_estacion", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Estacion_Colaborador",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha_alta_colaborador", models.DateField()),
                ("fecha_baja_colaborador", models.DateField()),
                ("modo_envio_datos", models.CharField(max_length=50)),
                ("es_cobrador", models.CharField(max_length=2)),
                ("es_ejerce", models.CharField(max_length=2)),
                ("es_clescom", models.CharField(max_length=2)),
                ("cod_categoria_est", models.CharField(max_length=50)),
                ("es_tiempo_real", models.CharField(max_length=2)),
                ("observ_colabo_est1", models.TextField()),
                ("observ_colabo_est", models.TextField()),
                (
                    "dni_cif_colaborador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="colabEstac.colaborador",
                    ),
                ),
                (
                    "ind_estacion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="colabEstac.estacion",
                    ),
                ),
            ],
        ),
    ]
