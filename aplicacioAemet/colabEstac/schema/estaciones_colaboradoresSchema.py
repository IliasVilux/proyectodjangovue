import graphene
from graphene_django import DjangoObjectType
from colabEstac.models import Estacion_Colaborador


class Estacion_ColaboradorType(DjangoObjectType):
    class Meta:
        model = Estacion_Colaborador
        fields = "__all__"


class Query(graphene.ObjectType):
    estaciones_colaboradores = graphene.List(Estacion_ColaboradorType)
    estacion_colaborador = graphene.Field(
        Estacion_ColaboradorType,
    )

    def resolve_colaboradores(self):
        return Estacion_Colaborador.objects.all()
