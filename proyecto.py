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

# Cuales son los 10 alojamientos con mayor disponibilidad anual?


import csv

def manejar_archivo() -> dict:
    dicc = {}
    with open('listings-Buenos_Aires-12K.csv') as listings:
        lector = csv.reader(listings)
        next(lector)
        for linea in lector:
            datos = linea
            dicc[datos[0]] = (datos[1],datos[2],datos[3],datos[4],datos[5],datos[6],datos[7],datos[8],datos[9],datos[10],datos[11],datos[12],datos[13],datos[14],datos[15],datos[16],datos[17],datos[18])
    return dicc


def mayor(lista: list[tuple]) -> tuple:
    '''
    Dada una lista de tuplas  de numeros, devuelve la tupla con el mayor en el segundo elemento de ellos.\n
    mayor([1,2,3]) = 3  
    mayor([]) = 0
    '''
    mayor = lista[0]
    for t in lista:
        if t[1] > mayor[1]:
            mayor = t
    return mayor

def disponibilidades_anuales(listings: dict[int,tuple]) -> list[tuple]:
    lista_disponibilidad = []
    for ids, datos in listings.items():
        lista_disponibilidad += [(ids,int(datos[15]))]
    return lista_disponibilidad

def mayores10(listings) -> list[tuple]:
    lista_disponibilidad = disponibilidades_anuales(listings)
    lista_mayores = []
    for i in range(10):
        t_mayor = mayor(lista_disponibilidad)
        lista_mayores.append(t_mayor)
        lista_disponibilidad.remove(t_mayor)
    return lista_mayores
def test_mayores10():
    assert mayores10([1,2,3,4,5,6,7,8,9,10,11,12,13]) == [13,12,11,10,9,8,7,6,5,4]
    assert mayores10([123,56,114]) == [123,114,56,0,0,0,0,0,0,0]

def alojamientos_mayor_disp(listings) -> list:
    lista_alojamientos = []
    for ids, disponibilidad in mayores10(listings):
        lista_alojamientos.append([listings[ids][0],listings[ids][3],listings[ids][5],listings[ids][8],listings[ids][15]])
    return lista_alojamientos

def mostrar_tabla(listings):
    st.table(alojamientos_mayor_disp(listings),width= 'content')

def main():
    st.title('¿Cuales son los alojamientos con mayor disponibilidad anual?')
    mostrar_tabla(manejar_archivo())

main()

