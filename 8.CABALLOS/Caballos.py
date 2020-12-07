# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 09:25:51 2020

@author: oswaldo
"""

import json
with open ("caballos.json","r") as read_file:
	data = json.load(read_file)
	Movimientos = data['Movimientos']
	Tableroini = data['Tableroini']
	Tablerofin = data['Tablerofin']

def caballo(Mtr,aca,mov):
	f=[[0,0,0],[0,0,0],[0,0,0]]
	t = 0
	while(t < 3):
		d = 0
		while(d < 3):
			if (Mtr[t][d] != 0):
				dig = Mtr[t][d]
				Mtr[t][d] = 0
				busca(t,d,dig,f,mov)
			d +=1
		t +=1
	for c in f: print (c)
	if (f != Tablerofin):
		return caballo(f,aca,mov)

def busca(p_i,p_j,dig,f,mov):
	ele = Ma[p_i][p_j]
	for c in Movimientos:
		if (ele == c[0]):
			t = 0
			while(t <= 2):
				d = 0
				while(d <= 2):
					if (Ma[t][d] == c[mov]):
						f[t][d] = dig
						return f
					d += 1
				t += 1

Ma=[[0,1,2],[3,4,5],[6,7,8]]
mov = int(input("Recorre derecha = 1 , Recorre Izquierda = 2    "))

if (mov < 1 or mov > 2):
	quit()
caballo(Tableroini,Tablerofin,mov)