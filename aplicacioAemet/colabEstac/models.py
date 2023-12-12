from django.db import models


# Create your models here.
class Colaborador(models.Model):
    dni_cif_colaborador = models.CharField(max_length=10, primary_key=True)
    fech_naci_colaborador = models.DateField(null=True, auto_now=False)
    nombre_colaborador = models.CharField(null=True, max_length=50)
    apellidos_colaborador = models.CharField(null=True, max_length=100)
    direccion_colaborador = models.CharField(null=True, max_length=50)
    localidad_colaborador = models.CharField(null=True, max_length=50)
    cpostal_colaborador = models.CharField(null=True, max_length=5)
    provincia_colaborador = models.CharField(null=True, max_length=30)
    telefono1_colaborador = models.CharField(null=True, max_length=15)
    telefono2_colaborador = models.CharField(null=True, max_length=15)
    email1_colaborador = models.CharField(null=True, max_length=100)
    email2_colaborador = models.CharField(null=True, max_length=100)
    cc_banc_colaborador = models.CharField(null=True, max_length=25)
    es_recibir_revista_obs = models.CharField(null=True, max_length=50)
    anios_premio = models.CharField(null=True, max_length=50)

    def __str__(self):
        return f"{self.nombre_colaborador} {self.apellidos_colaborador}"


class Estacion(models.Model):
    ind_estacion = models.CharField(max_length=50, primary_key=True)
    nom_estacion = models.CharField(max_length=50)
    localidad_estacion = models.CharField(max_length=50)
    provincia_estacion = models.CharField(max_length=30)
    comarca_estacion = models.CharField(max_length=30)
    altitud_estacion = models.DecimalField(max_digits=7, decimal_places=2)
    ubicacion_estacion = models.CharField(max_length=50)
    es_activa_ubicacion = models.CharField(max_length=2)
    fecha_alta_estaion = models.DateField(auto_now_add=False)
    fecha_baja_estaion = models.DateField(auto_now_add=False)
    fecha_ultima_revision = models.DateField(auto_now_add=False)
    cod_mod_auto_estacion = models.CharField(max_length=50)
    longitud_estacion = models.CharField(max_length=50)
    latitud_estacion = models.CharField(max_length=50)

    def __str__(self):
        return self.nom_estacion


class Estacion_Colaborador(models.Model):
    dni_cif_colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    ind_estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE)
    fecha_alta_colaborador = models.DateField(auto_now_add=False)
    fecha_baja_colaborador = models.DateField(auto_now_add=False)
    modo_envio_datos = models.CharField(max_length=50)
    es_cobrador = models.CharField(max_length=2)
    es_ejerce = models.CharField(max_length=2)
    es_clescom = models.CharField(max_length=2)
    cod_categoria_est = models.CharField(max_length=50)
    es_tiempo_real = models.CharField(max_length=2)
    observ_colabo_est1 = models.TextField()
    observ_colabo_est = models.TextField()

    def __str__(self):
        return f"{self.dni_cif_colaborador} - {self.ind_estacion}"
