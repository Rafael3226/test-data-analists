

import config
import importlib
assert config

"""
  Este módulo implementa el tipo abstracto de datos
  (TAD) Map sin orden. Se puede implementar sobre una estructura
  de datos Hash Table, con resolución de colisiones: Linear Probing
  o separate chaining
"""


def newMap(numelements=17,
           prime=109345121,
           maptype='CHAINING',
           loadfactor=0.5,
           cmpfunction=None):
    """Crea una tabla de símbolos (map) sin orden

    Args:
        numelements: Tamaño inicial de la tabla
        prime: Número primo utilizado en la función MAD
        maptype: separate chaining ('CHAINING' ) o linear probing('PROBING')
        loadfactor: Factor de carga inicial de la tabla
        cmpfunction: Función de comparación entre llaves
    Returns:
        Un nuevo map
    Raises:
        Exception
    """
    ht = mapSelector(maptype)
    return ht.newMap(numelements,
                     prime,
                     loadfactor,
                     cmpfunction,
                     ht)


def put(map, key, value):
    """ Ingresa una pareja llave,valor a la tabla de hash.
    Si la llave ya existe en la tabla, se reemplaza el valor

    Args:
        map: El map a donde se guarda la pareja
        key: la llave asociada a la pareja
        value: el valor asociado a la pareja
    Returns:
        El map
    Raises:
        Exception
    """
    return map['datastructure'].put(map, key, value)


def get(map, key):
    """ Retorna la pareja llave, valor, cuya llave sea igual a key
    Args:
        map: El map a donde se guarda la pareja
        key: la llave asociada a la pareja

    Returns:
        Una pareja <llave,valor>
    Raises:
        Exception
    """
    return map['datastructure'].get(map, key)


def remove(map, key):
    """ Elimina la pareja llave,valor, donde llave == key.
    Args:
        map: El map a donde se guarda la pareja
        key: la llave asociada a la pareja

    Returns:
        El map
    Raises:
        Exception
    """
    return map['datastructure'].remove(map, key)


def contains(map, key):
    """ Retorna True si la llave key se encuentra en el map
        o False en caso contrario.
    Args:
        map: El map a donde se guarda la pareja
        key: la llave asociada a la pareja

    Returns:
        True / False
    Raises:
        Exception
    """
    return map['datastructure'].contains(map, key)


def size(map):
    """  Retorna  el número de entradas en la tabla de hash.
    Args:
        map: El map
    Returns:
        Tamaño del map
    Raises:
        Exception
    """
    return map['datastructure'].size(map)


def isEmpty(map):
    """ Informa si la tabla de hash se encuentra vacía
    Args:
        map: El map
    Returns:
        True: El map esta vacío
        False: El map no esta vacío
    Raises:
        Exception
    """
    return map['datastructure'].isEmpty(map)


def keySet(map):
    """
    Retorna una lista con todas las llaves de la tabla de hash

    Args:
        map: El map
    Returns:
        lista de llaves
    Raises:
        Exception
    """
    return map['datastructure'].keySet(map)


def valueSet(map):
    """
    Retorna una lista con todos los valores de la tabla de hash

    Args:
        map: El map
    Returns:
        lista de valores
    Raises:
        Exception
    """
    return map['datastructure'].valueSet(map)


"""
Selector dinámico de la estructura de datos solicitada
"""

switch_module = {
    "CHAINING": ".chaininghashtable",
    "PROBING": ".probehashtable",
}


def mapSelector(datastructure):
    """
    Carga dinámicamente el import de la estructura de datos
    seleccionada
    """
    ds = switch_module.get(datastructure)

    if ds is None:
        raise Exception(
            f"Tipo de estructura de datos no soportada. Solo se soportan: {', '.join(switch_module.keys())}"
        )

    module = importlib.import_module(ds, package="DISClib.DataStructures")
    return module
