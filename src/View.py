class View:
    def init(self):
        self.controlador = SNIESController("", "", "", "", "", "", "")

    def pantalla_bienvenido(self):
        # Implementación
        pass

    def visualizacion_datos_extra(self):
        # Implementación
        pass

    def buscar_por_palabra_clave_y_formacion(self):
        # Implementación
        pass

    def salir(self):
        # Implementación
        pass

    def is_convertible_to_int(self, value):
        # Implementación
        return value.isdigit()