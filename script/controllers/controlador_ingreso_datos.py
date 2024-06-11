

class ControladorDatos:
    def __init__(self, ingreso_datos) :
        self.ingreso_datos = ingreso_datos
    
    def controlador_volver(self):
        self.ingreso_datos.app.mostrar_marco(self.ingreso_datos.app.marco_menu.frame)

    def controlador_enviar(self):
        self.ingreso_datos.app.mostrar_marco(self.ingreso_datos.app.marco_tabla.frame)
