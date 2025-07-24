import streamlit as st
import pandas as pd
import plotly as px
from datetime import datetime

# Simulación de datos
data = {
    "curso": [
        "Primeros auxilios", "Uso de herramientas", "Covid UR", "Unificación de criterios",
        "Protección personal", "Primeros auxilios 2"
    ],
    "categoria": [
        "INDEC-INAP", "INDEC-INAP", "INDEC Universidad", "INDEC Universidad",
        "Capacitación Técnico-Profesional", "INDEC-INAP"
    ],
    "fecha": pd.to_datetime([
        "2021-12-10", "2022-01-15", "2022-03-20", "2022-05-15", "2022-09-01", "2023-03-15"
    ]),
    "inscriptos": [100, 150, 300, 200, 100, 120],
    "aprobados": [60, 75, 140, 120, 80, 70]
}
df = pd.DataFrame(data)

# Sidebar filtros
st.sidebar.title("Filtros")
categorias = st.sidebar.multiselect("Categorías", df["categoria"].unique(), default=df["categoria"].unique())
rango_fechas = st.sidebar.date_input("Período de visualización", [df["fecha"].min(), df["fecha"].max()])

# Filtrado de datos
df_filtrado = df[
    (df["categoria"].isin(categorias)) &
    (df["fecha"] >= pd.to_datetime(rango_fechas[0])) &
    (df["fecha"] <= pd.to_datetime(rango_fechas[1]))
]

# KPIs
cursos_dictados = df_filtrado["curso"].nunique()
total_inscriptos = df_filtrado["inscriptos"].sum()
total_aprobados = df_filtrado["aprobados"].sum()
porcentaje_aprobados = (total_aprobados / total_inscriptos) * 100 if total_inscriptos else 0

st.title("Cursos Capacitación y Carrera del Personal")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Cursos dictados", cursos_dictados)
col2.metric("Cantidad de inscriptos", total_inscriptos)
col3.metric("Cantidad de aprobados", total_aprobados)
col4.metric("% Aprobados", f"{porcentaje_aprobados:.1f}%")

# Lista de cursos dictados
st.subheader("Cursos dictados")
st.write(df_filtrado["curso"].unique())

# Gráfico de barras: cantidad de cursos por mes
df_filtrado["mes"] = df_filtrado["fecha"].dt.to_period("M").dt.to_timestamp()
cursos_por_mes = df_filtrado.groupby("mes").size().reset_index(name="cursos")

fig = px.bar(cursos_por_mes, x="mes", y="cursos", title="Cantidad de cursos dictados por mes")
st.plotly_chart(fig)
