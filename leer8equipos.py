from typing import final
import pandas as pd
# generate random integer values
from numpy.random import seed
from numpy.random import randint

df = pd.read_csv("equipos1.csv")
nombreEquipos = df["Nombre"][:]
lenEquipos = len(nombreEquipos)
#for nombre in nombreEquipos:
#   print(nombre)

seed(1)
sorteo = []
i=0
while i < lenEquipos:
    value = randint(0 , 16)
    if value in sorteo:
        i-=1
    else:
        sorteo.append(value)
    i+=1  
#print(sorteo)
OctRound1 = list(sorteo[:2])
OctRound2 = list(sorteo[2:4])
OctRound3 = list(sorteo[4:6])
OctRound4 = list(sorteo[6:8])
OctRound5 = list(sorteo[8:10])
OctRound6 = list(sorteo[10:12])
OctRound7 = list(sorteo[12:14])
OctRound8 = list(sorteo[14:16])
sorteoFinal = [OctRound1, OctRound2, OctRound3, OctRound4, OctRound5, OctRound6, OctRound7, OctRound8]
#print(sorteoFinal)
j=1
for equipo in sorteoFinal:
    print("El duelo numero ", j, " es: ", nombreEquipos[equipo[0]], " VS ", nombreEquipos[equipo[1]],"\n")
    j+=1