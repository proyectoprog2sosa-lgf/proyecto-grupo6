lista_m = [0,0,0,0,0,0,0,0,0]
def menor (lista):
    """
    menor(list) -> int
    lista: representa una lista con 10 numeros enteros
    retorna el indice del numero mas bajo dentro de la lista
    """
    menor_indice = 0
    for i in range(len(lista_m)):
        if lista[menor_indice] > lista[i]:
            menor_indice = i
    return menor_indice
def mayor (lista_de_mayores,nuevo,indice_menor):
    """
    mayor(list, int, int) --> list
    lista_de_mayores: es una lista con los numeros mas grandes recolectados
    nuevo: es el nuevo numero a verificar
    indice_menor: almacena el numero mas pequeño
    retorna una lista con o sin el numero nuevo dependiendo si entra o no
    """
    if lista_de_mayores[indice_menor] < nuevo:
        lista_de_mayores[indice_menor] = nuevo
    return lista_de_mayores
def acomodar (lista,nuevo):
    """
    funcion de prueba 
    """
    x = mayor(lista,nuevo,menor(lista))
    print(x)
acomodar(lista_m,6)
