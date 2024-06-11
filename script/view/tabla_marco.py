from script.controllers.controlador_tabla import ControladorTabla

from tkinter import *
from tkinter import ttk


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

            self.btn_info = Button(self.lbl_menu_opciones_tabla,bd=5,text="INFORMACION",font=('Arial',12),bg="lightgrey",  command=lambda: self.informacion_adicional(self.app.marco2.entry_nombre_estudio.get(), self.app.marco2.datos))
            self.btn_info.grid(row=0,column= 0,padx=5,pady=7)
            
            self.btn_barras = Button(self.lbl_menu_opciones_tabla,bd=5,text="G. BARRAS",bg="lightgrey",font=("Arial",12), command = lambda: self.grafico_barras())
            self.btn_barras.grid(row=1,column=0,padx=5,pady=7)

            self.btn_tortas = Button(self.lbl_menu_opciones_tabla,bd=5,text="G. TORTAS",bg="lightgrey",font=("Arial",12), command= lambda: self.grafico_tortas())
            self.btn_tortas.grid(row=2,column=0,padx=5,pady=7)

            self.btn_poligonos = Button(self.lbl_menu_opciones_tabla,bd=5,text="G. POLIGONOS",bg="lightgrey",font=("Arial",12), command= lambda: self.graficar_poligono())
            self.btn_poligonos.grid(row=3,column=0,padx=5,pady=7)

            self.btn_guardar = Button(self.lbl_menu_opciones_tabla,bd=5,text="GUARDAR",bg="lightgrey",font=("Arial",12), command= lambda: self.guardar_tabla())
            self.btn_guardar.grid(row=4,column=0,padx=5,pady=7)


            self.btn_volver_anterior = Button(self.lbl_menu_opciones_tabla,bd=5,text="ANTERIOR",bg="lightgrey",font=("Arial",12), command= lambda: self.ir_marco2())
            self.btn_volver_anterior.grid(row=5,column=0,padx=5,pady=7)

            self.btn_volver_menu = Button(self.lbl_menu_opciones_tabla,bd=5,text="MENU",bg="lightgrey",font=("Arial",12), command= lambda:  self.ir_menu())
            self.btn_volver_menu.grid(row=6,column=0,padx=5,pady=7)

            self.btn_salir = Button(self.lbl_menu_opciones_tabla,bd=5,text="SALIR",bg="lightgrey",font=("Arial",12), command= lambda:  self.__on_click_salir())
            self.btn_salir.grid(row=7,column=0,padx=5,pady=7)

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

    def __on_click_salir(self):
        self.controlador.controlador_salir()

    def ir_marco2(self):
        self.controlador.controlador_volver()

    def ir_menu(self):
        self.controlador.controlador_volver_menu()