"""TEST-API"""

from microactividad_tests import api


def test_obtener_primer_elemento():
    """
    Test the function obtener_primer_elemento in the api module.

    The function should return the first element of the provided list.
    """
    lista = ["master", "full", "stack"]
    elemento = api.obtener_primer_elemento(lista)
    assert elemento == "master"


def test_inserta_elemento_al_final():
    """
    Test the function inserta_elemento_al_final in the api module.

    The function should insert the given element at the end of the provided list.
    """
    lista = ["master", "full", "stack"]
    api.inserta_elemento_al_final(lista, "hola")
    assert len(lista) == 4
    assert lista[-1] == "hola"


def test_inserta_elemento_al_principio():
    """
    Test the function inserta_elemento_al_principio in the api module.

    The function should insert the given element at the beginning of the provided list.
    """
    lista = ["master", "full", "stack"]
    api.inserta_elemento_al_principio(lista, "hola")
    assert len(lista) == 4
    assert lista[0] == "hola"


def test_borra_lista():
    """
    Test the function borra_lista in the api module.

    The function should remove all elements from the provided list, making it empty.
    """
    lista = ["master", "full", "stack"]
    api.borra_lista(lista)
    assert len(lista) == 0
