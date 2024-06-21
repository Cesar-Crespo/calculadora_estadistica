from script.models.modelo_datos import ModeloDatos


class ControladorDatos:
    def __init__(self, ingreso_datos) :
        self.vista_ingreso_datos = ingreso_datos    
        self.modelo_datos = ModeloDatos()
  
    def agregar_dato(self):
        nombre_dato = self.vista_ingreso_datos.obtener_dato()
        cantidad_dato = self.vista_ingreso_datos.obtener_cantidad_dato()
        if nombre_dato and cantidad_dato.isdigit():
            if float(cantidad_dato) > 0 :
                self.modelo_datos.agregar_dato(nombre_dato,cantidad_dato)
                self.vista_ingreso_datos.actualizar_datos_guardados(self.modelo_datos.obtener_datos())
                self.vista_ingreso_datos.actualizar_combobox(self.modelo_datos.obtener_datos())
                self.vista_ingreso_datos.limpiar_entradas_datos()
            else:
                self.vista_ingreso_datos.mostrar_mensaje_error("La cantida debe de ser un numero entero positivo")
        elif not cantidad_dato.isdigit():
            self.vista_ingreso_datos.mostrar_mensaje_error("La cantidad debe de ser un entero positivo")      
        else:
            self.vista_ingreso_datos.mostrar_mensaje_error("Por favor complete tanto el nombre como la cantidad")

    def modificar_dato(self):
        if not self.modelo_datos.obtener_datos():
            self.vista_ingreso_datos.mostrar_mensaje_error("Por favor complete tanto el nombre como la cantidad")
            return
        
        index = self.vista_ingreso_datos.seleccion_dato_combobox.current()
        if index == -1:
            self.vista_ingreso_datos.mostrar_mensaje_error("Error, selecione un dato para modificar")
            return
        
        nombre, cantidad = self.modelo_datos.obtener_dato(index)
        self.vista_ingreso_datos.limpiar_entradas_datos()
        self.vista_ingreso_datos.entry_dato.insert(0, nombre)
        self.vista_ingreso_datos.entry_cantidad_dato.insert(0, cantidad)
        self.modelo_datos.eliminar_dato(index)
        self.vista_ingreso_datos.actualizar_datos_guardados(self.modelo_datos.obtener_datos())
        self.vista_ingreso_datos.limpiar_combobox()

    def eliminar_dato(self):

        if not self.modelo_datos.obtener_datos():
            self.vista_ingreso_datos.mostrar_mensaje_error("Error, selecione un dato para eliminar")
            return
        
        index = self.vista_ingreso_datos.seleccion_dato_combobox.current()
        if index == -1 :
            self.vista_ingreso_datos.mostrar_mensaje_error("Seleccione un dato para eliminar")
            return
        
        confirmacion = self.vista_ingreso_datos.mostrar_mensaje_confirmacion("¿Estas seguro de eliminar este dato?")
        if confirmacion :
            self.modelo_datos.eliminar_dato(index)
            self.vista_ingreso_datos.actualizar_datos_guardados(self.modelo_datos.obtener_datos())
            self.vista_ingreso_datos.actualizar_combobox(self.modelo_datos.obtener_datos())
            self.vista_ingreso_datos.limpiar_combobox()


    def enviar_datos(self):
        nombre_estudio = self.vista_ingreso_datos.obtener_nombre_estudio()
        self.modelo_datos.establecer_nombre_estudio(nombre_estudio)
        n_estudio = self.modelo_datos.obtener_nombre_estudio()
        print(n_estudio)
        if not n_estudio :
            self.vista_ingreso_datos.mostrar_mensaje_error("Ingresa un nombre para el estudio")
            return
        
        if self.modelo_datos.obtener_datos():
            print("los datos: ", self.modelo_datos.obtener_datos())
            confirmacion = self.vista_ingreso_datos.mostrar_mensaje_confirmacion("¿Estás seguro de enviar los datos?")
            if confirmacion:
                self.vista_ingreso_datos.mostrar_mensaje_informacion("Los datos han sido enviados correctamente.")
                self.vista_ingreso_datos.limpiar_entradas_datos()
                self.vista_ingreso_datos.limpiar_combobox()

                self.vista_ingreso_datos.app.enviar_datos_a_tabla(self.modelo_datos.obtener_datos(), self.modelo_datos.obtener_nombre_estudio())

                

        else:
            self.vista_ingreso_datos.mostrar_mensaje_error("no hay datos para enviar")
            return

    def limpiar_datos(self):
        self.modelo_datos.limpiar_datos()
        self.vista_ingreso_datos.limpiar_entrada_nombre_estudio()
        self.vista_ingreso_datos.limpiar_entradas_datos()
        self.vista_ingreso_datos.actualizar_datos_guardados(self.modelo_datos.obtener_datos())
        self.vista_ingreso_datos.actualizar_combobox(self.modelo_datos.obtener_datos())
        self.vista_ingreso_datos.limpiar_combobox()

    def controlador_volver(self):
        self.limpiar_datos()
        self.modelo_datos.limpiar_datos()
        self.vista_ingreso_datos.app.mostrar_marco(self.vista_ingreso_datos.app.marco_menu.frame)