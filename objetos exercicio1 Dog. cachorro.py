class Dog:
    def __init__(self, nome, dia, mes, ano, latido):
        self._nome = nome
        self._mes = mes
        self._dia = dia
        self._ano = ano
        self._latido = latido
        self._idade = None

    
    def nome(self):
        nome = self._nome
        return f'Seu nome é: {nome}'

    def data(self):
        dia = self._dia
        mes = self._mes
        ano = self._ano

        return f'Nasceu em: {dia}/{mes}/{ano}'
    
    def latido(self):
        latido = self._latido
        return f'Seu latido é: {latido}'

    def novo_nome(self):
        novo_nome = input('Qual o nome do novo cachorro: ')
        self._nome = novo_nome
        
    def nova_data(self):
        dia = int(input('Digite o novo dia de nascimento: '))
        mes = int(input('Digite o novo mes de nascimento: '))
        ano = int(input('Digite o novo ano de nascimento: '))
        self._dia = dia
        self._mes = mes
        self._ano = ano
    
    def novo_latido(self):
        latido = input('Digite o novo latido: ')
        self._latido = latido

    def idade(self):
        self._idade = 2024 - self._ano
    
    def __str__(self):
        inf = 'Nome: ' + str(self._nome) + '\n'  
        inf += 'Data: ' + str(f'{self._dia}/{self._mes}/{self._ano}') + '\n'
        inf += 'Latido:' + str(self._latido) + '\n'
        inf += 'Idade:' + str(self._idade) + '\n'
        return inf 



nome = input('Digite o nome do cachorro: ')
dia = int(input('Qual dia o cachorro nasceu: '))
mes = int(input('Qual mes o cachorro nasceu: '))
ano = int(input('Qual ano o cachorro nasceu: '))
latido = input('Digite o latido do bixo: ')

cachorro = Dog(nome,dia,mes,ano,latido)
cachorro_nome = cachorro.nome()
cachorro_data = cachorro.data()
cachorro_latido = cachorro.latido()
print(cachorro_nome)
print(cachorro_data)
print(cachorro_latido)

cachorro.novo_nome()
cachorro.nova_data()
cachorro.novo_latido()
cachorro_latido = cachorro.latido()
cachorro_data = cachorro.data()
cachorro_nome = cachorro.nome()
cachorro.idade()
print(cachorro_nome)
print(cachorro_data)
print(cachorro_latido)

def main():
    cachorro._nome = 'Rex'
    cachorro._dia = 6
    cachorro._mes = 11
    cachorro._ano = 2005
    cachorro._latido = 'HUUUUUUUUUUUUUUUUUUUUUUUUUUF'
    cachorro._idade= 18
    return cachorro._nome, cachorro._dia , cachorro._mes , cachorro._ano  , cachorro._latido , cachorro._idade
main()

print(f'Principais informações do cachorro: {str(cachorro)}' )
