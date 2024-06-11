
class ControladorMenu :

    def __init__(self, menu_marco):
        self.menu_marco = menu_marco

    def controlador_salir (self):
        self.menu_marco.app.ventana.quit()

    def controlador_nuevo_estudio(self):
        self.menu_marco.app.mostrar_marco(self.menu_marco.app.marco_datos.frame)