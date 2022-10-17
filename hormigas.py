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