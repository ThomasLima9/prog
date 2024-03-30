from math import *

#Entrada de dados

lado1 = float(input( "Digite o valor do lado 1: "))
lado2 = float(input( "Digite o valor do lado 2: "))
lado3 = float(input( "Digite o valor do lado 3: "))

# Dados

if lado1 == lado2 and lado1 == lado3 or lado2 == lado3:
  print('O triângulo é equilatero. ')

elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
  print('O triângulo é escaleno. ')

else:
  print('O triângulo é isósceles. ')