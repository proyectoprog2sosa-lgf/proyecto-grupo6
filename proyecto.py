"""
Un Airbnb es:
{id: Datos}
{int: tuple}
id: es el numero que identifica al alquiler
Datos: es una tupla que contiene la informacion  del airbnb donde:
(nombre, host_id, host_profile_id, host_name, neighbourhood_group, neighbourhood, latitude, longitude, room_type, price, minimun_nights, number_of_reviews, last_review, reviews_per_month, calculated_hots_listing_count, availability_356, number_of_reviews, license)
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
import matplotlib.pyplot as plt
import csv

def manejar_archivo():
    """
    manejar_archivo() -> dict[int, tuple]
    Lee el archivo CSV y construye un diccionario donde la clave es el id del alojamiento
    y el valor es una tupla con toda la información del Airbnb.
    """
    dicc = {}
    with open('listings-Buenos_Aires-12K.csv') as listings:
        lector = csv.reader(listings)
        next(lector)
        for linea in lector:
            datos = linea
            dicc[datos[0]] = (datos[1],datos[2],datos[3],datos[4],datos[5],datos[6],datos[7],datos[8],datos[9],datos[10],datos[11],datos[12],datos[13],datos[14],datos[15],datos[16],datos[17],datos[18])
    return dicc


def mayor(lista_de_mayores, nuevo, indice_menor, dataset, indice_columna=11):
    """
    mayor: list(int) int int Airbnb int --> list(int)
    lista_de_mayores: es una lista con los numeros mas grandes recolectados
    nuevo: es el nuevo numero a verificar
    indice_menor: almacena el numero mas pequeño
    Retorna una lista con o sin el numero nuevo dependiendo si entra o no
    """
    id_viejo = lista_de_mayores[indice_menor]
    
    if id_viejo == 0:
        lista_de_mayores[indice_menor] = nuevo
        return lista_de_mayores
        
    if dataset[nuevo][indice_columna] != '':
        val_nuevo = float(dataset[nuevo][indice_columna])
    else:
        val_nuevo = 0.0
        
    if dataset[id_viejo][indice_columna] != '':
        val_viejo = float(dataset[id_viejo][indice_columna])
    else:
        val_viejo = 0.0
    
    if val_viejo < val_nuevo:
        lista_de_mayores[indice_menor] = nuevo
        
    return lista_de_mayores

def menor(lista, dataset, indice_columna=11):
    """
    menor: List[Int] Airbnb Int -> Int
    lista: representa una lista con 10 numeros enteros
    retorna el indice del numero mas bajo dentro de la lista
    """
    if 0 in lista:
        return lista.index(0)
        
    menor_indice = 0
    for i in range(len(lista)):
        if dataset[lista[i]][indice_columna] != '':
            val1 = float(dataset[lista[i]][indice_columna])
        else:
            val1 = 0.0
            
        if dataset[lista[menor_indice]][indice_columna] != '':
            val2 = float(dataset[lista[menor_indice]][indice_columna])
        else:
            val2 = 0.0
        
        if val1 < val2:
            menor_indice = i
            
    return menor_indice

def mayores10(listings):
    """
    mayores10: Airbnb -> list
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
            lista_alojamientos.append([listings[ids][0], listings[ids][3], listings[ids][5], listings[ids][11]])
            
    return lista_alojamientos

def mostrar_tabla(listings):
    """
    mostrar_tabla(listings: dict[int, tuple]) -> None
    Muestra la tabla en Streamlit con los resultados.
    """
    st.table(alojamientos_mayor_reseñas(listings))

# Cuales alojamientos se pueden reservar por un minimo de X noches?

def alojamientos_minimo_noches(minimo: int,listings) -> list[tuple[float,float]]:
    '''
    alojamientos_minimo_nnoches: Int Airbnb -> List[(float,float)]
    Dado un numero minimo devuelve la lista de las coordenadas de los alojamientos que pueden
    reservar por el minimo dado.
    '''
    lista_coordenadas = []
    for ids,datos in listings.items():
        if datos[10] != '' and float(datos[10]) <= minimo:
            lista_coordenadas += [(float(datos[6]),float(datos[7]))]
    return lista_coordenadas

