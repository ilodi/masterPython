# Tkinter
# Modulo para crear interfaces graficas de usuario

from tkinter import *
import os.path


class Programa:
    def __init__(self):
        self.title = "Master en python"
        self.icon = "./imagenes/logotipo.ico"
        self.icon_alt = "./tkinter/imagenes/logotipo.ico"
        self.size = "770x450"
        self.resizable = False

    def cargar(self):
        # crear la ventana raiz
        ventana = Tk()
        self.ventana = ventana

        # titlo de la ventan
        ventana.title(self.title)
        # comprobar si existe un archivo
        ruta_icon = os.path.abspath(self.icon)
        # si no encuntra la ruta del icono
        if not os.path.isfile(ruta_icon):
            ruta_icon = os.path.abspath(self.icon_alt)
        # Icon de la ventana
        ventana.iconbitmap(ruta_icon)
        # Mostrar texto dento del programa
        text = Label(ventana, text=ruta_icon)
        # empaquetar a la ventana
        text.pack()
        # Cambio en el tamaño de la ventana
        ventana.geometry(self.size)
        # bloquear el tamaño de la ventana
        if self.resizable:
            ventana.resizable(1, 1)
        else:
            ventana.resizable(0, 0)

    def sefTitle(self, title):
        self.title = title

    def addText(self,dato):
        texto = Label(self.ventana, text=dato)
        texto.pack()

    def mostrar(self):
        self.ventana.mainloop()


# Intanciar mi programa
programa = Programa()

programa.cargar()

programa.addText('Soy un texto')
programa.mostrar()