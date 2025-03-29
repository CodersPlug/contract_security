import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración inicial de la página
st.set_page_config(page_title="Tablero Gestión de Incidentes", layout="wide", page_icon=":bar_chart:")

# Sección: Dashboard
st.title("Tablero de Gestión de Casos")
st.markdown("Indicadores clave para el seguimiento de obras")

# Add visual separator after header
st.markdown("---")

# Add three cards for metrics using Streamlit's native components
col_card1, col_card2, col_card3 = st.columns(3)

with col_card1:
    st.metric(
        label="Cantidad de Visitas",
        value="256",
        delta=None
    )

with col_card2:
    st.metric(
        label="Cantidad de Obras",
        value="48",
        delta=None
    )

with col_card3:
    st.metric(
        label="Visitas / Obras",
        value="5.3",
        delta="+12%",
        delta_color="normal"
    )

# Add visual separator after cards
st.markdown("---")

# Create two columns for the bar charts with spacing
col1, spacing, col2 = st.columns([1, 0.1, 1])

# Gráfico de barras: Casos por Mes (datos de ejemplo)
with col1:
    datos_mensuales = pd.DataFrame({
        "Mes": ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"],
        "Casos": [10, 12, 8, 15, 9, 11, 7, 13, 14, 10, 12, 9]
    })
    fig_bar = px.bar(datos_mensuales, x="Mes", y="Casos", title="Casos por Mes",
                     labels={"Casos": "Cantidad de Casos"},
                     color_discrete_sequence=['#2E86C1'])  # Blue color
    st.plotly_chart(fig_bar, use_container_width=True)

# Gráfico de barras: Accidentes por Mes (datos de ejemplo)
with col2:
    datos_accidentes = pd.DataFrame({
        "Mes": ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"],
        "Accidentes": [8, 15, 10, 12, 7, 9, 11, 14, 13, 8, 10, 12]
    })
    fig_bar2 = px.bar(datos_accidentes, x="Mes", y="Accidentes", title="Accidentes por Mes",
                      labels={"Accidentes": "Cantidad de Accidentes"},
                      color_discrete_sequence=['#E74C3C'])  # Red color
    st.plotly_chart(fig_bar2, use_container_width=True)

# Create two columns for the pie charts with spacing
col3, spacing2, col4 = st.columns([1, 0.1, 1])

# Gráfico de pastel: Distribución de Casos por Tipo
with col3:
    datos_tipo = pd.DataFrame({
        "Tipo": ["Seguridad", "Calidad", "Ambiente", "Otros"],
        "Cantidad": [50, 30, 25, 19]
    })
    fig_pie = px.pie(datos_tipo, names="Tipo", values="Cantidad", 
                     title="Tipos de Caso",
                     color_discrete_sequence=['#2E86C1', '#3498DB', '#5DADE2', '#85C1E9'])  # Blue color palette
    st.plotly_chart(fig_pie, use_container_width=True)

# Gráfico de pastel: Distribución de Accidentes por Tipo
with col4:
    datos_accidentes_tipo = pd.DataFrame({
        "Tipo": ["Leve", "Moderado", "Grave"],
        "Cantidad": [45, 30, 15]
    })
    fig_pie2 = px.pie(datos_accidentes_tipo, names="Tipo", values="Cantidad", 
                      title="Tipos de Accidente",
                      color_discrete_sequence=['#E74C3C', '#EC7063', '#F1948A'])  # Red color palette
    st.plotly_chart(fig_pie2, use_container_width=True)

st.markdown("---")
st.subheader("Cantidad de Horas Trabajadas (Último Mes)")

# Tabla de horas trabajadas por obra
horas_trabajadas = pd.DataFrame({
    "Obra": ["Proyecto A", "Proyecto B", "Proyecto C", "Proyecto D", "Proyecto E", "Proyecto F"],
    "Horas Trabajadas": [180, 165, 200, 150, 175, 190],
    "% de Cumplimiento": [95, 82, 100, 75, 88, 92]
})

# Mostrar la tabla con formato
st.dataframe(
    horas_trabajadas,
    column_config={
        "Horas Trabajadas": st.column_config.NumberColumn(format="%d hrs"),
        "% de Cumplimiento": st.column_config.NumberColumn(format="%d%%")
    },
    hide_index=True,
    use_container_width=True
)

st.markdown("---")
st.subheader("Ranking de Proveedores")

# Tabla de ranking de proveedores
proveedores = pd.DataFrame({
    "Proveedor": ["Constructora XYZ", "Servicios ABC", "Constructora 123", "Empresa DEF", "Constructora MNO"],
    "Obras": ["Proyecto B, Proyecto D", "Proyecto A, Proyecto C, Proyecto F", "Proyecto E", "Proyecto A, Proyecto B", "Proyecto C, Proyecto D"],
    "Calificación": [65, 72, 78, 85, 92]
})

# Ordenar proveedores de peor a mejor calificación
proveedores = proveedores.sort_values('Calificación')

# Mostrar la tabla con formato
st.dataframe(
    proveedores,
    column_config={
        "Proveedor": "Proveedor",
        "Obras": st.column_config.TextColumn(
            "Obras Asignadas",
            help="Proyectos en los que participa el proveedor"
        ),
        "Calificación": st.column_config.NumberColumn(
            "Calificación",
            help="Calificación del proveedor (0-100)",
            format="%d%%"
        )
    },
    hide_index=True,
    use_container_width=True
)

st.markdown("---")
st.subheader("Casos Recientes")
# Tabla con datos de casos (ejemplo)
casos = pd.DataFrame({
    "ID": [1, 2, 3, 4, 5],
    "Fecha": ["2025-02-01", "2025-02-02", "2025-02-03", "2025-02-04", "2025-02-05"],
    "Descripción": ["Caída de objeto", "Incidente eléctrico", "Accidente menor", "Falla en EPP", "Incidente con maquinaria"],
    "Estado": ["Resuelto", "Pendiente", "Resuelto", "Pendiente", "Resuelto"]
})
st.dataframe(casos)