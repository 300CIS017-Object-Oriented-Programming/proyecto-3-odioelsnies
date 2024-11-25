import os
import csv
from ProgramasAcademico import ProgramaAcademico

class SNIESController:
    def __init__(self, carpeta_inputs):
        self.carpeta_inputs = carpeta_inputs
        self.programas_academicos = []

    def buscarPorPalabra(self, palabra_clave):
        """
        Busca la palabra clave en todas las columnas de todos los archivos CSV dentro de la carpeta `inputs`.
        """
        resultados = []
        archivos_procesados = []

        # Verificar si la carpeta existe
        if not os.path.exists(self.carpeta_inputs):
            raise FileNotFoundError(f"La carpeta '{self.carpeta_inputs}' no existe.")

        # Iterar sobre todos los archivos CSV en la carpeta
        for archivo in os.listdir(self.carpeta_inputs):
            ruta_archivo = os.path.join(self.carpeta_inputs, archivo)
            if archivo.endswith(".csv"):
                archivos_procesados.append(archivo)
                print(f"Buscando en: {archivo}")

                # Leer el archivo CSV
                with open(ruta_archivo, mode='r', encoding='utf-8') as file:
                    reader = csv.DictReader(file, delimiter=';')
                    
                    # Limpiar los encabezados
                    reader.fieldnames = [header.strip() for header in reader.fieldnames]
                    print(f"Encabezados limpiados: {reader.fieldnames}")  # Debug

                    # Buscar la palabra clave en todas las filas y columnas
                    for row in reader:
                        row = {k.strip(): v for k, v in row.items()}  # Limpiar claves
                        for columna, valor in row.items():
                            if palabra_clave.lower() in valor.lower():
                                # Crear un objeto ProgramaAcademico o capturar la fila encontrada
                                resultados.append(row)
                                break  # No seguir revisando otras columnas de la misma fila
        if not archivos_procesados:
            print("No se encontraron archivos CSV en la carpeta proporcionada.")
        return resultados





