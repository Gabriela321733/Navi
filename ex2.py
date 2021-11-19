from numpy import log as ln 
import numpy as np
import math 

lista = [0,0,0,0,0,0,0,0,0,0]

for i in range(len(lista)):
    if i % 2 == 0: 
        lista[i] = (3**i) + 7*(math.factorial(i))
    else:
        lista[i] = (2**i) + 4*(math.log(i))
posicao_maior = lista.index(max(lista))
media = sum(lista)/len(lista)
print('A posição do maior elemento do vetor é {} e a média dos elementos do vetor é {:.2f}'.format(posicao_maior,media))
