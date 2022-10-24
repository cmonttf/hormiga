import numpy as np
import pandas as pd
import sys
import time

#Función randomica entre 0 y 1
def rand_bin():
    valor = np.random.random_sample()
    return valor


#Función randomico entre 1 y n
def rand_n(n):
    valor = np.random.randint(0,n)
    return valor

def solucionCalculaCosto(n, s, c):
    aux = c[s[n-1]][s[0]]
    for i in range(n-1):
        aux += c[s[i]][s[i+1]]
    return aux

def inicializarCoordenadas(entrada):
    matrizCoordenadas = pd.read_table(entrada, header=None, delim_whitespace=True, skiprows=6, skipfooter=2)
    matrizCoordenadas = matrizCoordenadas.drop(columns=0,axis=1).to_numpy()
    return matrizCoordenadas

def inicializarDistancia(numVariables, matrizCoordenadas):
    matrizDistancia = np.full((numVariables,numVariables), fill_value=-1.0,dtype=float)
    for i in range(numVariables - 1):
        for j in range(i + 1, numVariables):
            matrizDistancia[i][j] = np.sqrt(np.sum(np.square(matrizCoordenadas[i]-matrizCoordenadas[j])))
            matrizDistancia[j][i] = matrizDistancia[i][j]
    return matrizDistancia

def inicializarHeuristica(matrizDistancia):
    matrizHeuristica = np.full_like(matrizDistancia, fill_value=1/matrizDistancia,dtype=float)
    np.fill_diagonal(matrizHeuristica,0)
    return matrizHeuristica

sys.argv = ['hormigas.py', '4', '40', '200', '0.1', '2.5', '0.9', 'berlin52.tsp']

if len(sys.argv) == 8:
    semilla = int(sys.argv[1])
    col = int(sys.argv[2])
    ite = int(sys.argv[3])
    tev = float(sys.argv[4])
    B = float(sys.argv[5])
    q0 = float(sys.argv[6])
    entrada = 'archivos/' + sys.argv[7]
    print(semilla, col, ite, tev, B, q0, entrada)    
else:
    print("Error en la entrada de los parámetros")
    sys.exit(0)

tiempo_ini = time.process_time()
np.random.seed(semilla)

matrizCoordenadas = inicializarCoordenadas(entrada)
#print('matrizCoordenadas-shape:', matrizCoordenadas.shape)
numVariables = matrizCoordenadas.shape[0]
#print('Matriz de Coordenadas:\n', matrizCoordenadas, '\ntamaño:',matrizCoordenadas.shape,'\ntipo:', type(matrizCoordenadas))
#print('Número de variables:',numVariables)

matrizDistancia = inicializarDistancia(numVariables, matrizCoordenadas)
#print('Matriz de Distancia:\n', matrizDistancia, '\ntamaño:', matrizDistancia.shape, '\tipo:', type(matrizDistancia))

matrizHeuristica = inicializarHeuristica(matrizDistancia)
print('Matriz de Heuristica:\n', matrizHeuristica, '\ntamaño:', matrizHeuristica.shape, '\ntipo:', type(matrizHeuristica))

solucionMejor = np.zeros(numVariables)
solucionMejor = np.arange(0,numVariables)
np.random.shuffle(solucionMejor)
solucionMejorCosto = solucionCalculaCosto(numVariables,solucionMejor,matrizDistancia)
solucionMejorIteracion = 0
print('Solución inicial y a la vez mejor solución:\n', solucionMejor, '\ntamaño:', solucionMejor.shape, '\ntipo:', type(solucionMejor))
print('Costo de la solución inicial y a la vez mejor solución:', solucionMejorCosto)
print('Iteración donde se encontró la mejor solución:', solucionMejorIteracion)

Tij0 = 1/(numVariables*solucionMejorCosto)
matrizFeromona = np.full_like(matrizDistancia,fill_value=Tij0,dtype=float)
print('Matriz de Feromona:\n',matrizFeromona, '\ntamaño:', matrizFeromona.shape, '\ntipo:', type(matrizFeromona))

while solucionMejorIteracion < ite:
    #for i in range()
    #print(solucionMejorIteracion)
    solucionMejorIteracion+=1

tiempo_fin = time.process_time()
print('Tiempo:',(tiempo_fin-tiempo_ini),'seg.\n')