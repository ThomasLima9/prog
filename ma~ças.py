from math import *
from string import *

#Dados 

macas = int(input('Digite a quantidade de Macas: '))

#Saida de dados

while macas <= 0:
    print('Digite um numero valido: ')
    int(input('Digite a quantidade de Macas: '))

if macas < 12:
    print('O valor da compra é: R$', macas*0.30)

elif macas >= 12 and macas < 24:
    print('O valor da compra é: R$', macas*0.25)
    
else:
    print('O valor da compra é: R$', macas*0.20)
    