#from tkinter import * # Importa el módulo
#def centrar(ventana):
#    ventana.update_idletasks()
 #   w=ventana.winfo_width()
#    h=ventana.winfo_height()
#    extraW=ventana.winfo_screenwidth()-w
#    extraH=ventana.winfo_screenheight()-h
#    ventana.geometry("%dx%d%+d%+d" % (w,h,extraW/2,extraH/2))
#def mostrar(ventana):
#    ventana.deiconify()
#def ocultar(ventana):
#    ventana.withdraw()
#def ejecutar(f): v0.after(200,f) # Una forma alternativa de ejecutar una función
#v0 = Tk() # Tk() Es la ventana principal
#v0.config(bg="black") # Le da color al fondo
#v0.geometry("500x500") # Cambia el tamaño de la ventana
#b1=Button(v0,text="ABRIR VENTANA V1",command=lambda:
#    ejecutar(mostrar(v1))) # Primer botón
#b1.grid(row=1,column=1) # El botón es cargado
#b2=Button(v0,text="OCULTAR VENTANA V1",command=lambda:
#    ejecutar(ocultar(v1))) # Segundo botón
#b2.grid(row=1,column=2) # El botón es cargado
#v1=Toplevel(v0) # Crea una ventana hija
#v1.withdraw() # oculta v1
#v0.mainloop() # Es el evento que llama al inicio de nuestro programa.
#Siempre lo lleva la ventana principal.


#  creo las funciones para las operaciones

def sumar(n1,n2):
    return n1 + n2
def restar(n1, n2):
    return n1-n2
def multiplicar(n1, n2):
    return n1*n2
def dividir(n1,n2):
    try:
        return n1/n2
    except:
        print("no se puede dividir por cero ")
def potencia():
    n=int(input("ingrese el numero a elevar: "))
    x=int (input("ingrese la ponencia: "))
    i=1
    r=n
    while (i<x):
        r= r * n
        i=i+1
    return r

