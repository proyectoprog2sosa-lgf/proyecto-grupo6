import streamlit as st

st.title('Proyecto Grupal de Programacion')
st.write('Empecemos a trabajar equipo!')


propiedades = {
    "id": ("nombre", "host_id", "host_profile_id", "host_name", "neighbourhood", "latitud", "longitud", "room_type", "minimun_nights", "number_of_reviews", "last_review", "reviews_per_month", "calculated_hots_listing_count", "availability_356", "number_of_reviews", "licencia")
}
"""
Un Airbnb es:
{id: Datos}
{int: tuple}
id: es el complejo numero que identifica al alquiler
Datos: es una tupla que contiene la informacion donde:
(nombre, host_id, host_profile_id, host_name, neighbourhood, latitud, longitud, room_type, minimun_nights, number_of_reviews, last_review, reviews_per_month, calculated_hots_listing_count, availability_356, number_of_reviews, licencia)
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
def mas_disponibilidad_anual (datos):
    
