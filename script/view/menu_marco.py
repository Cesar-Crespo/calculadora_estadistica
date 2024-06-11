from script.controllers.controlador_menu import ControladorMenu

from tkinter import *
from PIL import Image,ImageTk

class MarcoMenu:
    def __init__(self, app) :
        self.controlador= ControladorMenu(self)
        self.app = app
        self.frame = Frame(self.app.ventana)
        self.titulo = Label(self.frame,text="CALCULADORA ESTADISTICA", font=('Arial',35,'bold'),bg="lightgrey",bd=8,relief=GROOVE)
        self.titulo.pack(side=TOP,fill=X)

        self.menu_lateral = Frame(self.frame,bg="#689FD3",width=150)
        self.menu_lateral.pack(side=LEFT,fill='both',expand=False)

        self.cuerpo_principal = Frame(self.frame,bg='#f1faff')
        self.cuerpo_principal.pack(side=RIGHT,fill='both',)

        self.img_o = Image.open('img/logo.png')
        self.img_r = self.img_o.resize((800,700))
        self.img = ImageTk.PhotoImage(self.img_r) 
        self.img_lb = Label(self.cuerpo_principal, image=self.img)
        self.img_lb.image = self.img
        self.img_lb.pack()

        #==========================Botones del menu====================================

        self.boton_nuevo_estudio = Button(self.menu_lateral, text="NUEVO ESTUDIO",bg="yellow",
                                 width=15,command=lambda: self.__on_click_nuevo_estudio())
        self.boton_nuevo_estudio.grid()
        self.boton_nuevo_estudio.place(x=17,y=280)


        self.boton_salir = Button(self.menu_lateral, text="SALIR",bg="yellow",width=15,command= lambda: self.__on_click_salir())
        self.boton_salir.grid()
        self.boton_salir.place(x=17,y=370)

    def __on_click_salir(self):
        self.controlador.controlador_salir()

    def __on_click_nuevo_estudio(self):
        self.controlador.controlador_nuevo_estudio()
        