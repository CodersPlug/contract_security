import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración inicial de la página
st.set_page_config(page_title="Tablero Gestión de Incidentes", layout="wide", page_icon=":bar_chart:")

# Sección: Dashboard
st.title("Tablero de Gestión de Casos")
st.markdown("Soporte para la toma de decisiones basada en datos")

# Add filters in columns
col_filter1, col_filter2, col_filter3 = st.columns(3)

with col_filter1:
    # Date range picker
    fecha_inicio, fecha_fin = st.date_input(
        "Periodo",
        value=(pd.to_datetime("2025-01-01"), pd.to_datetime("2025-12-31")),
        min_value=pd.to_datetime("2025-01-01"),
        max_value=pd.to_datetime("2025-12-31"),
        format="DD/MM/YYYY"
    )

with col_filter2:
    # Country selector
    pais = st.selectbox(
        "País",
        options=["Todos", "Chile", "Perú", "Colombia", "Argentina"],
        index=0
    )

with col_filter3:
    # Project selector
    obra = st.selectbox(
        "Obra",
        options=["Todas", "Proyecto A", "Proyecto B", "Proyecto C", "Proyecto D", "Proyecto E", "Proyecto F", "Proyecto G"],
        index=0
    )

# Add a separator
st.markdown("---")

# Bar Charts Section
with st.expander("Gráficos de Tendencia", expanded=True):
    col1, spacing, col2 = st.columns([1, 0.1, 1])
    
    with col1:
        datos_mensuales = pd.DataFrame({
            "Mes": ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"],
            "Casos": [10, 12, 8, 15, 9, 11, 7, 13, 14, 10, 12, 9]
        })
        fig_bar = px.bar(datos_mensuales, x="Mes", y="Casos", title="Casos por Mes",
                        labels={"Casos": "Cantidad de Casos"},
                        color_discrete_sequence=['#2E86C1'])
        st.plotly_chart(fig_bar, use_container_width=True)

    with col2:
        datos_accidentes = pd.DataFrame({
            "Mes": ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"],
            "Accidentes": [8, 15, 10, 12, 7, 9, 11, 14, 13, 8, 10, 12]
        })
        fig_bar2 = px.bar(datos_accidentes, x="Mes", y="Accidentes", title="Accidentes por Mes",
                          labels={"Accidentes": "Cantidad de Accidentes"},
                          color_discrete_sequence=['#E74C3C'])  # Red color
        st.plotly_chart(fig_bar2, use_container_width=True)

# Pie Charts Section
with st.expander("Distribución por Tipo", expanded=True):
    col3, spacing2, col4 = st.columns([1, 0.1, 1])
    
    with col3:
        datos_tipo = pd.DataFrame({
            "Tipo": ["Seguridad", "Calidad", "Ambiente", "Otros"],
            "Cantidad": [50, 30, 25, 19]
        })
        fig_pie = px.pie(datos_tipo, names="Tipo", values="Cantidad", 
                         title="Tipos de Caso",
                         color_discrete_sequence=['#2E86C1', '#3498DB', '#5DADE2', '#85C1E9'])  # Blue color palette
        st.plotly_chart(fig_pie, use_container_width=True)

    with col4:
        datos_accidentes_tipo = pd.DataFrame({
            "Tipo": ["Leve", "Moderado", "Grave"],
            "Cantidad": [45, 30, 15]
        })
        fig_pie2 = px.pie(datos_accidentes_tipo, names="Tipo", values="Cantidad", 
                          title="Tipos de Accidente",
                          color_discrete_sequence=['#E74C3C', '#EC7063', '#F1948A'])  # Red color palette
        st.plotly_chart(fig_pie2, use_container_width=True)

# No Conformidad Section
with st.expander("No Conformidad", expanded=True):
    no_conformidad = pd.DataFrame({
        "Fecha": ["2025-02-05", "2025-02-04"],
        "Obra": ["Proyecto A", "Proyecto C"],
        "Proveedor": ["Constructora XYZ", "Servicios ABC"],
        "Descripción": ["Incumplimiento de normas de seguridad", "Falta de documentación requerida"]
    })

    # Convert Fecha column to datetime
    no_conformidad['Fecha'] = pd.to_datetime(no_conformidad['Fecha'])

    st.dataframe(
        no_conformidad,
        column_config={
            "Fecha": st.column_config.DateColumn("Fecha", format="DD-MM-YYYY"),
            "Obra": "Obra",
            "Proveedor": "Proveedor",
            "Descripción": "Descripción"
        },
        hide_index=True,
        use_container_width=True
    )

# Compliance Section
with st.expander("Cumplimiento por Obra", expanded=True):
    cumplimiento_data = pd.DataFrame({
        "Obra": ["Proyecto A", "Proyecto B", "Proyecto C", "Proyecto D", "Proyecto E", "Proyecto F", "Proyecto G"],
        "% de Cumplimiento": [95, 82, 100, 75, 88, 92, 60],
        "Estado": ["✅ Supera", "✅ Supera", "✅ Supera", "✅ Cumple", "✅ Supera", "✅ Supera", "❌ No Cumple"]
    })

    # Sort by compliance percentage
    cumplimiento_data = cumplimiento_data.sort_values('% de Cumplimiento', ascending=False)

    st.dataframe(
        cumplimiento_data,
        column_config={
            "% de Cumplimiento": st.column_config.NumberColumn(format="%d%%"),
            "Estado": st.column_config.TextColumn(
                "Estado vs Objetivo (75%)",
                help="✅ Cumple/Supera: >= 75%\n❌ No Cumple: < 75%"
            )
        },
        hide_index=True,
        use_container_width=True
    )

# Hours Worked Section
with st.expander("Horas Trabajadas por Obra", expanded=True):
    horas_data = pd.DataFrame({
        "Obra": ["Proyecto A", "Proyecto B", "Proyecto C", "Proyecto D", "Proyecto E", "Proyecto F", "Proyecto G"],
        "Horas Trabajadas": [180, 165, 200, 150, 175, 190, 120]
    })

    # Reorder hours table to match the compliance table order
    horas_data = horas_data.set_index('Obra').reindex(cumplimiento_data['Obra']).reset_index()

    st.dataframe(
        horas_data,
        column_config={
            "Horas Trabajadas": st.column_config.NumberColumn(format="%d hrs")
        },
        hide_index=True,
        use_container_width=True
    )

# Providers Ranking Section
with st.expander("Ranking de Proveedores", expanded=True):
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

# Recent Cases Section
with st.expander("Casos Recientes", expanded=True):
    casos = pd.DataFrame({
        "ID": [1, 2, 3, 4, 5],
        "Fecha": ["2025-02-01", "2025-02-02", "2025-02-03", "2025-02-04", "2025-02-05"],
        "Descripción": ["Caída de objeto", "Incidente eléctrico", "Accidente menor", "Falla en EPP", "Incidente con maquinaria"],
        "Estado": ["Resuelto", "Pendiente", "Resuelto", "Pendiente", "Resuelto"]
    })
    st.dataframe(casos)

# Metrics Section
with st.expander("Métricas Generales", expanded=True):
    col_card1, col_card2 = st.columns(2)
    
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