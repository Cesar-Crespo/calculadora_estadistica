from script.controllers.controlador_ingreso_datos import ControladorDatos
from tkinter import *
from tkinter import ttk,messagebox

class MarcoDatos:

    def __init__(self, app) :
        self.controlador = ControladorDatos(self)
        self.app = app
        self.frame = Frame(self.app.ventana)
    
        self.titulo = Label(self.frame,text="CALCULADORA ESTADISTICA", font=('Arial',35,'bold'),bg="lightgrey",bd=8,relief=GROOVE)
        self.titulo.pack(side=TOP,fill=X)

        self.cuerpo_ingreso_datos = Frame(self.frame,bg='#f1faff')
        self.cuerpo_ingreso_datos.pack(expand=True,fill='both')

        self.cuerpo_estudio = LabelFrame(self.cuerpo_ingreso_datos,text="INGRESE LOS DATOS PARA EL ESTUDIO",font=("Arial",15),background="lightgrey",bd=7,relief=GROOVE) 
        self.cuerpo_estudio.place(x=20,y=25,width=470,height=550)

        self.lbl_nombre_estudio = Label(self.cuerpo_estudio,text="Nombre del estudio ",font=('Arial',15),bg="lightgrey")
        self.lbl_nombre_estudio.grid(row=0,column=0,padx=2,pady=4)

        self.entry_nombre_estudio = Entry(self.cuerpo_estudio,bd=5,font=('Arial',15))
        self.entry_nombre_estudio.grid(row=0,column=1,padx=2,pady=4)

        self.lbl_dato = Label(self.cuerpo_estudio,text="Dato",font=('Arial',15),bg="lightgrey")
        self.lbl_dato.grid(row=1,column=0,padx=2,pady=4)

        self.entry_dato = Entry(self.cuerpo_estudio,bd=5,font=('Arial',15))
        self.entry_dato.grid(row=1,column=1,padx=2,pady=4)

        self.lbl_cantidad_del_dato = Label(self.cuerpo_estudio,text="Cantidad del dato ",font=('Arial',15),bg="lightgrey")
        self.lbl_cantidad_del_dato.grid(row=2,column=0,padx=2,pady=4)

        self.entry_cantidad_dato = Entry(self.cuerpo_estudio,bd=5,font=('Arial',15))
        self.entry_cantidad_dato.grid(row=2,column=1,padx=2,pady=4)

        self.lbl_buscar_dato_guardado = Label(self.cuerpo_estudio,text="Buscar dato guardado",font=('Arial',15),bg="lightgrey")
        self.lbl_buscar_dato_guardado.grid(row=3,column=0,padx=2,pady=2)

        self.seleccion_dato_combobox = ttk.Combobox(self.cuerpo_estudio, state="readonly")
        self.seleccion_dato_combobox.grid(row=3,column=1,padx=10,pady=10)

        #=================================bBotones===========================================

        self.lbl_cuerpo_opciones = LabelFrame(self.cuerpo_estudio,bd=5,text="Opciones",bg="lightgrey",font=('Arial',15))
        self.lbl_cuerpo_opciones.place(x=20,y=300,width=415,height=200)

        self.agregar_btn = Button(self.lbl_cuerpo_opciones,bd=3,text="Agregar",font=('Arial',12),width=12,height=3,command=lambda: self.__on_click_btn_agregar())
        self.agregar_btn.grid(row=0,column=0,padx=7,pady=2)

        self.modificar_btn = Button(self.lbl_cuerpo_opciones,bd=3,text="Modificar",font=('Arial',12),width=12,height=3,command=lambda: self.__on_click_btn_modificar())
        self.modificar_btn.grid(row=0,column=1,padx=7,pady=2)

        self.eliminar_btn = Button(self.lbl_cuerpo_opciones,bd=3,text="Eliminar",font=('Arial',12),width=12,height=3,command=lambda: self.__on_click_btn_eliminar())
        self.eliminar_btn.grid(row=0,column=2,padx=7,pady=2)

        self.volver_menu_btn = Button(self.lbl_cuerpo_opciones,bd=3,text="Volver",font=('Arial',12),width=12,height=3,command=lambda: self.__on_click_btn_volver())
        self.volver_menu_btn.grid(row=1,column=0,columnspan=1,padx=7,pady=12)

        self.enviar_btn = Button(self.lbl_cuerpo_opciones,bd=3,text="ENVIAR DATOS",font=('Arial',12),width=27,height=3,command=lambda: self.__on_click_btn_enviar_datos())
        self.enviar_btn.grid(row=1 ,column = 1,columnspan=2 ,padx= 7 ,pady=12)

        #_______________________________mostrando datos__________________________________________

        self.cuerpo_mostrar_datos = LabelFrame(self.cuerpo_ingreso_datos,text="DATOS GUARDADDOS DEL ESTUDIO",font=("Arial",15),background="lightgrey",bd=7,relief=GROOVE) 
        self.cuerpo_mostrar_datos.place(x=500,y=25,width=450,height=550)

        self.etiqueta_mostrar_datos_guardados =Label(self.cuerpo_mostrar_datos, text="",font=("Arial",12))
        self.etiqueta_mostrar_datos_guardados.grid(row=0, columnspan=2, padx=10, pady=5)
    
    def borrar_datos_m (self):
        self.controlador.limpiar_datos()
    def obtener_dato(self):
        return self.entry_dato.get()
    
    def obtener_cantidad_dato(self):
        return self.entry_cantidad_dato.get()
    
    def obtener_nombre_estudio(self):
        return self.entry_nombre_estudio.get()
    
    def limpiar_entradas_datos(self):
        self.entry_dato.delete(0, END)
        self.entry_cantidad_dato.delete(0, END)

    def limpiar_entrada_nombre_estudio(self):
        self.entry_nombre_estudio.delete(0, END)

    def limpiar_combobox(self):
        self.seleccion_dato_combobox.set("")

    def actualizar_datos_guardados(self, datos):
        self.etiqueta_mostrar_datos_guardados.config(text="\n".join([f"Nombre : {nombre}, Cantidad : {cantidad}" for nombre, cantidad in datos]))
    
    def borrar_datos_guardados(self):
        self.etiqueta_mostrar_datos_guardados.config(text="")

    def actualizar_combobox(self, datos):
        self.seleccion_dato_combobox['values'] = [nombre for nombre, _ in datos]

    def borrar_combobox(self):
        self.seleccion_dato_combobox['values'] = []

    def mostrar_mensaje_error(self, mensaje):
        messagebox.showerror("Error", mensaje)

    def mostrar_mensaje_informacion(self, mensaje):
        messagebox.showinfo("Informacion", mensaje)

    def mostrar_mensaje_confirmacion(self, mensaje):
        respuesta = messagebox.askyesno("Confirmacion", mensaje)
        return  respuesta

    def __on_click_btn_agregar(self):
        self.controlador.agregar_dato()

    def __on_click_btn_modificar(self):
        self.controlador.modificar_dato()

    def __on_click_btn_eliminar(self):
        self.controlador.eliminar_dato()

    def __on_click_btn_volver(self):
        self.limpiar_entrada_nombre_estudio()
        self.controlador.controlador_volver()

    def __on_click_btn_enviar_datos(self):
        self.controlador.enviar_datos()