lista_m = [0,0,0,0,0,0,0,0,0]
def menor (lista):
    menor_indice = 0
    for i in range(len(lista_m)):
        if lista[menor_indice] > lista[i]:
            menor_indice = i
    return menor_indice
def mayor (lista_de_mayores,nuevo,indice_menor):
    if lista_de_mayores[indice_menor] < nuevo:
        lista_de_mayores[indice_menor] = nuevo
    return lista_de_mayores
def acomodar (lista,nuevo):
    x = mayor(lista,nuevo,menor(lista))
    print(x)
acomodar(lista_m,6)
