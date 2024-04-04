from math import *
from string import * 

#Entrada de dados

produto = float(input('Digite o preço do produto: '))
condicao = int(input('Condição de pagamento (1/2/3/4): '))

#Calculos + Saida de Dados

while condicao <=0 or condicao >=5:
    print('Condição de pagamento inválido, digite novamente: ')
    int(input('Condição de pagamento (1/2/3/4): '))

if condicao == 1:
    print('Valor a pagar: ', produto - (produto*10) / (100))

elif condicao == 2:
    print('Valor a pagar: ', produto - (produto*15) / (100))
    
elif condicao == 3:
    print('Valor a pagar: ', produto )

else:
    print('Valor a pagar: ', produto + (produto*10) / (100))

#Condição com if's 1 a 4.
#Fórmula da porcentagem.
    