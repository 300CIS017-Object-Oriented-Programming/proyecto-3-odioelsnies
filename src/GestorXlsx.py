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