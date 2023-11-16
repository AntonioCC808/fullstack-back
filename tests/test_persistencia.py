"""Tests persistencia"""
import pathlib

from backend.persistencia import guardar_pedido


def test_persistencia():
    """Test persistencia microactividad"""
    pathlib.Path("../pedidos/").mkdir(exist_ok=True)
    with open("../pedidos/pedidos.txt", "w", encoding="utf-8") as file:
        file.write("")
    pedidos = [
        {"nombre": "Pedro", "apellidos": "Gil de Diego"},
        {"nombre": "Michael", "apellidos": "Jordan"}
    ]
    for pedido in pedidos:
        guardar_pedido(pedido["nombre"], pedido["apellidos"])


def test_guardar_pedido():
    """
    Prueba general
    """
    with open("../pedidos/pedidos.txt", "w+", encoding="utf-8") as file:
        guardar_pedido("Pedro", "Gil de Diego")
        guardar_pedido("Michael", "Jordan")
        firstline = file.readline()
        secondline = file.readline()
    assert firstline == "-Pedro Gil de Diego\n"
    assert secondline == "-Michael Jordan\n"
