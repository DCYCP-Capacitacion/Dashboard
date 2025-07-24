import streamlit as st

# Título del dashboard
st.title("Mi primer Dashboard con Streamlit")

# Subtítulo
st.subheader("Hola Carlitos")

# Texto
st.write("¡Hola! Este es tu primer dashboard conectado con GitHub.")

# Entrada de usuario
nombre = st.text_input("Te gustaria saber quien soy?")

# Mostrar resultado si se escribe un nombre
if nombre:
    st.success(f"¡Bienvenido/a, {nombre}!")
