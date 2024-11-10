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