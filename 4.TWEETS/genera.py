"""
En el comentario del archivo anterior, hice varias cosas, 
para poder sacar la matriz de probabilidades, 
ahora hay que hacer un programa que a partir de 10 tweets genere la misma 
matriz de probabilidades
sabiendo de ante mano cuales son los de stream
Sugiero esta estructura, para lo tweets
{
	"Tweets" : [
		{"Stream":true, "texto":"Vamos a darle a Among Us con famosos"},
		{"Stream":false, "texto":"El Fugitivo: La Historia en 1 Video"},
	]
}
y debe generar el  json compatible con el programa de clasificacion
"""
import json
tweets = False
a = 0
palabras = ["Ya","ando","el","para","mas","bien","martes","Que","que","a","un","en","este","si","la","al","le","ya","mis","los","sí","de","=)",",","emperrado","el","y","con","buen"]

with open("tweet.json","r") as read_file:
	data = json.load(read_file)
	tweets = data['Tweets']

def cjson(matriz):
	print()
	a = 0
	data = {}
	data["Probabilidades"] = []
	while a < len(matriz):
		data["Probabilidades"].append([matriz[a][0],matriz[a][4]])
		a = a + 1
	with open('base_conocimiento.json', 'w') as file:
		json.dump(data, file, indent=1)
	with open("base_conocimiento.json","r") as read_file:
		data = json.load(read_file)
		tw = data["Probabilidades"]
	return(tw)

def adver(tweet,palabras):
	i=0
	j=[]
	k=[]
	while i<len(tweet):
		a=0
		while a<len(tweet[i]):
			if not tweet[i][a] in palabras:
				b=tweet[i][a]
				j=j+[b]
			a=a+1
		i=i+1

	i=0
	while i<len(j):
		if not j[i] in k:
			k=k+[j[i]]
		i=i+1 
	return matriz(j,k, len(tweet))

def separa(tweets,palabras,x = []):
	a=0
	while a<len(tweets):
		tw=tweets[a]
		Stream=tw['Stream']
		texto=tw['texto']
		if Stream==True:
			texto=texto.split()
			x=x+[texto]
		a=a+1
	return adver(x,palabras)

def matriz(tweets,palabra,notweets):
	a=0
	b=0
	c=0
	mtrz=[]
	while a<len(palabra):
		j = 0
		while j<len(tweets):
			if tweets[j] == palabra[a]:
				b=b+1
			c=notweets-b
			j=j+1
		x=b+c
		mtrz.append([palabra[a], c, b, x, b/x, c/x])
		b=0
		c=0
		a=a+1
	print(mtrz)
	return cjson(mtrz)

print(separa(tweets,palabras))