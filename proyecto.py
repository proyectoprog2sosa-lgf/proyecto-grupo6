
"""
Un Airbnb es:
{id: Datos}
{int: tuple}
id: es el numero que identifica al alquiler
Datos: es una tupla que contiene la informacion donde:
(nombre, host_id, host_profile_id, host_name, neighbourhood, latitud, longitud, room_type, minimun_nights, number_of_reviews, last_review, reviews_per_month, calculated_hots_listing_count, availability_356, number_of_reviews, license)
(string, int, int, string, string, float, float, string, int, int, string, float, int, int, int, string)
nombre: nombre del alojamiento
host_id: identificador por afiliado
host_name: nombre del anfitrion
neighbourhood: barrio donde se encuentra el alquiler
latitud: coordenada geografica
longitud: coordenada geografica
room_type: tipo de habitacion
minimun_nights: numero minimo de noches para alquilar
number_of_reviews: numero de reseñas
last_review: fecha de la ultima reseña
reviews_per_month: numero de reseñas por mes
calculated_hots_listing_count: numero de alojamientos que tiene el anfitrion
availability_356: disponibilidad durante el año
number_of_reviews: numero de reseñas
licencia: numero de licencia del alquiler (o string indicando que licencia tiene el alquiler)
"""
import streamlit as st
import csv

def manejar_archivo() -> dict:
    """
    manejar_archivo() -> dict[int, tuple]
    Lee el archivo CSV y construye un diccionario donde la clave es el id del alojamiento
    y el valor es una tupla con toda la información del Airbnb.
    """
    dicc = {}
    with open('listings-Buenos_Aires-12K.csv', encoding='utf-8') as listings:
        lector = csv.reader(listings)
        next(lector)
        for linea in lector:
            if linea:
                dicc[linea[0]] = tuple(linea)
    return dicc

def mayor(lista_de_mayores, nuevo, indice_menor, dataset):
    """
    mayor(list, int, int) --> list
    lista_de_mayores: es una lista con los numeros mas grandes recolectados
    nuevo: es el nuevo numero a verificar
    indice_menor: almacena el numero mas pequeño
    retorna una lista con o sin el numero nuevo dependiendo si entra o no
    """
    id_viejo = lista_de_mayores[indice_menor]
    
    if id_viejo == 0:
        lista_de_mayores[indice_menor] = nuevo
        return lista_de_mayores
        
    if dataset[nuevo][11] != '':
        val_nuevo = float(dataset[nuevo][11])
    else:
        val_nuevo = 0.0
        
    if dataset[id_viejo][11] != '':
        val_viejo = float(dataset[id_viejo][11])
    else:
        val_viejo = 0.0
    
    if val_viejo < val_nuevo:
        lista_de_mayores[indice_menor] = nuevo
        
    return lista_de_mayores

def menor(lista, dataset):
    """
    menor(list, dicc) -> int
    lista: representa una lista con 10 numeros enteros
    retorna el indice del numero mas bajo dentro de la lista
    """
    if 0 in lista:
        return lista.index(0)
        
    menor_indice = 0
    for i in range(len(lista)):
        if dataset[lista[i]][11] != '':
            val1 = float(dataset[lista[i]][11])
        else:
            val1 = 0.0
            
        if dataset[lista[menor_indice]][11] != '':
            val2 = float(dataset[lista[menor_indice]][11])
        else:
            val2 = 0.0
        
        if val1 < val2:
            menor_indice = i
            
    return menor_indice

def mayores10(listings) -> list:
    """
    """
    lista_mayores = [0,0,0,0,0,0,0,0,0,0]
    for id in listings:
        lista_mayores = mayor(lista_mayores, id, menor(lista_mayores, listings), listings)
        
    return lista_mayores

def alojamientos_mayor_reseñas(listings) -> list:
    """
    Devuelve una lista con información resumida de los 10 alojamientos
    """
    lista_alojamientos = [["Nombre", "Anfitrion", "Barrio", "Reseñas"]]
    top10 = mayores10(listings)
    
    for ids in top10:
        if ids != 0:
            lista_alojamientos.append([listings[ids][1], listings[ids][3], listings[ids][4], listings[ids][11]])
            
    return lista_alojamientos

def mostrar_tabla(listings):
    """
    mostrar_tabla(listings: dict[int, tuple]) -> None
    Muestra la tabla en Streamlit con los resultados.
    """
    st.table(alojamientos_mayor_reseñas(listings))

def main():
    st.title('¿Cuales son los alojamientos con mayor cantidad de reseñas?')
    mostrar_tabla(manejar_archivo())

main()