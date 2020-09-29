
"""
Created on Mon Sep 28 08:25:36 2020

@author: Arael Paloma - Oswaldo Robles
"""

ES=[
    ("Sauropsidos","Tetrapodos"),
    ("Mammalia","Tetrapodos"),
    ("Tetrapodos","Vertebrados"),
    ("Viviparo","Mammalia"),
    ("Oviparo","Sauropsidos"),
    ("Delfin","Viviparo"),
    ("Ballena","Viviparo"),
    ("Oso","Viviparo"),
    ("Gato","Viviparo"),
    ("Tortuga","Oviparo"),
    ("Iguana","Oviparo"),
    ("Cocodrilo","Oviparo"),
    ("Gallo","Oviparo"),
    ("Tortuga","Oviparo")
]
VIVE=[
    ("Tortuga","Agua"),
    ("Tortuga","Tierra"),
    ("Gallo","Tierra"),
    ("Cocodrilo","Agua"),
    ("Cocodrilo","Tierra"),
    ("Iguana","Tierra"),
    ("Gato","Tierra"),
    ("Oso","Tierra"),
    ("Ballena","Agua"),
    ("Delfin","Agua")
]
TIENE=[
    ("Tortuga","Garras"),
    ("Tortuga","Proteccion queratina"),
    ("Gallo","Garras"),
    ("Gallo","Proteccion queratina"),
    ("Cocodrilo","Garras"),
    ("Cocodrilo","Proteccion queratina"),
    ("Iguana","Garras"),
    ("Iguana","Proteccion queratina"),
    ("Gato","Garras"),
    ("Gato","Pelo"),
    ("Gato","G.Mamarias"),
    ("Oso","Garras"),
    ("Oso","Pelo"),
    ("Oso","G.Mamarias"),
    ("Ballena","Proteccion queratina"),
    ("Ballena","G.Mamarias"),
    ("Delfin","G.Mamarias")
]

def Es(A,B,CON):
    n=0
    while n<len(CON):
        if CON[n][0]==A:
            if CON[n][1]==B:
                return True
            A=CON[n][1]
        n=n+1
    return False

def Vive(A,B,CON):
    m=0
    while m<len(CON):
        if CON[m][0]==A:
            if CON[m][1]==B:
                return True
        m=m+1
    return False

def Tiene(A,B,CON):
    o=0
    while o<len(CON):
        if CON[o][0]==A:
            if CON[o][1]==B:
                return True
        o=o+1
    return False
print("***** ANIMALES QUE SON *****")
print(Es("Gato","Viviparo",ES)) #GATO TRUE
print(Es("Delfin","Oviparo",ES)) #DELFIN FALSE
print(Es("Cocodrilo","Oviparo",ES)) #COCODRILO TRUE
print(Es("Iguana","Viviparo",ES)) #IGUANA FALSE

print("*****ANIMALES QUE VIVEN EN*****")
print(Vive("Tortuga","Agua",VIVE)) #TORTUGA TRUE
print(Vive("Ballena","Tierra",VIVE))#BALLENA FALSE
print(Vive("Gato","Tierra",VIVE)) #GATO TRUE
print(Vive("Gallo","Agua",VIVE)) #GALLO FALSE

print("*****ANIMALES QUE TINEN*****")
print(Tiene("Oso","Pelo",TIENE)) #OSO TRUE
print(Tiene("Gallo","G.Mamarias",TIENE)) #GALLO FALSE
print(Tiene("Ballena","Proteccion queratina",TIENE)) #BALLENA TRUE
print(Tiene("Delfin","Garras",TIENE)) #DELFIN FALSE
