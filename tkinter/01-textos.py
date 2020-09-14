from tkinter import *

ventana = Tk()
ventana.geometry("500x500")
# cargar textos
texto = Label(ventana, text="hola")
texto.config(fg="#ee8822",
             bg="black",
             padx=50,
             pady=20,
             font=("Roboto", 30))
# empaquetar para mostrar
texto.pack()

def prubas(nombre):
    return f"hola {nombre}"

texto = Label(ventana, text=prubas(nombre="lodi"))
# empaquetar para mostrar
texto.config(
    font=("Roboto", 30))

texto.pack(anchor=W)

ventana.mainloop()
