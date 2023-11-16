from typing import List, Any

def obtener_primer_elemento(lista: List[Any]) -> Any:
    """
    Obtiene el primer elemento de la lista.

    Parameters
    ----------
    lista : list
        La lista de la cual se desea obtener el primer elemento.

    Returns
    -------
    Any
        El primer elemento de la lista.
    """
    return lista[0]

def inserta_elemento_al_final(lista: List[Any], elemento: Any) -> None:
    """
    Inserta un elemento al final de la lista.

    Parameters
    ----------
    lista : list
        La lista a la cual se desea agregar el elemento.
    elemento : Any
        El elemento que se va a agregar al final de la lista.

    Returns
    -------
    None
    """
    lista.append(elemento)

def inserta_elemento_al_principio(lista: List[Any], elemento: Any) -> None:
    """
    Inserta un elemento al principio de la lista.

    Parameters
    ----------
    lista : list
        La lista a la cual se desea agregar el elemento.
    elemento : Any
        El elemento que se va a agregar al principio de la lista.

    Returns
    -------
    None
    """
    lista.insert(0, elemento)

def borra_lista(lista: List[Any]) -> None:
    """
    Borra todos los elementos de la lista, dejándola vacía.

    Parameters
    ----------
    lista : list
        La lista que se desea borrar.

    Returns
    -------
    None
    """
    lista.clear()
