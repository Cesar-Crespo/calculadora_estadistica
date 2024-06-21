
class ModeloDatos:
    def __init__(self):
        self.datos = []
        self.nombre_estudio = ''

    def agregar_dato (self,nombre_dato,cantidad_dato) :
        self.datos.append((nombre_dato,cantidad_dato))

    
    def eliminar_dato(self, index):
        self.datos.pop(index)

    def limpiar_datos(self):
        self.datos.clear()

    def obtener_dato(self, index):
        return self.datos[index]

    def obtener_datos(self):
        return self.datos
    
    def establecer_nombre_estudio(self, nombre):
        self.nombre_estudio = nombre

    def obtener_nombre_estudio(self):
        return self.nombre_estudio
    

