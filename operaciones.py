from tkinter import *
def envia_boton(valor):
   anterior = pantalla.get()
   pantalla.delete(0, END)
   pantalla.insert(0, str(anterior) + str(valor))
def suma():
   global num1
   global operacion
   num1 = pantalla.get()
   num1 = float(num1)
   pantalla.delete(0,END)
   operacion = "+"
def resta():
    global num1
    global operacion
    num1 = pantalla.get()
    num1 = float(num1)
    pantalla.delete(0, END)
    operacion = "-"
def multiplicacion():
    global num1
    global operacion
    num1 = pantalla.get()
    num1 = float(num1)
    pantalla.delete(0, END)
    operacion = "*"
def division():
    global num1
    global operacion
    num1 = pantalla.get()
    num1 = float(num1)
    pantalla.delete(0, END)
    operacion = "/"
def borrar():
    pantalla.delete(0, END)
def borrar_uno():
    largo = len(pantalla.get())
    pantalla.delete(largo-1, END)
def igual():
    global num2
    num2 = pantalla.get()
    pantalla.delete(0, END)

    if operacion == "+":
        pantalla.insert(0, num1 + float(num2))
    if operacion == "-":
        pantalla.insert(0, num1 - float(num2))
    if operacion == "*":
        pantalla.insert(0, num1 * float(num2))
    if operacion == "/":
        pantalla.insert(0, num1 / float(num2))

root = Tk()
root.title("Calculadora básica")
root.resizable(0, 0)
pantalla = Entry(root,
               width=22,
               bg="black",
               fg="white",
               borderwidth=0,
               justify=RIGHT,
               font=('arial', 18, 'bold'))

pantalla.grid(row=0, padx=2, pady=2, columnspan=4)


boton_1 = Button(root,text="1",
               width=9,
               height=3,
               bg="white",
               fg="red",
               borderwidth=0,
               cursor="hand2",command=lambda: envia_boton(1)).grid(row=1, column=0, padx=1, pady=1)

boton_2 = Button(root,text="2",
               width=9,
               height=3,
               bg="white",
               fg="red",
               borderwidth=0,
               cursor="hand2",
               command=lambda: envia_boton(2)).grid(row=1, column=1, padx=1, pady=1)

boton_3 = Button(root,text="3",
               width=9,
               height=3,
               bg="white",
               fg="red",
               borderwidth=0,
               cursor="hand2",
               command=lambda: envia_boton(3)).grid(row=1, column=2, padx=1, pady=1)

boton_4 = Button(root,text="4",
               width=9,
               height=3,
               bg="white",
               fg="red",
               borderwidth=0,
               cursor="hand2",
               command=lambda: envia_boton(4)).grid(row=2, column=0, padx=1, pady=1)

boton_5 = Button(root,text="5",
               width=9,
               height=3,
               bg="white",
               fg="red",
               borderwidth=0,
               cursor="hand2",
               command=lambda: envia_boton(5)).grid(row=2, column=1, padx=1, pady=1)

boton_6 = Button(root,text="6",
               width=9,
               height=3,
               bg="white",
               fg="red",
               borderwidth=0,
               cursor="hand2",
               command=lambda: envia_boton(6)).grid(row=2, column=2, padx=1, pady=1)

boton_7 = Button(root,text="7",
               width=9,
               height=3,
               bg="white",
               fg="red",
               borderwidth=0,
               cursor="hand2",
               command=lambda: envia_boton(7)).grid(row=3, column=0, padx=1, pady=1)

boton_8 = Button(root,text="8",
               width=9,
               height=3,
               bg="white",
               fg="red",
               borderwidth=0,
               cursor="hand2",
               command=lambda: envia_boton(8)).grid(row=3, column=1, padx=1, pady=1)

boton_9 = Button(root,text="9",
               width=9,
               height=3,
               bg="white",
               fg="red",
               borderwidth=0,
               cursor="hand2",
               command=lambda: envia_boton(9)).grid(row=3, column=2, padx=1, pady=1)


boton_igual = Button(root,text="=",
               width=20,
               height=3,
               bg="red",
               fg="white",
               borderwidth=0,
               cursor="hand2",
               command=igual).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

boton_punto = Button(root,text=".",
               width=9,
               height=3,
               bg="spring green",
               fg="black",
               cursor="hand2",
               borderwidth=0,
               command=lambda: envia_boton(".")).grid(row=4, column=2, padx=1, pady=1)

boton_mas = Button(root,text="+",
               width=9,
               height=3,
               bg="deep sky blue",
               fg="black",
               borderwidth=0,
               cursor="hand2",
               command=suma).grid(row=1, column=3, padx=1, pady=1)

boton_menos = Button(root,text="-",
               width=9,
               height=3,
               bg="deep sky blue",
               fg="black",
               borderwidth=0,
               cursor="hand2",
               command=resta).grid(row=2, column=3, padx=1, pady=1)

boton_multiplicacion = Button(root,text="*",
               width=9,
               height=3,
               bg="deep sky blue",
               fg="black",
               borderwidth=0,
               cursor="hand2",
               command=multiplicacion).grid(row=3, column=3, padx=1, pady=1)

boton_division = Button(root,text="/",
               width=9,
               height=3,
               bg="deep sky blue",
               fg="black",
               borderwidth=0,
               cursor="hand2",
               command=division).grid(row=4, column=3, padx=1, pady=1)
boton_despejar = Button(root,text="Borrar",
               width=20,
               height=3,
               bg="deep sky blue",
               fg="black",
               borderwidth=0,
               cursor="hand2",
               command=borrar).grid(row=5, column=0,columnspan=2,  padx=1, pady=1)
boton_despejar_uno = Button(root,text="Borrar Uno",
               width=20,
               height=3,
               bg="deep sky blue",
               fg="black",
               borderwidth=0,
               cursor="hand2",
               command=borrar_uno).grid(row=5, column=2,columnspan=2, padx=1, pady=1)

mainloop()

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
def raiz (n):
    x=0
    while x * x <= n:
        x+=0.1
    return x

