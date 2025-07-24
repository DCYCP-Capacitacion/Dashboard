import streamlit as st

# Título del dashboard
st.title("Mi primer Dashboard con Streamlit")

# Subtítulo
st.subheader("Este es un ejemplo básico")

# Texto
st.write("¡Hola! Este es tu primer dashboard conectado con GitHub.")

# Entrada de usuario
nombre = st.text_input("¿Cómo te llamás?")

# Mostrar resultado si se escribe un nombre
if nombre:
    st.success(f"¡Bienvenido/a, {nombre}!")
