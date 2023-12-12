import graphene
from graphene_django import DjangoObjectType
from colabEstac.models import Colaborador


class ColaboradorType(DjangoObjectType):
    class Meta:
        model = Colaborador


class AddColaborador(graphene.Mutation):
    colaborador = graphene.Field(ColaboradorType)

    class Arguments:
        dni_cif_colaborador = graphene.String(required=True)
        fech_naci_colaborador = graphene.Date()
        nombre_colaborador = graphene.String(required=True)
        apellidos_colaborador = graphene.String(default_value=None)
        direccion_colaborador = graphene.String(default_value=None)
        localidad_colaborador = graphene.String(default_value=None)
        cpostal_colaborador = graphene.String(default_value=None)
        provincia_colaborador = graphene.String(default_value=None)
        telefono1_colaborador = graphene.String(default_value=None)
        telefono2_colaborador = graphene.String(default_value=None)
        email1_colaborador = graphene.String(default_value=None)
        email2_colaborador = graphene.String(default_value=None)
        cc_banc_colaborador = graphene.String(default_value=None)
        es_recibir_revista_obs = graphene.String(default_value=None)
        anios_premio = graphene.String(default_value=None)

    def mutate(self, info, dni_cif_colaborador, nombre_colaborador, **kwargs):
        newColaborador = Colaborador(
            dni_cif_colaborador=dni_cif_colaborador,
            nombre_colaborador=nombre_colaborador,
            **kwargs,
        )
        newColaborador.save()

        return AddColaborador(colaborador=newColaborador)


class UpdateColaborador(graphene.Mutation):
    colaborador = graphene.Field(ColaboradorType)

    class Arguments:
        dni_cif_colaborador = graphene.String(required=True)
        fech_naci_colaborador = graphene.Date()
        nombre_colaborador = graphene.String()
        apellidos_colaborador = graphene.String()
        direccion_colaborador = graphene.String()
        localidad_colaborador = graphene.String()
        cpostal_colaborador = graphene.String()
        provincia_colaborador = graphene.String()
        telefono1_colaborador = graphene.String()
        telefono2_colaborador = graphene.String()
        email1_colaborador = graphene.String()
        email2_colaborador = graphene.String()
        cc_banc_colaborador = graphene.String()
        es_recibir_revista_obs = graphene.String()
        anios_premio = graphene.String()

    def mutate(self, info, dni_cif_colaborador, **kwargs):
        updateColaborador = Colaborador.objects.get(pk=dni_cif_colaborador)

        for field, value in kwargs.items():
            setattr(updateColaborador, field, value)

        updateColaborador.save()
        return UpdateColaborador(colaborador=updateColaborador)


class DeleteColaborador(graphene.Mutation):
    message = graphene.String()

    class Arguments:
        dni_cif_colaborador = graphene.String(required=True)

    def mutate(self, info, dni_cif_colaborador):
        delColaborador = Colaborador.objects.get(pk=dni_cif_colaborador)
        delColaborador.delete()
        return DeleteColaborador(
            message=f"colaborador con dni {dni_cif_colaborador} se ha eliminado correctamente."
        )


class Query(graphene.ObjectType):
    colaboradores = graphene.List(ColaboradorType)
    colaborador = graphene.Field(ColaboradorType, dni_cif_colaborador=graphene.String())

    def resolve_colaboradores(self, info):
        return Colaborador.objects.all()

    def resolve_colaborador(self, info, dni_cif_colaborador):
        return Colaborador.objects.get(pk=dni_cif_colaborador)


class Mutation(graphene.ObjectType):
    add_colaborador = AddColaborador.Field()
    update_colaborador = UpdateColaborador.Field()
    delete_colaborador = DeleteColaborador.Field()
