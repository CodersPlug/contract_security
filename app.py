import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración inicial de la página
st.set_page_config(page_title="Tablero Gestión de Incidentes", layout="wide", page_icon=":bar_chart:")

# Sidebar de navegación
st.sidebar.title("Menú de Navegación")
menu = st.sidebar.radio("Selecciona una sección:", ("Dashboard", "Registro de Incidentes", "Reportes"))

# Sección: Dashboard
if menu == "Dashboard":
    st.title("Tablero de Gestión de Incidentes")
    st.markdown("Este tablero muestra indicadores clave para el seguimiento de incidentes en obra.")

    # Indicadores clave con st.metric()
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Incidentes", 124)
    col2.metric("Incidentes Resueltos", 100)
    col3.metric("Incidentes Pendientes", 24)
    col4.metric("Días sin Accidentes", 15)

    st.markdown("---")

    # Gráfico de barras: Incidentes por Mes (datos de ejemplo)
    datos_mensuales = pd.DataFrame({
        "Mes": ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"],
        "Incidentes": [10, 12, 8, 15, 9, 11, 7, 13, 14, 10, 12, 9]
    })
    fig_bar = px.bar(datos_mensuales, x="Mes", y="Incidentes", title="Incidentes por Mes",
                     labels={"Incidentes": "Cantidad de Incidentes"})
    st.plotly_chart(fig_bar, use_container_width=True)

    # Gráfico de pastel: Distribución de Incidentes por Tipo (datos de ejemplo)
    datos_tipo = pd.DataFrame({
        "Tipo": ["Seguridad", "Calidad", "Ambiente", "Otros"],
        "Cantidad": [50, 30, 25, 19]
    })
    fig_pie = px.pie(datos_tipo, names="Tipo", values="Cantidad", title="Distribución por Tipo de Incidente")
    st.plotly_chart(fig_pie, use_container_width=True)

    st.markdown("---")
    st.subheader("Incidentes Recientes")
    # Tabla con datos de incidentes (ejemplo)
    incidentes = pd.DataFrame({
        "ID": [1, 2, 3, 4, 5],
        "Fecha": ["2025-02-01", "2025-02-02", "2025-02-03", "2025-02-04", "2025-02-05"],
        "Descripción": ["Caída de objeto", "Incidente eléctrico", "Accidente menor", "Falla en EPP", "Incidente con maquinaria"],
        "Estado": ["Resuelto", "Pendiente", "Resuelto", "Pendiente", "Resuelto"]
    })
    st.dataframe(incidentes)

# Sección: Registro de Incidentes
elif menu == "Registro de Incidentes":
    st.title("Registro de Incidentes")
    st.markdown("Utiliza el siguiente formulario para capturar nuevos incidentes en obra.")

    with st.form("form_registro"):
        fecha = st.date_input("Fecha del Incidente")
        descripcion = st.text_area("Descripción del Incidente")
        estado = st.selectbox("Estado del Incidente", ["Abierto", "En proceso", "Cerrado"])
        # Campos para adjuntar multimedia
        imagenes = st.file_uploader("Adjuntar Imágenes", accept_multiple_files=True, type=["png", "jpg", "jpeg"])
        videos = st.file_uploader("Adjuntar Videos", accept_multiple_files=True, type=["mp4", "mov"])
        submit_button = st.form_submit_button("Registrar Incidente")

        if submit_button:
            st.success("¡Incidente registrado correctamente!")
            # Aquí se podría agregar la lógica para guardar la información en una base de datos o sistema de almacenamiento

# Sección: Reportes
elif menu == "Reportes":
    st.title("Generación de Reportes")
    st.markdown("Selecciona el rango de fechas y parámetros para generar reportes personalizados de incidentes.")

    col_date1, col_date2 = st.columns(2)
    with col_date1:
        fecha_inicio = st.date_input("Fecha de Inicio")
    with col_date2:
        fecha_fin = st.date_input("Fecha de Fin")
    
    if st.button("Generar Reporte"):
        st.write("Generando reporte para el periodo seleccionado...")
        # Aquí se implementaría la generación dinámica del reporte (por ejemplo, extracción y filtrado de datos)
        st.success("Reporte generado exitosamente. (Esta es una simulación.)")