import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
from SNIEScontroller import SNIESController

# Ruta de la carpeta con los CSVs
carpeta_inputs = "inputs"

# Crear instancia del controlador
controller = SNIESController(carpeta_inputs)

st.title("Búsqueda de Programas SNIES con Selección")

palabra_clave = st.text_input("Ingresa una palabra clave para buscar en los programas académicos")

if st.button("Buscar"):
    resultados = controller.buscarPorPalabra(palabra_clave)
    if resultados:
        # Configurar opciones de la tabla
        gb = GridOptionsBuilder.from_dataframe(resultados)
        gb.configure_selection(selection_mode="multiple", use_checkbox=True)
        gb.configure_column("checkbox", headerCheckboxSelection=True)  # Selección general
        grid_options = gb.build()

        # Mostrar tabla con selección
        grid_response = AgGrid(
            resultados,
            gridOptions=grid_options,
            update_mode=GridUpdateMode.SELECTION_CHANGED,
            height=400,
            theme="streamlit"
        )

        # Recuperar filas seleccionadas
        seleccionados = grid_response["selected_rows"]
        st.write("Filas seleccionadas:", seleccionados)
    else:
        st.write("No se encontraron resultados para la palabra clave ingresada.")
