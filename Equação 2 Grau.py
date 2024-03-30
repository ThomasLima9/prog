from math import * 

#Entrada de dados.

a=int(input('Digite o coeficiente A: '))
b=int(input('Digite o coeficiente B: '))
c=int(input('Digite o coeficiente C: '))

# Calculo.
   
Delta = ((b**2) - (4-a*c))
x1 = (-b + sqrt(Delta) / 2*a)
x2 = (-b - sqrt(Delta) / 2*a)

# Saida de dados.

print('Valor de x1 é:', x1)
print('Valor de x2 é:', x2)


 