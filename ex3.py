from numpy import log as ln 
import numpy as np
import math 

dicionario = {}
for i in range(0, 5):
    nome_aluno = input('Nome do aluno(a)? ')
    nota_aluno = float(input('Nota aluno? '))
    dicionario[nome_aluno] = nota_aluno
maior_nota = -1
for nome_aluno, nota_aluno in dicionario.items():
    if maior_nota < nota_aluno:
        maior_nota = nota_aluno
        nome_maior = nome_aluno
print(f'O aluno com a maior nota foi {nome_maior} com nota {maior_nota}')
