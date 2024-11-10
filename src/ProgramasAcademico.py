class ProgramaAcademico:
    def __init__(self):
        self.codigo_de_la_institucion = 0
        self.ies_padre = 0
        self.institucion_de_educacion_superior_ies = ""
        self.principal_o_seccional = ""
        self.id_sector_ies = 0
        self.sector_ies = ""
        self.id_caracter = 0
        self.caracter_ies = ""
        self.codigo_del_departamento_ies = 0
        self.departamento_de_domicilio_de_la_ies = ""
        self.codigo_del_municipio_ies = 0
        self.municipio_de_domicilio_de_la_ies = ""
        self.codigo_snies_del_programa = 0
        self.programa_academico = ""
        self.id_nivel_academico = 0
        self.nivel_academico = ""
        self.id_nivel_de_formacion = 0
        self.nivel_de_formacion = ""
        self.id_metodologia = 0
        self.metodologia = ""
        self.id_area = 0
        self.area_de_conocimiento = ""
        self.id_nucleo = 0
        self.nucleo_basico_del_conocimiento_nbc = ""
        self.id_cine_campo_amplio = 0
        self.desc_cine_campo_amplio = ""
        self.id_cine_campo_especifico = 0
        self.desc_cine_campo_especifico = ""
        self.id_cine_codigo_detallado = 0
        self.desc_cine_codigo_detallado = ""
        self.codigo_del_departamento_programa = 0
        self.departamento_de_oferta_del_programa = ""
        self.codigo_del_municipio_programa = 0
        self.municipio_de_oferta_del_programa = ""
        self.consolidados = []

        # Setters y Getters para cada atributo

    def set_codigo_de_la_institucion(self, valor):
        self.codigo_de_la_institucion = valor

    def get_codigo_de_la_institucion(self):
        return self.codigo_de_la_institucion

    def set_ies_padre(self, valor):
        self.ies_padre = valor

    def get_ies_padre(self):
        return self.ies_padre

    def set_institucion_de_educacion_superior_ies(self, valor):
        self.institucion_de_educacion_superior_ies = valor

    def get_institucion_de_educacion_superior_ies(self):
        return self.institucion_de_educacion_superior_ies

    def set_principal_o_seccional(self, valor):
        self.principal_o_seccional = valor

    def get_principal_o_seccional(self):
        return self.principal_o_seccional

    def set_id_sector_ies(self, valor):
        self.id_sector_ies = valor

    def get_id_sector_ies(self):
        return self.id_sector_ies

    def set_sector_ies(self, valor):
        self.sector_ies = valor

    def get_sector_ies(self):
        return self.sector_ies

    def set_id_caracter(self, valor):
        self.id_caracter = valor

    def get_id_caracter(self):
        return self.id_caracter

    def set_caracter_ies(self, valor):
        self.caracter_ies = valor

    def get_caracter_ies(self):
        return self.caracter_ies

    def set_codigo_del_departamento_ies(self, valor):
        self.codigo_del_departamento_ies = valor

    def get_codigo_del_departamento_ies(self):
        return self.codigo_del_departamento_ies

    def set_departamento_de_domicilio_de_la_ies(self, valor):
        self.departamento_de_domicilio_de_la_ies = valor

    def get_departamento_de_domicilio_de_la_ies(self):
        return self.departamento_de_domicilio_de_la_ies

    def set_codigo_del_municipio_ies(self, valor):
        self.codigo_del_municipio_ies = valor

    def get_codigo_del_municipio_ies(self):
        return self.codigo_del_municipio_ies

    def set_municipio_de_domicilio_de_la_ies(self, valor):
        self.municipio_de_domicilio_de_la_ies = valor

    def get_municipio_de_domicilio_de_la_ies(self):
        return self.municipio_de_domicilio_de_la_ies

    def set_codigo_snies_del_programa(self, valor):
        self.codigo_snies_del_programa = valor

    def get_codigo_snies_del_programa(self):
        return self.codigo_snies_del_programa

    def set_programa_academico(self, valor):
        self.programa_academico = valor

    def get_programa_academico(self):
        return self.programa_academico

    def set_id_nivel_academico(self, valor):
        self.id_nivel_academico = valor

    def get_id_nivel_academico(self):
        return self.id_nivel_academico

    def set_nivel_academico(self, valor):
        self.nivel_academico = valor

    def get_nivel_academico(self):
        return self.nivel_academico

    def set_id_nivel_de_formacion(self, valor):
        self.id_nivel_de_formacion = valor

    def get_id_nivel_de_formacion(self):
        return self.id_nivel_de_formacion

    def set_nivel_de_formacion(self, valor):
        self.nivel_de_formacion = valor

    def get_nivel_de_formacion(self):
        return self.nivel_de_formacion

    def set_id_metodologia(self, valor):
        self.id_metodologia = valor

    def get_id_metodologia(self):
        return self.id_metodologia

    def set_metodologia(self, valor):
        self.metodologia = valor

    def get_metodologia(self):
        return self.metodologia

    def set_id_area(self, valor):
        self.id_area = valor

    def get_id_area(self):
        return self.id_area

    def set_area_de_conocimiento(self, valor):
        self.area_de_conocimiento = valor

    def get_area_de_conocimiento(self):
        return self.area_de_conocimiento

    def set_id_nucleo(self, valor):
        self.id_nucleo = valor

    def get_id_nucleo(self):
        return self.id_nucleo

    def set_nucleo_basico_del_conocimiento_nbc(self, valor):
        self.nucleo_basico_del_conocimiento_nbc = valor

    def get_nucleo_basico_del_conocimiento_nbc(self):
        return self.nucleo_basico_del_conocimiento_nbc

    def set_id_cine_campo_amplio(self, valor):
        self.id_cine_campo_amplio = valor

    def get_id_cine_campo_amplio(self):
        return self.id_cine_campo_amplio

    def set_desc_cine_campo_amplio(self, valor):
        self.desc_cine_campo_amplio = valor

    def get_desc_cine_campo_amplio(self):
        return self.desc_cine_campo_amplio

    def set_id_cine_campo_especifico(self, valor):
        self.id_cine_campo_especifico = valor

    def get_id_cine_campo_especifico(self):
        return self.id_cine_campo_especifico

    def set_desc_cine_campo_especifico(self, valor):
        self.desc_cine_campo_especifico = valor

    def get_desc_cine_campo_especifico(self):
        return self.desc_cine_campo_especifico

    def set_id_cine_codigo_detallado(self, valor):
        self.id_cine_codigo_detallado = valor

    def get_id_cine_codigo_detallado(self):
        return self.id_cine_codigo_detallado

    def set_desc_cine_codigo_detallado(self, valor):
        self.desc_cine_codigo_detallado = valor

    def get_desc_cine_codigo_detallado(self):
        return self.desc_cine_codigo_detallado

    def set_codigo_del_departamento_programa(self, valor):
        self.codigo_del_departamento_programa = valor

    def get_codigo_del_departamento_programa(self):
        return self.codigo_del_departamento_programa

    def set_departamento_de_oferta_del_programa(self, valor):
        self.departamento_de_oferta_del_programa = valor

    def get_departamento_de_oferta_del_programa(self):
        return self.departamento_de_oferta_del_programa

    def set_codigo_del_municipio_programa(self, valor):
        self.codigo_del_municipio_programa = valor

    def get_codigo_del_municipio_programa(self):
        return self.codigo_del_municipio_programa

    def set_municipio_de_oferta_del_programa(self, valor):
        self.municipio_de_oferta_del_programa = valor

    def get_municipio_de_oferta_del_programa(self):
        return self.municipio_de_oferta_del_programa