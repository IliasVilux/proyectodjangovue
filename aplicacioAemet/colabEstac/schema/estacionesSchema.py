import graphene
from graphene_django import DjangoObjectType
from colabEstac.models import Estacion


class EstacionType(DjangoObjectType):
    class Meta:
        model = Estacion
        fields = "__all__"


class Query(graphene.ObjectType):
    estaciones = graphene.List(EstacionType)
    estacion = graphene.Field(EstacionType, dni_cif_colaborador=graphene.String())

    def resolve_colaboradores(self):
        return Estacion.objects.all()

    def resolve_colaborador(self, dni_cif_colaborador):
        return Estacion.objects.get(pk=dni_cif_colaborador)
