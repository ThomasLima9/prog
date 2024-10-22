class Dog:
    def __init__(self, nome, dia, mes, ano, latido,):
        self._nome = nome
        self._mes = mes
        self._dia = dia
        self._ano = ano
        self._latido = latido

    
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
        nova_dia = input('Digite a nova data do cachorro: ')
        novo
        self._data = nova_data

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
cachorro_data = cachorro.data()
cachorro_nome = cachorro.nome()
print(cachorro_nome)
print(cachorro_data)
