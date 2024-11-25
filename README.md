# Documentación Técnica del Proyecto SNIES

**Autores**: Santiago Figueroa y Juan Carlos Díaz

---

## Estructura del Proyecto

### 1. Carpeta `inputs`:
- Contiene los archivos con datos de programas académicos, matriculados, graduados y otros parámetros relevantes.
- Los nombres de los archivos siguen una nomenclatura estándar para su procesamiento automático.

### 2. Archivos `.py` del Proyecto:
- **`app.py`**: Archivo secundario utilizado para organizar funciones auxiliares y componentes reutilizables que soportan la ejecución de la aplicación.
- **`main.py`**: Archivo principal que ejecuta la aplicación de Streamlit. Contiene las rutas de navegación, configuraciones generales y puntos de entrada.
- **`SNIESController.py`**: Controla el flujo de datos y las funciones principales para procesar los archivos CSV y generar estadísticas.
- **`GestorCsv.py`**: Encargado de leer y validar los archivos CSV, manejando errores comunes como formato incorrecto o datos faltantes.
- **`GestorJson.py`**: Facilita la exportación de configuraciones o resultados a archivos JSON para su almacenamiento.
- **`View.py`**: Genera visualizaciones gráficas como histogramas, gráficos de barras y tablas interactivas.

---

## Cumplimiento de Requerimientos

| Requisito                   | Descripción                                      | Estado        |
|-----------------------------|--------------------------------------------------|---------------|
| Lectura de múltiples archivos | Lectura automatizada desde la carpeta `inputs`. | ✅ Completado |
| Generación de estadísticas   | Tasa de graduados, tasa de retención, etc.       | ✅ Completado |
| Visualizaciones interactivas | Gráficos de barras, tablas dinámicas.           | 🔄 Incompleto |
| Exportación de resultados    | Exportación a JSON y gráficos descargables.      | 🔄 Incompleto |
| Modularidad del código       | Separación en funciones y módulos.              | ✅ Completado |


