from script.models.modelo_datos_excel import ModeloDatos
from script.models.modelo_datos import ModeloDatos
from collections import Counter
from tkinter import *
from tkinter import filedialog,messagebox

class ControladorTabla:

    def __init__(self, tabla):
        self.modelo = ModeloDatos()
        self.m = ModeloDatos()
        self.tabla = tabla
        self.datos_unicos = set()
        self.son_numeros = True

    def crear_tabla(self, datos):
        datos_validos = self.validar_datos(datos)
        if datos_validos:
            self.datos_unicos, self.son_numeros = datos_validos
            datos_ordenados = self.obtener_datos_ordenados(datos)
            self.insertar_datos(datos_ordenados)

        else:
            pass
    
    def validar_datos(self, datos):
        datos_unicos = set()
        todos_numeros = True
        for dato, cantidad in datos:
            try:
                 dato = float(dato) if '.' in dato else int(dato)
            except ValueError:
                self.son_numeros = False
                break
            
            if isinstance(dato, (int, float)):
                datos_unicos.add(dato)
            else:
                todos_numeros = False
                break

        if todos_numeros:
            return datos_unicos,todos_numeros
        else:
            return None
    
    def contar_datos(self, datos):
        datos_numericos = []
        datos_no_numericos = []
        for dato,frecuencia in datos:
            try:
                if '.' in dato:
                    dato_num = float(dato)
                else:
                    dato_num = int(dato)
                datos_numericos.append((dato_num, int(frecuencia)))
            except ValueError:
                datos_no_numericos.append((dato, int(frecuencia)))

        todos_numericos = all(isinstance(dato, (int, float)) for dato, _ in datos_numericos)
        return datos_numericos, datos_no_numericos, todos_numericos

    def calcular_medidas_tencia_central(self, datos):
       datos_numericos, datos_no_numericos,todos_numericos = self.contar_datos(datos)

       if todos_numericos and datos_numericos :
           datos_completos = [dato for dato, frecuencia in datos_numericos for _ in range(frecuencia)]

           cantidad_datos_unicos = len(set(datos_completos))
           cantidad_datos_ingresados = len(datos_completos)
           
           enteros = all(isinstance(dato, int) for dato in datos_completos)

           if enteros:
               # Calcular la media aritmética redondeando a enteros
               suma = sum(dato * frecuencia for dato, frecuencia in datos_numericos)
               total_frecuencia = sum(frecuencia for _, frecuencia in datos_numericos)
               media_aritmetica = suma // total_frecuencia  # Redondear a entero

               # Calcular la mediana para datos enteros
               # Ordenar los datos por dato
               datos_ordenados = sorted(datos_numericos, key=lambda x: x[0])
               
               # Expander los datos según sus frecuencias
               datos_expandidos = []
               for dato, frecuencia in datos_ordenados:
                   datos_expandidos.extend([dato] * frecuencia)
               
               # Calcular la mediana
               n = len(datos_expandidos)
               if n % 2 == 1:
                   mediana = datos_expandidos[n // 2]
               else:
                   mediana = (datos_expandidos[n // 2 - 1] + datos_expandidos[n // 2]) // 2  # Redondear a entero
                
                  # Calcular medidas de dispersión
                  
               datos_ordenados = sorted(datos_numericos, key=lambda x: x[0])
               rango = datos_ordenados[-1][0] - datos_ordenados[0][0]

               media = media_aritmetica
               desviacion_media_absoluta = sum(abs(dato - media) * frecuencia for dato, frecuencia in datos_numericos) / total_frecuencia

               varianza = sum(((dato - media) ** 2) * frecuencia for dato, frecuencia in datos_numericos) / total_frecuencia
               desviacion_estandar = varianza ** 0.5

               coeficiente_variacion = (desviacion_estandar / media) * 100

           else:
               pass
           
           # Calcular la moda
           frecuencia_datos = Counter(datos_completos)
           max_frecuencia = max(frecuencia_datos.values())
           modas = [dato for dato, frecuencia in frecuencia_datos.items() if frecuencia == max_frecuencia]

           if len(modas) == 1:
               m = modas[0]
           else:
               m = modas
       return cantidad_datos_unicos, cantidad_datos_ingresados, media_aritmetica, mediana, m, rango, desviacion_media_absoluta, desviacion_estandar, coeficiente_variacion
    




    def obtener_datos_ordenados (self, datos):
        self.datos_ordenados = sorted(datos, key=lambda x: x[0])
        return self.datos_ordenados

    def calcular_datos(self, datos_ordenados):
        print("datos en calcular_datos:", datos_ordenados)  # Verifica los datos obtenidos

        if not datos_ordenados:
            return []  # Retorna una lista vacía si no hay datos

        datos_totales = sum((int(dato[1])) for dato in datos_ordenados)
        frecuencia_acumulada = 0
        tabla_datos = []

        for dato, frecuencia in datos_ordenados:
            frecuencia = int(frecuencia)
            frecuencia_acumulada += frecuencia
            frecuencia_relativa = frecuencia / datos_totales
            frecuencia_acumulada_relativa = frecuencia_acumulada / datos_totales

            tabla_datos.append((dato, frecuencia, frecuencia_acumulada, 
                                f"{frecuencia_relativa:.2%}", 
                                f"{frecuencia_acumulada_relativa:.2%}"))

        return tabla_datos


    def insertar_datos(self,datos_ordenados):
        self.tabla.limpiar_tabla()
        datos = self.calcular_datos(datos_ordenados)
        print("datos insertar:", datos)
        for dato, frecuencia, frecuencia_acumulada, frecuencia_relativa, frecuencia_acumulada_relativa in datos:
            self.tabla.tree.insert("", "end",text = str(dato) ,values=( frecuencia, frecuencia_acumulada, frecuencia_relativa, frecuencia_acumulada_relativa))

    
    def obtener_datos_para_graficar(self):
        datos_ordenados = self.datos_ordenados
        if datos_ordenados:
            datos_totales = [(dato, int(frecuencia)) for dato, frecuencia in datos_ordenados]
            return datos_totales
        return None 

    def calcular_intervalos(self, datos,num_clases):

        datos_expandidos = []
        for dato, frecuencia in datos:
            dato = float(dato)  # Convertir el dato a flotante
            frecuencia = int(frecuencia)  # Convertir la frecuencia a entero
            datos_expandidos.extend([dato] * frecuencia)

        min_dato = min(datos_expandidos)
        max_dato = max(datos_expandidos)

        # Calcular la anchura del intervalo
        rango = max_dato - min_dato + 1
        anchura_intervalo = (rango // num_clases) + (1 if rango % num_clases != 0 else 0)

        # Crear los intervalos
        intervalos = [(min_dato + i * anchura_intervalo, min_dato + (i + 1) * anchura_intervalo - 1) for i in range(num_clases)]

        # Asignar los datos a los intervalos
        datos_clasificados = [[] for _ in range(num_clases)]
        for dato in datos_expandidos:
            for i, (inicio, fin) in enumerate(intervalos):
                if inicio <= dato <= fin:
                    datos_clasificados[i].append(dato)
                    break

        return intervalos, datos_clasificados
        

    def agrupar_por_clases(self, datos):
        cantidad_datos = sum(int(cantidad) for dato, cantidad in datos)
        num_clases = self.tabla.mostrar_mensaje_pregunta("¿Cuantas clases deseas ? (ingresa 0 para salir)") 

        if num_clases is None or num_clases == 0:
            return
        
        if  cantidad_datos >= num_clases:
            intervalos,datos_clasificados = self.calcular_intervalos(datos, num_clases)
            
             # Calcular la tabla de frecuencias para los intervalos
            tabla_intervalos = []
            frecuencia_acumulada = 0

            for i, (inicio, fin) in enumerate(intervalos):
                datos_intervalo = datos_clasificados[i]
                frecuencia = len(datos_intervalo)
                frecuencia_acumulada += frecuencia
                frecuencia_relativa = frecuencia / cantidad_datos
                frecuencia_acumulada_relativa = frecuencia_acumulada / cantidad_datos
                marca_clase = (inicio + fin) / 2

                tabla_intervalos.append((f"{inicio} - {fin}", marca_clase, frecuencia, 
                                         frecuencia_acumulada, 
                                         f"{frecuencia_relativa:.2%}", 
                                         f"{frecuencia_acumulada_relativa:.2%}"))
            
            return tabla_intervalos
    


    def guar_dar_tabla(self):
        datos = []
        for item in self.tabla.tree.get_children():
            dato = self.tabla.tree.item(item, 'text')
            valores = self.tabla.tree.item(item, 'values')
            datos.append((dato,) + valores)

        nombre_archivo = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
        if nombre_archivo:
            self.modelo.guardar_datos_excel(datos, nombre_archivo, self.tabla.con_clases)
            messagebox.showinfo("Guardar", f"Datos guardados en {nombre_archivo} con éxito")
        

    def controlador_salir(self):
        self.tabla.app.ventana.quit()

    def controlador_volver(self):
        self.tabla.app.mostrar_marco(self.tabla.app.marco_datos.frame)

    def controlador_volver_menu(self):
        self.tabla.app.mostrar_marco(self.tabla.app.marco_menu.frame)
        self.tabla.app.m()