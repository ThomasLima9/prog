entrada = input('Digite os numeros separados com '"virgula:" )

numero = list(map(int, entrada.split(',')))

print('Quantidade de digitos', len(numero))
print('Soma dos numeros',sum(numero))
