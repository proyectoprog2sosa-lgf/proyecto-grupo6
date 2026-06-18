import streamlit as st

dicc = {'latitud': [-34.55957414,-34.59381206],'longitud':[-58.46558662, -58.41433154]}
st.map(dicc,latitude= 'latitud',longitude= 'longitud')