import time
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from os import system
from Metodos.NewtonRaphson import NewtonRaphson
from Metodos.Eliminacion_Gauss import Eliminacion_Gauss
from Metodos.RaizCuadratica import RaizCuadratica
from Metodos.Metodo_Secante import Secante
from Metodos.Metodo_Biseccion import Metodo_biseccion
x=sp.Symbol('x')



def metodo1():
    print("                  Método de Newton Raphson")
    funcion = input("Ingrese los coeficientes de la funcion: ")
    xi = input("Ingrese xi: ")
    rangoI = input("Ingrese el rango inicial de la grafica: ")
    rangoF = input("Ingrese el rango final de la grafica: ")
    newton = NewtonRaphson()
    newton.set_ecuacion(funcion)
    newton.set_xi(xi)
    newton.set_rango(rangoI, rangoF)
    print("Resultado: ",newton.get_resultado())
    newton.get_grafica()
    time.sleep(3)



def metodo2():
    Eliminacion = Eliminacion_Gauss;
    Eliminacion.gauss();



def metodo3():
    print("")
    print("                 MÉTODO DE BISECCIÓN")
    print("")
    biseccion = Metodo_biseccion()
    biseccion.Biseccion()
    time.sleep(3)

    

def metodo4():
    print("                  Raiz Cuadratica.")
    print("Ingrese los valores a,b,c...")
    __a = input("Ingrese a: ")
    __b = input("Ingrese b: ")
    __c = input("Ingrese c: ")
    cuadratica = RaizCuadratica()
    cuadratica.set_variables(__a, __b, __c)
    cuadratica.get_calcular()
    cuadratica.get_grafica()
    time.sleep(3)
    
def metodo5():
    print("")
    print("                 MÉTODO DE LA SECANTE")
    print("")
    M_secante = Secante()
    M_secante.get_secante()
    time.sleep(3)


def menu():
    operacion = 0
    while operacion != 10:
        print("||||||||||||||||||||||||||||||||||||||||||||||||")
        print("||                   Menu                     ||")
        print("||           1. Newton raphson.               ||")
        print("||           2. Eliminacion de gauss.         ||")
        print("||           3. Método de bisección.          ||")
        print("||           4. Raiz cuadratica.              ||")
        print("||           5. Método de la secante.         ||")
        print("||           6. Salir del programa.           ||")
        print("||||||||||||||||||||||||||||||||||||||||||||||||")
        print("||/*NOTA: para ingresar la funcion e ingresar x debe poner '*x' o elevar '**2'*/||")
        operacion = int(input("Digite la Opcion: "))
        if operacion == 1:
            metodo1()
        elif operacion == 2:
            metodo2()
        elif operacion == 3:
            metodo3()
        elif operacion == 4:
            metodo4()
        elif operacion == 5:
            metodo5()
        elif operacion == 6:
            exit
        system('cls')   
menu()