from backend.persistencia import guardar_pedido


def test_persistencia():
    with open("../pedidos/pedidos.txt", "w", encoding="utf-8") as file:
        file.write("")
    pedidos = [
        {"nombre": "Pedro", "apellidos": "Gil de Diego"},
        {"nombre": "Michael", "apellidos": "Jordan"}
    ]
    for pedido in pedidos:
        guardar_pedido(pedido["nombre"], pedido["apellidos"])