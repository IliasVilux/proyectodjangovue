import pytest
from colabEstac.models import Colaborador, Estacion, Estacion_Colaborador
from core.schema import schema
from graphene.test import Client

client = Client(schema)


@pytest.mark.django_db
def test_colaborador_create():
    mutation = """
        mutation{
            addColaborador(
                dniCifColaborador: "111",
                nombreColaborador: "test"
            ){
                colaborador{
                dniCifColaborador
                nombreColaborador
                }
            }
        }
    """

    result = client.execute(mutation)

    assert result == {
        "data": {
            "addColaborador": {
                "colaborador": {"dniCifColaborador": "111", "nombreColaborador": "test"}
            }
        }
    }
    assert "errors" not in result


@pytest.mark.django_db
def test_colaborador_get_by_dni():
    Colaborador.objects.create(dni_cif_colaborador="1", nombre_colaborador="Test")
    query = """
    {
        colaborador(dniCifColaborador: "1"){
            dniCifColaborador
            nombreColaborador
        }
    }
    """

    result = client.execute(query)
    assert result == {
        "data": {"colaborador": {"dniCifColaborador": "1", "nombreColaborador": "Test"}}
    }
    assert "errors" not in result


@pytest.mark.django_db
def test_colaborador_update():
    Colaborador.objects.create(dni_cif_colaborador="1", nombre_colaborador="Test")
    mutation = """
        mutation {
            updateColaborador(
                dniCifColaborador: "1",
                nombreColaborador: "Test Update"
            ) {
                colaborador {
                    dniCifColaborador
                    nombreColaborador
                }
            }
        }
    """

    result = client.execute(mutation)
    assert result == {
        "data": {
            "updateColaborador": {
                "colaborador": {
                    "dniCifColaborador": "1",
                    "nombreColaborador": "Test Update",
                }
            }
        }
    }
    assert "errors" not in result


@pytest.mark.django_db
def test_colaborador_delete():
    Colaborador.objects.create(dni_cif_colaborador="1", nombre_colaborador="Test")
    mutation = """
        mutation{
            deleteColaborador(dniCifColaborador: "1"){
                message
            }
        }
    """

    result = client.execute(mutation)
    assert result == {
        "data": {
            "deleteColaborador": {
                "message": "colaborador con dni 123 se ha eliminado correctamente."
            }
        }
    }
    assert "errors" not in result


# @pytest.mark.django_db
# def test_colaborador_model_exist():
#     colaboradores = Colaborador.objects.count()

#     assert colaboradores == 0

# def test_colaborador_has_string_representation():
#     colaborador = Colaborador(nombre_colaborador = "Ilias", apellidos_colaborador = "Otsman El Abbadi")

#     assert str(colaborador) == "Ilias Otsman El Abbadi"
