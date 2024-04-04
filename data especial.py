from math import *
from string import *

#Entrada de dados

numero = int(input('Digite um número: '))

#Calcule

dezenad = (numero%100)
dezenae = (numero//100)

somaq = (dezenad + dezenae)**2

#Saida de dados

if somaq == numero:
    print(numero,'é especial!')

else:
    print(numero,' não é especial!')

