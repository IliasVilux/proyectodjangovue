from django.contrib import admin
from .models import Colaborador, Estacion, Estacion_Colaborador

# Register your models here.
admin.site.register(Colaborador)
admin.site.register(Estacion)
admin.site.register(Estacion_Colaborador)
