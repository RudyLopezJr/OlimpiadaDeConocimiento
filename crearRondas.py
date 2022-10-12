from unicodedata import category
import pandas as pd
import random



df = pd.read_csv("Preguntas.csv")
totalP = len(df)

print(len(df))

preguntas = list(range(0,totalP))
#print(preguntas)

nRondas = 16

preguntasPorRonda = []


#for i in range(nRondas):clr
    #preguntasPorRonda.append([])

def separarCategoria(nombre):
    categoria = []
    for i in range(len(preguntas)):
        if df['Categoría'][preguntas[i]] == nombre:
            categoria.append(preguntas[i])
    return categoria

def separarDificultad(categoria):
    dificultades = ['Facil', 'Medio', 'Dificil']
    mDificultades = [[],[],[]]

    for j in range(len(dificultades)):
        for i in range(len(categoria)):
            if df['Dificultad'][categoria[i]] == dificultades[j]:
                mDificultades[j].append(categoria[i])
    return mDificultades

def seleccionarPreguntas(dificultades, nFacil, nMedio, nDificil):
    preguntasSel = []
    j = 0
    #print(nFacil,nMedio,nDificil)
    for dificultad in dificultades:
        #print(j)
        if j == 0:
            nDif = nFacil
        elif j == 1: 
            nDif = nMedio
        else:
            nDif = nDificil
        
        for i in range(nDif):
            n = random.randint(0, len(dificultad)-1)
            numElim = dificultad.pop(n)
            #print(numElim)
            preguntasSel.append(numElim)
            #print(numElim)
            preguntas.remove(numElim)
        j+=1
    #print(preguntasSel)
    
    return dificultades, preguntasSel




categorias = ['Ciencias básicas', 'Ingeniería en Datos', 'Ingeniería en Logística', 'Ingeniería Ambiental', 'Ingeniería Industrial', 'Cultura General']




for j in range(nRondas):
    rondaPregSel = []
    for i in range(len(categorias)):
        #print(categorias[i])
        categoria = separarCategoria(categorias[i])
        dificultades = separarDificultad(categoria)

        if i == 0:
            nFaciles = 2
            nMedia = 2
            nDificil = 1
        else:
            nFaciles = 1
            nMedia = 1
            nDificil = 1

        dificultades, preguntasSel = seleccionarPreguntas(dificultades, nFaciles, nMedia, nDificil)
        rondaPregSel += preguntasSel
    
    preguntasPorRonda.append(rondaPregSel)

print(len(preguntasPorRonda))
print(len(preguntas))



i = 1
columns_names = df.columns.values

for ronda in preguntasPorRonda:
    name = "ronda " + str(i)
    dfN = pd.DataFrame(columns=[columns_names])
    for element in ronda:
        nueva_fila = df.iloc[element].tolist()
        #print(nueva_fila)
        dfN.loc[len(dfN)] = nueva_fila
    
    i= i +1
    print(name)
    namecsv = name + ".csv"
    dfN.to_csv(namecsv)
    print(dfN)

#df.to_csv("hola mundo2.csv")