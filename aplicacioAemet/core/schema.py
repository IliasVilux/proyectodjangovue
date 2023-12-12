import graphene
from colabEstac.schema.colaboradoresSchema import (
    Query as queryColaboradores,
    Mutation as mutationColaboradores,
)
from colabEstac.schema.estacionesSchema import Query as queryEstaciones
from colabEstac.schema.estaciones_colaboradoresSchema import (
    Query as queryEstacionesColaboradores,
)


class Query(
    queryColaboradores,
    queryEstaciones,
    queryEstacionesColaboradores,
    graphene.ObjectType,
):
    def query(self):
        return ""


class Mutation(mutationColaboradores, graphene.Mutation):
    def mutate(self):
        return ""


schema = graphene.Schema(query=Query, mutation=Mutation)
