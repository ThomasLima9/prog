def inicializa():
    print("\n--- Inicialização do Caixa Eletrônico ---")
    notas = [100, 50, 20, 10]
    quantidade_notas = {}
    
    for nota in notas:
        quantidade = int(input(f"Digite a quantidade de notas de R${nota}: "))
        if quantidade < 0:
            print("Erro: quantidade de notas não pode ser negativa. Programa encerrado.")
            exit(1)
        quantidade_notas[nota] = quantidade
    
    return quantidade_notas

def saque(saldo, valor, quantidade_notas):
    if valor <= 0:
        print("Saque inválido: valor solicitado é nulo ou negativo.")
        return saldo, quantidade_notas
    
    if valor > saldo:
        print("Saque inválido: saldo insuficiente.")
        return saldo, quantidade_notas
    
    notas_saque = {}
    valor_restante = valor
    for nota in sorted(quantidade_notas.keys(), reverse=True):
        if valor_restante >= nota:
            num_notas = min(valor_restante // nota, quantidade_notas[nota])
            notas_saque[nota] = num_notas
            valor_restante -= num_notas * nota
    
    if valor_restante > 0:
        print("Saque indisponível: caixa não possui o valor exato para saque.")
        return saldo, quantidade_notas
    
    saldo -= valor
    for nota, num_notas in notas_saque.items():
        quantidade_notas[nota] -= num_notas
    
    print("Saque realizado com sucesso. Notas entregues:")
    for nota, num_notas in notas_saque.items():
        print(f"R${nota}: {num_notas} nota(s)")
    
    return saldo, quantidade_notas

def deposito(saldo, valor):
    if valor <= 0:
        print("Erro: valor de depósito inválido.")
        return saldo
    saldo += valor
    print("Depósito realizado com sucesso.")
    return saldo

def saldo(saldo):
    print(f"Saldo atual: R${saldo:.2f}")

def sair():
    print("Encerrando o programa.")
    exit(0)

def menu():
    saldo_conta = 1000.00
    quantidade_notas = inicializa()
    
    while True:
        print("\n==============================")
        print("      CAIXA ELETRÔNICO        ")
        print("==============================")
        print("1. Saque")
        print("2. Depósito")
        print("3. Saldo")
        print("4. Sair")
        print("==============================")
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            valor_saque = float(input("Digite o valor do saque: R$"))
            saldo_conta, quantidade_notas = saque(saldo_conta, valor_saque, quantidade_notas)
        elif opcao == '2':
            valor_deposito = float(input("Digite o valor do depósito: R$"))
            saldo_conta = deposito(saldo_conta, valor_deposito)
        elif opcao == '3':
            saldo(saldo_conta)
        elif opcao == '4':
            sair()
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
menu()
