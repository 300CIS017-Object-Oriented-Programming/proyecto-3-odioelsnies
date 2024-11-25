class Consolidado:
    def __init__(self):
        self.inscritos = 0
        self.admitidos = 0
        self.matriculados_primer_semestre = 0
        self.matriculados = 0
        self.graduados = 0
        self.id_sexo = 0
        self.sexo = ""
        self.ano = 0
        self.semestre = 0

    def set_inscritos(self, inscritos):
        self.inscritos = inscritos

    def get_inscritos(self):
        return self.inscritos