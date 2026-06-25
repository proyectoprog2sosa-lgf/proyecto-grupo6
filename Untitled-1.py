import streamlit as st
minimo = st.slider(
    "Elija la cantidad mínima de noches",
    min_value=1,
    max_value=165,
    value=1
)

st.write("Cantidad seleccionada:", minimo)
