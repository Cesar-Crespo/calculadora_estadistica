from script.controllers.controlador_tabla import ControladorTabla

from tkinter import *
from tkinter import ttk,font,simpledialog
import matplotlib.pyplot as plt

class MarcoTabla:

    def __init__(self, app) :
            self.controlador = ControladorTabla(self)
            self.con_clases = False
            self.app = app
            self.frame = Frame(self.app.ventana)

            self.titulo = Label(self.frame,text="CALCULADORA ESTADISTICA", font=('Arial',35,'bold'),bg="lightgrey",bd=8,relief=GROOVE)
            self.titulo.pack(side=TOP,fill=X)

            self.cuerpo_tabla_frecuencia = Frame(self.frame,bg='#f1faff')
            self.cuerpo_tabla_frecuencia.pack(expand=True,fill='both')

            self.lbl_menu_opciones_tabla = LabelFrame(self.cuerpo_tabla_frecuencia,bd=5,text="Opciones",bg="lightgrey",font=('Arial',15))
            self.lbl_menu_opciones_tabla.place(x=5,y=15,width=150,height=570)

            self.btn_info = Button(self.lbl_menu_opciones_tabla,bd=5,text="INFORMACION",font=('Arial',12),bg="lightgrey", command= lambda: self.informacion_adicional())
            self.btn_info.grid(row=0,column= 0,padx=5,pady=7)
            
            self.btn_barras = Button(self.lbl_menu_opciones_tabla,bd=5,text="G. BARRAS",bg="lightgrey",font=("Arial",12), command = lambda: self.grafico_barras())
            self.btn_barras.grid(row=1,column=0,padx=5,pady=7)

            self.btn_tortas = Button(self.lbl_menu_opciones_tabla,bd=5,text="G. TORTAS",bg="lightgrey",font=("Arial",12), command= lambda: self.grafico_tortas())
            self.btn_tortas.grid(row=2,column=0,padx=5,pady=7)

            self.btn_poligonos = Button(self.lbl_menu_opciones_tabla,bd=5,text="G. POLIGONOS",bg="lightgrey",font=("Arial",12), command= lambda: self.grafico_poligono())
            self.btn_poligonos.grid(row=3,column=0,padx=5,pady=7)

            self.btn_clases = Button(self.lbl_menu_opciones_tabla,bd=5,text="clases",bg="lightgrey",font=("Arial",12), command= lambda: self.transformar_datos_a_clases())
            self.btn_clases.grid(row=4,column=0,padx=5,pady=7)

            self.btn_guardar = Button(self.lbl_menu_opciones_tabla,bd=5,text="GUARDAR",bg="lightgrey",font=("Arial",12), command= lambda: self.guardar_tabla())
            self.btn_guardar.grid(row=5,column=0,padx=5,pady=7)


            self.btn_volver_anterior = Button(self.lbl_menu_opciones_tabla,bd=5,text="ANTERIOR",bg="lightgrey",font=("Arial",12), command= lambda: self.ir_marco2())
            self.btn_volver_anterior.grid(row=6,column=0,padx=5,pady=7)

            self.btn_volver_menu = Button(self.lbl_menu_opciones_tabla,bd=5,text="MENU",bg="lightgrey",font=("Arial",12), command= lambda:  self.ir_menu())
            self.btn_volver_menu.grid(row=7,column=0,padx=5,pady=7)

            self.btn_salir = Button(self.lbl_menu_opciones_tabla,bd=5,text="SALIR",bg="lightgrey",font=("Arial",12), command= lambda:  self.__on_click_salir())
            self.btn_salir.grid(row=8,column=0,padx=5,pady=7)

            #==================================tabla=========================================================

            self.lbl_tabla_frecuencia = LabelFrame(self.cuerpo_tabla_frecuencia,bd=5,text="Tabla Frecuencia",bg="lightgrey",font=('Arial',15))
            self.lbl_tabla_frecuencia.place(x=180,y=15,width=780,height=570)



            # Crear el Treeview con scrollbar
            self.tree_frame = Frame(self.lbl_tabla_frecuencia)
            self.tree_frame.pack(expand=True, fill="both")

            self.tree_scroll = ttk.Scrollbar(self.tree_frame, orient="vertical")
            self.tree_scroll.pack(side="right", fill="y")

            self.tree = ttk.Treeview(self.tree_frame, yscrollcommand=self.tree_scroll.set)
            self.tree.pack(expand=True, fill="both")

            self.tree_scroll.config(command=self.tree.yview)

            self.tree["columns"] = ("Frecuencia", "Frecuencia Acumulada", "Frecuencia Relativa", "Frecuencia Acumulada Relativa")
            self.tree.heading("#0", text="Dato", anchor=W)
            self.tree.heading("Frecuencia", text="Frecuencia", anchor=W)
            self.tree.heading("Frecuencia Acumulada", text="Frecuencia Acumulada", anchor=W)
            self.tree.heading("Frecuencia Relativa", text="Frecuencia Relativa", anchor=W)
            self.tree.heading("Frecuencia Acumulada Relativa", text="Frecuencia Acumulada Relativa", anchor=W)

            self.tree.column("#0", anchor=W, width=100)
            self.tree.column("Frecuencia", anchor=W, width=100)
            self.tree.column("Frecuencia Acumulada", anchor=W, width=150)
            self.tree.column("Frecuencia Relativa", anchor=W, width=150)
            self.tree.column("Frecuencia Acumulada Relativa", anchor=W, width=150)

    def mostrar_mensaje_pregunta(self, mensaje):
        respuesta = simpledialog.askinteger("Confirmacion", mensaje)
        return  respuesta
    
    

    def mostrar_datos (self,datos,estudio):
        self.controlador.crear_tabla(datos)
        self.nombre_estudio = estudio
        self.datos = datos

    def limpiar_tabla(self):
        for row in  self.tree.get_children() :
            self.tree.delete(row)

    def __on_click_salir(self):
        self.controlador.controlador_salir()

    def ir_marco2(self):
        self.controlador.controlador_volver()

    def ir_menu(self):
        self.controlador.controlador_volver_menu()
        

    def grafico_barras(self):
        datos = self.controlador.obtener_datos_para_graficar()
        
        if datos:
            etiquetas, valores = zip(*datos)
            
            if self.con_clases:
                # Obtener marcas de clase si se usan clases
                datos_clases = self.controlador.agrupar_por_clases(self.datos)
                if datos_clases and len(datos_clases[0]) >= 6:  # Ajustar según la estructura devuelta
                    _, marcas_clase, _, _, _, _ = zip(*datos_clases)
                    print("Marcas de Clase:", marcas_clase)
                    print("Valores:", valores)
                    plt.bar(marcas_clase, valores)
                    plt.xlabel('Marcas de Clase')
                else:
                    raise ValueError("Estructura de datos de clases inesperada")
            else:
                print("Etiquetas:", etiquetas)
                print("Valores:", valores)
                plt.bar(etiquetas, valores)
                plt.xlabel('Datos')
            
            plt.ylabel('Frecuencia')
            plt.title('Gráfico de Barras')
            plt.show()
        else:
            print("No hay datos disponibles para graficar.")

    def grafico_tortas(self):
        datos = self.controlador.obtener_datos_para_graficar()
        if datos:
            etiquetas, valores = zip(*datos)
            if self.con_clases:
                _, marcas_clase, _, _, _, _ = zip(*self.controlador.agrupar_por_clases(self.datos))
                plt.pie(valores,labels=marcas_clase , autopct='%1.1f%%')

            else:
                plt.pie(valores, labels=etiquetas, autopct='%1.1f%%')
            
            plt.title('Gráfico de Tortas')
            plt.show()
            

    def grafico_poligono(self):
        datos = self.controlador.obtener_datos_para_graficar()
        if datos:
            etiquetas, valores = zip(*datos)
            if self.con_clases:
                _, marcas_clase, _, _, _, _ = zip(*self.controlador.agrupar_por_clases(self.datos))
                plt.plot(marcas_clase, valores, marker = 'o')
                plt.xlabel('Marca de clase')
            else:

                plt.plot(etiquetas, valores, marker='o')
                plt.xlabel('Datos')
            plt.ylabel('Frecuencia')
            plt.title('Polígono de Frecuencias')
            plt.grid(True)
            plt.show()
    
    
    def informacion_adicional(self):
        self.ventana_info = Toplevel()
        self.ventana_info.title("Informacion")
        self.ventana_info.geometry("600x400")
        # Configurar fuentes
        self.title_font =font.Font(family="Helvetica", size=20, weight="bold")
        self.label_font =font.Font(family="Helvetica", size=12, weight="bold")
        self.info_font = font.Font(family="Helvetica", size=12)

        # Contenedor principal
        self.container = Frame(self.ventana_info, bg='#ecf0f1', bd=2, relief="groove")
        self.container.pack(expand=True, padx=20, pady=20, fill=BOTH)

        title = Label(self.container, text="Informacion del estudio estadistico", font=self.title_font, bg='#2980b9', fg='white', pady=10)
        title.pack(fill=X)
        
        # Frame de información
        info_frame = Frame(self.container, bg='#ecf0f1')
        info_frame.pack(pady=20, fill=BOTH, expand=True)

        self.lbl_nombre_estudio = Label(info_frame, text="NOMBRE DEL ESTUDIO: ", font=self.label_font, bg='#ecf0f1', fg='#2c3e50', anchor='e')
        self.lbl_nombre_estudio.grid(row=0, column=0, sticky='e', pady=5, padx=(0, 10))

        self.get_nombre_estudio = Label(info_frame, text= self.nombre_estudio, font=self.info_font, bg='white', fg='#2c3e50', anchor='w', relief='solid', borderwidth=1, padx=10, pady=5)
        self.get_nombre_estudio.grid(row=0, column=1, sticky='w', pady=5, padx=(0, 10))

        cantidad_datos_unicos, cantidad_datos_ingresados, media_aritmetica, mediana , m ,rango, desviacion_media_absoluta, desviacion_estandar, coeficiente_variacion= self.controlador.calcular_medidas_tencia_central(self.datos)

        self.lbl_cantidad_datos_unicos = Label(info_frame, text="CANTIDAD DE DATOS UNICOS: ", font=self.label_font, bg='#ecf0f1', fg='#2c3e50', anchor='e')
        self.lbl_cantidad_datos_unicos.grid(row=2, column=0, sticky='e', pady=5, padx=(0, 10))

        self.get_cantidad_datos_unicos = Label(info_frame, text=cantidad_datos_unicos, font=self.info_font, bg='white', fg='#2c3e50', anchor='w', relief='solid', borderwidth=1, padx=10, pady=5)
        self.get_cantidad_datos_unicos.grid(row=2, column=1, sticky='w', pady=5, padx=(0, 10))

        self.lbl_total_datos = Label(info_frame, text="CANTIDAD DE DATOS INGRESADOS: ", font=self.label_font, bg='#ecf0f1', fg='#2c3e50', anchor='e')
        self.lbl_total_datos.grid(row=3, column=0, sticky='e', pady=5, padx=(0, 10))

        self.get_total_datos = Label(info_frame, text=cantidad_datos_ingresados, font=self.info_font, bg='white', fg='#2c3e50', anchor='w', relief='solid', borderwidth=1, padx=10, pady=5)
        self.get_total_datos.grid(row=3, column=1, sticky='w', pady=5, padx=(0, 10))
            
        self.lbl_media_aritmetica = Label(info_frame, text="MEDIA ARITMETICA: ", font=self.label_font, bg='#ecf0f1', fg='#2c3e50', anchor='e')
        self.lbl_media_aritmetica.grid(row=4, column=0, sticky='e', pady=5, padx=(0, 10))

        self.get_media_aritmetica = Label(info_frame, text=media_aritmetica, font=self.info_font, bg='white', fg='#2c3e50', anchor='w', relief='solid', borderwidth=1, padx=10, pady=5)
        self.get_media_aritmetica.grid(row=4, column=1, sticky='w', pady=5, padx=(0, 10))

        self.lbl_mediana = Label(info_frame, text="MEDIANA: ", font=self.label_font, bg='#ecf0f1', fg='#2c3e50', anchor='e')
        self.lbl_mediana.grid(row=5, column=0, sticky='e', pady=5, padx=(0, 10))

        self.get_mediana = Label(info_frame, text=mediana, font=self.info_font, bg='white', fg='#2c3e50', anchor='w', relief='solid', borderwidth=1, padx=10, pady=5)
        self.get_mediana.grid(row=5, column=1, sticky='w', pady=5, padx=(0, 10))

        self.lbl_moda = Label(info_frame, text="MODA: ", font=self.label_font, bg='#ecf0f1', fg='#2c3e50', anchor='e')
        self.lbl_moda.grid(row=6, column=0, sticky='e', pady=5, padx=(0, 10))

        self.get_moda = Label(info_frame, text=m, font=self.info_font, bg='white', fg='#2c3e50', anchor='w', relief='solid', borderwidth=1, padx=10, pady=5)
        self.get_moda.grid(row=6, column=1, sticky='w', pady=5, padx=(0, 10))

        self.lbl_rango = Label(info_frame, text="RANGO: ", font=self.label_font, bg='#ecf0f1', fg='#2c3e50', anchor='e')
        self.lbl_rango.grid(row=7, column=0, sticky='e', pady=5, padx=(0, 10))

        self.get_rango = Label(info_frame, text=rango, font=self.info_font, bg='white', fg='#2c3e50', anchor='w', relief='solid', borderwidth=1, padx=10, pady=5)
        self.get_rango.grid(row=7, column=1, sticky='w', pady=5, padx=(0, 10))

        self.lbl_desviacion_media_absoluta = Label(info_frame, text="DESVIACION MEDIA ABSOLUTA: ", font=self.label_font, bg='#ecf0f1', fg='#2c3e50', anchor='e')
        self.lbl_desviacion_media_absoluta.grid(row=8, column=0, sticky='e', pady=5, padx=(0, 10))

        self.get_desviacion_media_absoluta = Label(info_frame, text=desviacion_media_absoluta, font=self.info_font, bg='white', fg='#2c3e50', anchor='w', relief='solid', borderwidth=1, padx=10, pady=5)
        self.get_desviacion_media_absoluta.grid(row=8, column=1, sticky='w', pady=5, padx=(0, 10))

        self.lbl_desviacion_estandar = Label(info_frame, text="DESVIACION ESTANDAR: ", font=self.label_font, bg='#ecf0f1', fg='#2c3e50', anchor='e')
        self.lbl_desviacion_estandar.grid(row=9, column=0, sticky='e', pady=5, padx=(0, 10))

        self.get_desviacion_estandar = Label(info_frame, text=desviacion_estandar, font=self.info_font, bg='white', fg='#2c3e50', anchor='w', relief='solid', borderwidth=1, padx=10, pady=5)
        self.get_desviacion_estandar.grid(row=9, column=1, sticky='w', pady=5, padx=(0, 10))

        self.lbl_coeficiente_variacion = Label(info_frame, text="COEFICIENTE VARIACION: ", font=self.label_font, bg='#ecf0f1', fg='#2c3e50', anchor='e')
        self.lbl_coeficiente_variacion.grid(row=10, column=0, sticky='e', pady=5, padx=(0, 10))

        self.get_coeficiente_variacion = Label(info_frame, text=coeficiente_variacion, font=self.info_font, bg='white', fg='#2c3e50', anchor='w', relief='solid', borderwidth=1, padx=10, pady=5)
        self.get_coeficiente_variacion.grid(row=10, column=1, sticky='w', pady=5, padx=(0, 10))



 

    def encabezados_clases(self, tabla_intervalos):
        # tabla_intervalos = self.controlador.agrupar_por_clases(datos)
        self.limpiar_tabla()
        self.tree["columns"] = ("marca de clase", "frecuencia", "frecuencia acumulada", "frecuencia relativa", "frecuencia acumulada relativa")
        
        self.tree.heading("#0", text="Intervalo")
        self.tree.heading("marca de clase", text="Marca de Clase")
        self.tree.heading("frecuencia", text="Frecuencia")
        self.tree.heading("frecuencia acumulada", text="Frecuencia Acumulada")
        self.tree.heading("frecuencia relativa", text="Frecuencia Relativa")
        self.tree.heading("frecuencia acumulada relativa", text="Frecuencia Acumulada Relativa")
        
        self.tree.column("#0", anchor='w', width=80)
        self.tree.column("marca de clase", anchor='w', width=100)
        self.tree.column("frecuencia", anchor='w', width=100)
        self.tree.column("frecuencia acumulada", anchor='w', width=150)
        self.tree.column("frecuencia relativa", anchor='w', width=150)
        self.tree.column("frecuencia acumulada relativa", anchor='w', width=140)
        
        for intervalo, marca_clase, frecuencia, frecuencia_acumulada, frecuencia_relativa, frecuencia_acumulada_relativa in tabla_intervalos:
            self.tree.insert("", "end", text=str(intervalo), values=(marca_clase, frecuencia, frecuencia_acumulada, frecuencia_relativa, frecuencia_acumulada_relativa))

        

    def transformar_datos_a_clases(self):
        tabla_intervalos = self.controlador.agrupar_por_clases(self.datos)
        self.encabezados_clases(tabla_intervalos)
        self.con_clases = True

    def guardar_tabla (self):
        self.controlador.guar_dar_tabla()
        

        



