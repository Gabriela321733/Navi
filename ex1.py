from numpy import log as ln 
import numpy as np
import math 

contador = 0
for i in range(1, 5000001):
    if i%2 == 0 and i%37 == 0 and i%49 == 0:
        contador += 1
print(f'Quantidade de numeros pares multiplos de 37 e 49: {contador}')