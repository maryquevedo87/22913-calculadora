import os
import statistics
from operaciones import*

def menu():
    os.system("cls")
    print("+ para sumar")
    print("- para restar")
    print("/ para dividir")
    print("* para multiplicar")
    print("s para salir")

def menu_estadistica():
    os.system("cls")
    print("1 para media")
    print("2 para mediana")
    print("3 para moda")
    print("4 para varianza")
    print("5 para desviacion estandar")
    print("6 para cargar datos")
    print("7 para salir")

def menu_cientifica():
    os.system("cls")
    print("1 para potencia")
    print("2 para Raiz 2")
    print("3 para seno")
    print("4 para coseno")
    print("5 para tangente")
    print("6 para Salir")

def cargar_datos(datos):
    while True:
        d=int(input("ingrese un dato: "))
        datos.append(d)
        print("desea ingresar otro dato? s/n")
        op=input()
        if op=="n":
            break
    return datos

def main():
        
    while True:
        os.system("cls")
        print("n Para calculadora normal")
        print("e para datos estadisticos")
        print("c Para calculadora cientifica")
        print("s Para salir")
        tc=input("ingrese el tipo de calculadora que desea usar: ")
        if tc=="n":
            menu()
            op=input("ingrese una operación ")
            while op != "s":
                pn=int(input("ingrese un numero: "))
                sn=int(input("ingrese otro numero: "))
                if op=="+":
                    print("el resultado de la suma es:" , sumar(pn,sn)) 
                elif op =="-":
                    print ("el resultado de la resta es: ",  restar(pn,sn))
                elif op=="/":
                    print("el resultado de la división es: ", dividir(pn, sn))
                elif op=="*":
                    print ("El resultado de multiplicar es:", multiplicar(pn,sn))
                else:
                    print("opcion no valida")
                input("presione enter para continuar....")
                menu()
                op=input("ingrese una operación ")
        elif tc=="e":
            datos=[]
            print("estadistica")
            menu_estadistica()
            op=input("ingrese una operación ")
            while op != "7":
                if op=="6":
                    datos=cargar_datos(datos)
                elif op=="1":
                    if len(datos)>0:
                        print("la media es: ", statistics.mean(datos))
                    else:
                        print("no hay datos cargados")
                elif op=="2":
                    if len(datos)>0:
                        print("la mediana es: ", statistics.median(datos))
                    else:
                        print("no hay datos cargados")
                elif op=="3":
                    if len(datos)>0:
                        print("la moda es: ", statistics.mode(datos))
                    else:
                        print("no hay datos cargados")
                elif op=="4":
                    if len(datos)>0:
                        print("la varianza es: ", statistics.variance(datos))
                    else:
                        print("no hay datos cargados")
                elif op=="5":
                    if len(datos)>0:
                        print("la desviacion estandar es: ", statistics.stdev(datos))
                    else:
                        print("no hay datos cargados")
                else:
                    print("opcion no valida")
                input("presione enter para continuar....")
                menu_estadistica()
                op=input("ingrese una operación ")
        elif tc=="c":
            import math
            print("cientifica")
            menu_cientifica()
            op=input("seleccione la operacion: ")
            while op !=6:
                if op=="1":
                    print("el resultado de la potencia es: ", math.pow())
                elif op=="2":
                    print("el resultado de la raiz es: " , math.sqrt())
                elif op=="3":
                    print("el resultado del logaritmo es: " , math.log())
                elif op=="4":
                    print("el resultado del logaritmo en base 10 es: " , math.log10())
                elif op=="5":
                    print("el resultado del exponente es: " , math.exp())
                input("ingrese enter para continuar")
        else tc=="s":
            print("saliendo")
            break