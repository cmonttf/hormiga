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

print(rand_bin())
print(rand_n(15))

sys.argv = ['hormigas.py', '4', '40', '200', '0.1', '2.5', '0.9', 'berlin52.tsp']

if len(sys.argv) == 8:
    semilla = int(sys.argv[1])
    col = int(sys.argv[2])
    ite = int(sys.argv[3])
    tev = float(sys.argv[4])
    B = float(sys.argv[5])
    q0 = float(sys.argv[6])
    entrada = '/archivos/' + sys.argv[7]
    print(semilla, col, ite, tev, B, q0, entrada)    
else:
    print("Error en la entrada de los parámetros")
    sys.exit(0)

tiempo_ini = time.process_time()
np.random.seed(semilla)

matrizCoordenadas = pd.read_table(entrada, header=None, delim_whitespace=True, skiprows=6, skipfooter=2)
matrizCoordenadas = matrizCoordenadas.drop(columns=0,axis=1).to_numpy()
print('matrizCoordenadas-shapa:', matrizCoordenadas.shape)
numVariables = matrizCoordenadas.shape[0]
print('Matriz de Coordenadas:\n', matrizCoordenadas, '\ntamaño:',matrizCoordenadas.shape,'\ntipo:', type(matrizCoordenadas))
print('Número de variables:',numVariables)
