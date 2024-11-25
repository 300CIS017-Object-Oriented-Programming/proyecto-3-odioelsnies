import csv
from ProgramasAcademico import ProgramaAcademico

class SNIESController:
    def __init__(self, ruta_csv):
        self.ruta_csv = ruta_csv
        self.programas_academicos = []

    def buscarPorPalabra(self, palabra_clave):
        resultados = []
        with open(self.ruta_csv, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            
            #remueve caracteres invisibles y espacios
            reader.fieldnames = [header.strip().replace('\ufeff', '') for header in reader.fieldnames]
            print("Encabezados limpiados:", reader.fieldnames)  # para confirmar los encabezados limpios

            for row in reader:
                #limpia espacios adicionales en las claves de cada fila
                row = {k.strip(): v for k, v in row.items()}
                if palabra_clave.lower() in row['PROGRAMA ACADÉMICO'].lower():
                    programa = ProgramaAcademico(
                        codigo_institucion=row['CÓDIGO DE LA INSTITUCIÓN'],
                        ies_padre=row['IES_PADRE'],
                        institucion=row['INSTITUCIÓN DE EDUCACIÓN SUPERIOR (IES)'],
                        principal_o_seccional=row['PRINCIPAL O SECCIONAL'],
                        id_sector_ies=row['ID SECTOR IES'],
                        sector_ies=row['SECTOR IES'],
                        id_caracter=row['ID CARACTER'],
                        caracter_ies=row['CARACTER IES'],
                        codigo_departamento_ies=row['CÓDIGO DEL DEPARTAMENTO (IES)'],
                        departamento_domicilio_ies=row['DEPARTAMENTO DE DOMICILIO DE LA IES'],
                        codigo_municipio_ies=row['CÓDIGO DEL MUNICIPIO IES'],
                        municipio_domicilio_ies=row['MUNICIPIO DE DOMICILIO DE LA IES'],
                        codigo_snies=row['CÓDIGO SNIES DEL PROGRAMA'],
                        programa_academico=row['PROGRAMA ACADÉMICO'],
                        id_nivel_academico=row['ID NIVEL ACADÉMICO'],
                        nivel_academico=row['NIVEL ACADÉMICO'],
                        id_nivel_formacion=row['ID NIVEL DE FORMACIÓN'],
                        nivel_formacion=row['NIVEL DE FORMACIÓN'],
                        id_metodologia=row['ID METODOLOGÍA'],
                        metodologia=row['METODOLOGÍA'],
                        id_area=row['ID ÁREA'],
                        area_conocimiento=row['ÁREA DE CONOCIMIENTO'],
                        id_nucleo=row['ID NÚCLEO'],
                        nucleo_basico_conocimiento=row['NÚCLEO BÁSICO DEL CONOCIMIENTO (NBC)'],
                        id_cine_campo_amplio=row['ID CINE CAMPO AMPLIO'],
                        desc_cine_campo_amplio=row['DESC CINE CAMPO AMPLIO'],
                        id_cine_campo_especifico=row['ID CINE CAMPO ESPECIFICO'],
                        desc_cine_campo_especifico=row['DESC CINE CAMPO ESPECIFICO'],
                        id_cine_codigo_detallado=row['ID CINE CODIGO DETALLADO'],
                        desc_cine_codigo_detallado=row['DESC CINE CODIGO DETALLADO'],
                        codigo_departamento_programa=row['CÓDIGO DEL DEPARTAMENTO (PROGRAMA)'],
                        departamento_oferta_programa=row['DEPARTAMENTO DE OFERTA DEL PROGRAMA'],
                        codigo_municipio_programa=row['CÓDIGO DEL MUNICIPIO (PROGRAMA)'],
                        municipio_oferta_programa=row['MUNICIPIO DE OFERTA DEL PROGRAMA']
                    )
                    resultados.append(programa)
        return resultados