def mostrar_mapa(minimo: int,listings):
    '''
    motrar_mapa: Int Airbnb -> None
    Muestra el mapa en streamlit con los resultados.
    '''
    dicc = {}
    lista_latitudes = []
    lista_longitudes = []
    for tupla in alojamientos_minimo_noches(minimo,listings):
        latitud, longitud = tupla
        lista_latitudes.append(latitud)
        lista_longitudes.append(longitud)
    dicc['Latitud'] = lista_latitudes
    dicc['Longitud'] = lista_longitudes
    st.map(dicc,latitude= 'Latitud',longitude= 'Longitud')

# Cuantos alojamientos hay por barrio?

def contar_aloj_barrio(listings) -> dict[str,int]:
    '''
    contar_aloj_barrio: Airbnb -> dict[str,int]
    Dado el dataset leido, devuelve un diccionario donde las claves son los barrios y los valores son la cantidad de alojamientos que se encuentran en ese barrio.
    '''
    dicc = {}
    for ids,datos in listings.items():
        barrio = datos[5]
        if barrio not in dicc:
            dicc[barrio] = 1
        else:
            dicc[barrio] += 1 
    return dicc

def mostrar_grafico(listings):
    '''
    mostrar_grafico: Airbnb -> None     
    Dado el dataset con los airbnb crea el grafico de barras horizontal con la cantidad de alojamientos por barrio.
    '''
    aloj_por_barrio = contar_aloj_barrio(listings)
    plt.barh(aloj_por_barrio.keys(),aloj_por_barrio.values(),color='blue')
    plt.xlabel('Cantidad de Alojamientos')
    plt.ylabel('Barrios')
    plt.tick_params(axis= 'y', labelsize= 7)
    plt.tight_layout()

# Buscar alojamientos por nombre.

def buscar_alojamiento(nombre, listings):
    resultado = [["Nombre", "Anfitrión", "Barrio", "Reseñas"]]
    for ids, datos in listings.items():
        if nombre.lower() in datos[0].lower():
           resultado.append([datos[0], datos[3], datos[5], datos[11]])
    return resultado

def mostrar_busqueda(listings):
    nombre = st.text_input("Ingrese el nombre del alojamiento:")
    if nombre != "":
        resultado = buscar_alojamiento(nombre, listings)
        if resultado != [["Nombre", "Anfitrión", "Barrio", "Reseñas"]]:
            st.table(resultado)
        else:
            st.write("No se encontraron alojamientos.")

# Cuales fueron los aljomaientos con mas reservas en el ultimo año?



def alojamientos_mas_reservas(listings) -> list:
    """
    alojamientos_mas_reservas: Airbnb -> list
    Devuelve una lista cbon los ids de los alojamientos que han tenido mas reservas.
    """
    lista_mayores = [0,0,0,0,0,0,0,0,0,0]
    
    for id in listings:
        indice_del_menor = menor(lista_mayores, listings, indice_columna=16)
        lista_mayores = mayor(lista_mayores, id, indice_del_menor, listings, indice_columna=16)
        
    lista_alojamientos = [["Nombre", "Anfitrion", "Barrio", "Reservas (Ultimo Anio)"]]
    
    for ids in lista_mayores:
        if ids != 0:
            lista_alojamientos.append([listings[ids][0], listings[ids][3], listings[ids][5], listings[ids][16]])
            
    return lista_alojamientos

def mostrar_tabla_reservas(listings):
    """
    mostrar_tabla_reservas(listings: dict[int, tuple]) -> None
    Muestra la tabla en streamlit con los resultados
    """
    st.table(alojamientos_mas_reservas(listings))

def main():
    listings = manejar_archivo()

    tab1, tab2, tab3, tab4, tab5 = st.tabs(['Mas reservas','Minimo de dias para reservar','Alojamientos por barrio', 'Buscar alojamientos', 'Reservas Último Año'])
    with tab1:
        st.title('¿Cuales son los alojamientos con mayor cantidad de reseñas?')
        mostrar_tabla(listings)
    with tab2:
        minimo = st.select_slider("Elija un minimo de dias para reservar el alojamiento:",options= [x for x in range(1,365)])
        mostrar_mapa(minimo, listings)
    with tab3:
        st.title('¿Cuantos alojamientos hay por barrio?')
        mostrar_grafico(listings)
        st.pyplot(plt)
    with tab4:
        st.title('Buscar alojamiento por nombre')
        mostrar_busqueda(listings)
    with tab5:
        st.title('¿Cuales son los alojamientos con más reservas en el último año?')
        mostrar_tabla_reservas(listings)

main()