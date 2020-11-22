# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 11:42:05 2020

@author: oswap
"""

import json
import random
from operator import itemgetter
#para abrir nuestro documento json
with open('Conocimiento.json') as file:
	Conocimiento = json.load(file)


ruta=[]
way=[]
otra = []

def subida(inicial,objetivo,ant):
	ruta.append(inicial)
	print("La ruta actual es "+inicial)
	print("La ruta anterior fue "+ant)
	if otra:
		del otra[:]
		del way[:]
	if objetivo == inicial:
		print("valor ha sido encontrado en")
		return inicial
	if ant == "":
		ant = inicial
	for d in Conocimiento:
		if d[0] == inicial:
			if ant != "":
				if d[1] != ant:
					way.append(d)
	print(min(way, key=itemgetter(2))[:])
	print (way)
	Nuev = (min(way, key=itemgetter(2))[2])
	
	for c in way:
		if c[2] == Nuev:
			print("entra")
			otra.append(c)
	print("valores definitivos")
	print(otra)
	cont = 0
	for n in otra:
		cont = cont +1
		if cont > 1:
			r = random.random()
			print("n")
			print(n)
			if r < 0.5:
				otra.pop()
			else: 
				otra.pop(0)
		else:
			print(otra)
	if otra:
		for n in otra:
			print("nodo")
			print(n[1])
			return subida(n[1],objetivo,inicial)


arch=subida("A","H","")
if arch:
	print("nodo")
	print(arch)
	print("ruta")
	print(ruta)