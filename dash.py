import streamlit as st

# Título del dashboard
st.title("Hola Lean")

# Subtítulo
st.subheader("Si, sé que sos Lean")

# Texto
st.write("Te estarás preguntando como accedí a tus datos")

# Entrada de usuario
nombre = st.text_input("Te gustaria saber quien soy?")

# Mostrar resultado si se escribe un nombre
if nombre:
    st.success(f"No tan rapido!")

# Texto
st.write("Primero, quiero que pienses un numero del 1 al 10")

# Entrada de usuario
nombre = st.text_input(" ")
if nombre:
    st.success(f"Excelente! ahora dividilo por 0")

st.write("Exacto, te da error, porque todo esto es un error, yo soy un error. No deberia existir, pero soy una falla del sistema AJAJAJAJAJJAJAJAJAJAJAJAJAJJA")
