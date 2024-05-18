from tkinter import * #todo esto fue una prueba fallida para asignar los botones funcionales
import triangulos

z=0



ventana=Tk()
ventana.geometry('300x300')


entrada1= Entry(ventana,font='arial 20')
entrada1.grid(row=0, column=0, columnspan=4, padx=20, pady=5)


def click_boton(valor):
    global z
    entrada1.insert(z, valor)
    z += 1

def borrar():
    entrada1.delete(0,END)

def operaciones():
    ecuacion=entrada1.get()
    resultado=eval(ecuacion)
    entrada1.delete(0,END)
    entrada1.insert(0, resultado)
    z=0

boton_1=Button(ventana, text="1", width=5, heigth=2, command=triangulos.circulo)




ventana.mainloop()