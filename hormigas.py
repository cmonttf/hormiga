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

matrizCoordenadas = pd.read_table(entrada, header=None, delim_whitespace=True, skiprows=6, skipfooter=2)
matrizCoordenadas = matrizCoordenadas.drop(columns=0,axis=1).to_numpy()
print('matrizCoordenadas-shape:', matrizCoordenadas.shape)
numVariables = matrizCoordenadas.shape[0]
print('Matriz de Coordenadas:\n', matrizCoordenadas, '\ntamaño:',matrizCoordenadas.shape,'\ntipo:', type(matrizCoordenadas))
print('Número de variables:',numVariables)

matrizDistancia = np.full((numVariables,numVariables), fill_value=-1.0,dtype=float)
for i in range(numVariables - 1):
    for j in range(i + 1, numVariables):
        matrizDistancia[i][j] = np.sqrt(np.sum(np.square(matrizCoordenadas[i]-matrizCoordenadas[j])))
        matrizDistancia[j][i] = matrizDistancia[i][j]
print('Matriz de Distancia:\n', matrizDistancia, '\ntamaño:', matrizDistancia.shape, '\tipo:', type(matrizDistancia))

matrizHeuristica = np.full_like(matrizDistancia, fill_value=1/matrizDistancia,dtype=float)
np.fill_diagonal(matrizHeuristica,0)
print('Matriz de Heuristica:\n', matrizHeuristica, '\ntamaño:', matrizHeuristica.shape, '\ntipo:', type(matrizHeuristica))

solucionMejor = np.zeros(numVariables)
solucionMejor = np.arange(0,numVariables)
np.random.shuffle(solucionMejor)
solucionMejorCosto = solucionCalculaCosto(numVariables,solucionMejor,matrizDistancia)
solucionMejorIteracion = 0
print('Solución inicial y a la vez mejor solución:\n', solucionMejor, '\ntamaño:', solucionMejor.shape, '\ntipo:', type(solucionMejor))
print('Costo de la solución inicial y a la vez mejor solución:', solucionMejorCosto)
print('Iteración donde se encontró la mejor solución:', solucionMejorIteracion)