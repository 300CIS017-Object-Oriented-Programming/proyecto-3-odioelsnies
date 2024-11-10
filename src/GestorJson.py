class GestorJson:
    def __init__(self):
        pass

    def crear_archivo_json(selfS, ruta, mapa_de_programas_academicos):
        try:
            data = {}
            for codigo, programa in mapa_de_programas_academicos.items():
                data[codigo] = {
                    "codigoDeLaInstitucion": programa.codigo_de_la_institucion,
                    "iesPadre": programa.ies_padre,
                    "institucionDeEducacionSuperiorIes": programa.institucion_de_educacion_superior_ies,
                }
            with open(ruta, 'w') as json_file:
                json.dump(data, json_file, indent=4)
            print(f"Archivo .json creado exitosamente en {ruta}")
        except Exception as e:
            print(f"Error al crear el archivo .json: {e}")


class GestorCsv:
    def __init__(self):
        pass

    def leer_programas_csv(self, ruta):
        # Implementar la lectura del archivo CSV aquí
        pass

class GestorXlsx:
    def __init__(self):
        pass

    def crear_archivo_xlsx(self, ruta, mapa_de_programas_academicos):
        try:
            data = []
            for codigo, programa in mapa_de_programas_academicos.items():
                data.append({
                    "codigoDeLaInstitucion": programa.codigo_de_la_institucion,
                    "iesPadre": programa.ies_padre,
                    "institucionDeEducacionSuperiorIes": programa.institucion_de_educacion_superior_ies,
                })
            df = pd.DataFrame(data)
            df.to_excel(ruta, index=False)
            print(f"Archivo .xlsx creado exitosamente en {ruta}")
        except Exception as e:
            print(f"Error al crear el archivo .xlsx: {e}")
            






class SNIESController:
    def __init__(self, ruta_programas_csv, ruta_admitidos, ruta_graduados, ruta_inscritos, ruta_matriculados, ruta_matriculados_primer_semestre, ruta_output):
        self.programas_academicos = {}
        self.gestor_csv_obj = GestorCsv()
        self.gestor_xlsx_obj = GestorXlsx()
        self.gestor_json_obj = GestorJson()
        self.etiquetas_columnas = []
        self.ruta_programas_csv = ruta_programas_csv
        self.ruta_output = ruta_output

    def procesar_datos_csv(self, ano1, ano2):
        pass

    def exportar_datos_xlsx(self):
        self.gestor_xlsx_obj.crear_archivo_xlsx(self.ruta_output + "datos_exportados.xlsx", self.programas_academicos)

    def exportar_datos_json(self):
        self.gestor_json_obj.crear_archivo_json(self.ruta_output + "datos_exportados.json", self.programas_academicos)