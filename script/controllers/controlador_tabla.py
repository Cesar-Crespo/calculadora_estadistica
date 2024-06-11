

class ControladorTabla:
    def __init__(self,tabla):
        self.tabla = tabla

    def controlador_salir(self):
        self.tabla.app.ventana.quit()

    def controlador_volver(self):
        self.tabla.app.mostrar_marco(self.tabla.app.marco_datos.frame)

    def controlador_volver_menu(self):
        self.tabla.app.mostrar_marco(self.tabla.app.marco_menu.frame)

    