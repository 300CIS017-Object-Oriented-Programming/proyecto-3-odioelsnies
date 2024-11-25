import os
import csv

class SNIESController:
    def __init__(self, carpeta_inputs):
        self.carpeta_inputs = carpeta_inputs

    def buscarPorPalabra(self, palabra_clave):
        
        resultados = {}

        # Verificar si la carpeta existe
        if not os.path.exists(self.carpeta_inputs):
            raise FileNotFoundError(f"La carpeta '{self.carpeta_inputs}' no existe.")

        # Iterar sobre todos los archivos CSV en la carpeta
        for archivo in os.listdir(self.carpeta_inputs):
            ruta_archivo = os.path.join(self.carpeta_inputs, archivo)
            if archivo.endswith(".csv"):
                print(f"Procesando archivo: {archivo}")

                # Leer el archivo CSV
                with open(ruta_archivo, mode='r', encoding='utf-8') as file:
                    reader = csv.DictReader(file, delimiter=';')
                    
                    # Limpiar encabezados
                    reader.fieldnames = [header.strip() for header in reader.fieldnames]
                    print(f"Encabezados: {reader.fieldnames}")

                    # Obtener el nombre de la última columna
                    ultima_columna = reader.fieldnames[-1]

                    # Buscar la palabra clave en las filas
                    for row in reader:
                        row = {k.strip(): v for k, v in row.items()}  # Limpiar claves
                        for columna, valor in row.items():
                            if palabra_clave.lower() in valor.lower():
                                # Agregar la fila al grupo correspondiente a la última columna
                                if ultima_columna not in resultados:
                                    resultados[ultima_columna] = []
                                resultados[ultima_columna].append(row)
                                break  # Salir después de encontrar la palabra clave en esta fila
        return resultados


