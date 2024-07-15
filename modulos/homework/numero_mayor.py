
def es_mayor(lista):
    """funcion para saber el numero menor de la lista"""
    mayor=lista[0]
    for n in lista:
        if n < mayor:
            mayor=n
    return mayor