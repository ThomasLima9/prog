from math import *
#Dados das notas

print('Digite as notas: ')

me = int(input('Digite o me: '))
nota1 = int(input('Nota da prova 1: '))
nota2 = int(input('Nota da prova 2: '))
nota3 = int(input('Nota da prova 3: '))

#Calculos


ma = ((nota1 * nota2 * 2) + (nota3 * 3) + (me)) / (3)



#Saida de dados

print('Media das notas: ', ma)