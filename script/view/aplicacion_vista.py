from script.view.menu_marco import MarcoMenu
from script.view.datos_marco import MarcoDatos
from script.view.tabla_marco import MarcoTabla
from tkinter import *
from tkinter import messagebox,ttk,font,filedialog

import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
import numpy as np


class Aplicacion :

    def __init__(self):

        self.ventana = Tk()
        self.ventana.title("CALCULADORA ESTADISTICA ")
        self.ventana.geometry("970x675")
        self.ventana.resizable(False,False)

        # Configurar la ventana principal para que se expanda
        self.ventana.rowconfigure(0, weight=1)
        self.ventana.columnconfigure(0, weight=1)

        self.marco_menu = MarcoMenu(self)
        self.marco_datos = MarcoDatos(self)
        self.marco_tabla = MarcoTabla(self)

        self.marco_menu.frame.grid(row=0, column=0, sticky="nsew")
        self.marco_datos.frame.grid(row=0, column=0, sticky="nsew")
        self.marco_tabla.frame.grid(row=0,column=0,sticky="nsew")
        self.mostrar_marco(self.marco_menu.frame)

    def mostrar_marco(self, marco):
        marco.tkraise()

    def iniciar(self):
        self.ventana.mainloop()

    def enviar_datos_a_tabla(self, datos, estudio):
        self.marco_tabla.mostrar_datos(datos,estudio)
        self.mostrar_marco(self.marco_tabla.frame)

    def m(self):
        self.marco_datos.borrar_combobox()
        self.marco_datos.borrar_datos_guardados()
        self.marco_datos.limpiar_entrada_nombre_estudio()
        self.marco_datos.limpiar_combobox()
        self.marco_datos.limpiar_entradas_datos()