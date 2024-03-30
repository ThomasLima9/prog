from math import *
from string import * 

#entrada de dados

altura = float(input('Digite a altura em metros: '))
sexo = input('Digite o sexo (F/M): ')

#Calculos 

while sexo not in ['M', 'm', 'F', 'f']:
  print('Sexo invalido: ')
  sexo = input('Digite o sexo (F/M): ')
  

if sexo == 'M' or sexo == 'm':
    peso=(72.7*altura) - 58

elif sexo == 'F' or sexo == 'f':
    peso=(62.1*altura) - 44.7

else:
    print('Entrada deve ser F ou M')
  
#Saida 
print('Peso ideal={:.1f}'.format(peso))
