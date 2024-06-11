from script.view.aplicacion_vista import Aplicacion


class ControladorAplicacion :

    def __init__(self) :
        
        self.__vista_aplicacion = Aplicacion()

    def controlador_iniciar(self):
        self.__vista_aplicacion.iniciar()

    