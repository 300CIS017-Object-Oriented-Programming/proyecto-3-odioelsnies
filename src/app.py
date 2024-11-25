import os
import re
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
from SNIEScontroller import SNIESController


carpeta_inputs = "inputs"

controller = SNIESController(carpeta_inputs)


st.sidebar.title("Menú")
opcion = st.sidebar.radio(
    "Seleccione una opción:",
    ["Página de bienvenida", "Procesar datos por rango", "Procesar datos por palabra clave"]
)

if opcion == "Página de bienvenida":
    st.title("Bienvenido al Sistema de Procesamiento de Datos SNIES")
    st.write("Seleccione una opción del menú para continuar:")
    st.write("- **Procesar datos por rango**: Analiza datos según un rango definido.")
    st.write("- **Procesar datos por palabra clave**: Busca y procesa datos según una palabra clave.")

elif opcion == "Procesar datos por rango":
    st.title("Procesar Datos por Rango")

   
    anio_inicial = st.number_input("Año inicial", min_value=1900, max_value=2100, step=1, value=2020)
    anio_final = st.number_input("Año final", min_value=1900, max_value=2100, step=1, value=2023)

    if st.button("Procesar Datos"):
        
        if anio_inicial > anio_final:
            st.error("El año inicial no puede ser mayor al año final.")
        else:
            
            archivos_validos = []
            for archivo in os.listdir(carpeta_inputs):
                
                match = re.search(r'\d{4}', archivo)
                if match:
                    anio = int(match.group())
                    if anio_inicial <= anio <= anio_final:
                        archivos_validos.append(os.path.join(carpeta_inputs, archivo))

            if not archivos_validos:
                st.warning("No se encontraron archivos para el rango de años especificado.")
            else:
                st.write(f"Archivos encontrados: {', '.join([os.path.basename(a) for a in archivos_validos])}")

                
                tabla_consolidada = pd.DataFrame()
                for archivo in archivos_validos:
                    
                    df = pd.read_csv(archivo, delimiter=';', encoding='utf-8')

                    
                    df.columns = [col.strip().upper() for col in df.columns]

                    
                    anio = int(re.search(r'\d{4}', archivo).group())
                    df['AÑO'] = anio  # Agregar columna del año

                    
                    tabla_consolidada = pd.concat([tabla_consolidada, df], ignore_index=True)

                
                columnas_requeridas = ['PROGRAMA ACADÉMICO', 'INSCRITOS', 'ADMITIDOS', 'PRIMER CURSO', 'MATRICULADOS', 'GRADUADOS']
                columnas_presentes = [col for col in columnas_requeridas if col in tabla_consolidada.columns]

                if 'PROGRAMA ACADÉMICO' not in columnas_presentes:
                    st.error("No se encontró la columna 'PROGRAMA ACADÉMICO' en los archivos procesados.")
                else:
                    
                    tabla_resumen = tabla_consolidada[columnas_presentes].groupby('PROGRAMA ACADÉMICO').sum()

                    
                    st.subheader("Tabla Consolidada")
                    if not tabla_resumen.empty:
                        gb = GridOptionsBuilder.from_dataframe(tabla_resumen)
                        gb.configure_pagination()
                        grid_options = gb.build()

                        AgGrid(
                            tabla_resumen,
                            gridOptions=grid_options,
                            update_mode=GridUpdateMode.NO_UPDATE,
                            height=500,
                            theme="streamlit"
                        )
                    else:
                        st.warning("No se encontraron datos para consolidar en los archivos seleccionados.")

elif opcion == "Procesar datos por palabra clave":
    st.title("Procesar Datos por Palabra Clave")

    
    palabra_clave = st.text_input("Ingresa una palabra clave para buscar en los programas académicos")

    if st.button("Buscar"):
        resultados = controller.buscarPorPalabra(palabra_clave)

        if resultados:
            tablas_por_ultima_columna = {}
            for ultima_columna, filas in resultados.items():
                tabla = pd.DataFrame(filas)
                st.subheader(f"Tabla para: {ultima_columna}")

                gb = GridOptionsBuilder.from_dataframe(tabla)
                gb.configure_selection(selection_mode="multiple", use_checkbox=True)
                grid_options = gb.build()

                grid_response = AgGrid(
                    tabla,
                    gridOptions=grid_options,
                    update_mode=GridUpdateMode.SELECTION_CHANGED,
                    height=300,
                    theme="streamlit"
                )

                seleccionados_por_tabla = {}
                seleccionados_por_tabla[ultima_columna] = grid_response["selected_rows"]

            if st.button("Generar Análisis"):
                for ultima_columna, seleccionados in seleccionados_por_tabla.items():
                    if seleccionados:
                        seleccionados_df = pd.DataFrame(seleccionados)
                        st.subheader(f"Análisis para: {ultima_columna}")
                        st.bar_chart(seleccionados_df[ultima_columna])



