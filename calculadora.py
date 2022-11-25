import os

def sumar (n1, n2):
    return n1+n2
def restar (n1, n2):
    return n1-n2
def multiplicar(n1, n2):
    return n1*n2
def division (n1, n2):
    try: 
        return n1/n2
    except:
        print("no se puede dividir por 0")

def menu ():
    os.system("cls")
    print("+ para sumar")
    print("- para restar")
    print("* para multiplicar")
    print("/ para dividir")
    print("s para salir")


def main():
    menu()
    op=input("ingrese una operación ")
    while op != "s":
        pn=int(input("ingrese un número: "))
        sn=int(input("ingrese otro número"))
        if op=="+":
            print ("el resultado de la suma es: " , sumar(pn,sn))
        elif op=="-":
             print ("el resultado de la resta es: " , restar(pn,sn))
        elif op=="*":
            print ("el resultado de la multiplicación es: " , multiplicar(pn,sn))
        elif op=="/":
             print ("el resultado de la división es: " , division(pn,sn))
        else:
            print("opción no válida")
        op=input("ingrese una operación ")
