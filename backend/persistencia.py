"""Persistencia"""


def guardar_pedido(nombre: str, apellidos: str) -> None:
    """
    Save a customer order in the "pedidos.txt" file.

    Parameters
    ----------
    nombre : str
        The customer's first name.
    apellidos : str
        The customer's last name.

    Returns
    -------
    None
    """
    with open("../pedidos/pedidos.txt", "a", encoding="utf-8") as file:
        file.write(f"-{nombre} {apellidos}\n")
