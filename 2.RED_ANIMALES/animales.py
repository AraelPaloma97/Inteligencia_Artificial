# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 14:36:03 2020

@author: arael
"""
import json
Conocimiento = False

with open("animales.json", "r") as read_file:
    data = json.load(read_file)
    Conocimiento = data['conocimiento']

def principal(A, B, C, CON):
    if B == "es":
        return valida(A, B, C, CON)
    if B == "vive":
        return valida(A, B, C, CON)
    if B == "tiene":
        return valida(A, B, C, CON)

def valida(A, B, C, CON):
    n = 0
    while n<len(CON):
        if CON[n][0] == A:
          if CON[n][1] == B:
            if CON[n][2] == C:
              return True
        n = n + 1
    return False

def buscar(A, B, C):
    return principal(A, B, C, Conocimiento)

def main():
    print("Bienvenido a este programa")
    print()
    print('Puedes consutar escribiendo -> buscar("<animal>","<vive/es/tiene>","<lugar/clasificacion/caracteristica>")')
    print()
    print("Para salir presiona -> 'q' ")
    Terminar = False
    while not Terminar:
        Leer = input("> ")
        if Leer == 'q':
            return
        else:
            Imprimir = eval(Leer)
            print(Imprimir)

if __name__ == "__main__":
    main()