# Desafio do banco DIO - Bootcamp Ciência de Dados com Python

# Entrada de variáveis
saldo = 0
limite = 500
extrato = " "
quant_saque = 0
LIMITE_SAQUE = 3

# Entrada, processamento e saída de dados
while True:

    opcao = int(input(menu="""
	*********** BANCO DIO ***********
	| 1. Depósito                   |
	| 2. Saque                      |
	| 3. Extrato                    |
	| 0. Sair                       |
	*********************************

=> """))

    # Realizar depósito em conta
    if opcao == 1:
        valor = float(input("Digite o valor do Depósito: R$  "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito R$ {valor:.2f} \n"

        else:
            print("Ocorreu uma FALHA! Valor inválido! informe um valor válido!")

    # Realizar Saque
    elif opcao == 2:
        valor = float(input("Digite o valor de Saque: R$  "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = quant_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Saldo Insuficiente")

        elif excedeu_limite:
            print("Operação não realizada! Excedeu o valor de limite de saque!")

        elif excedeu_saque:
            print("Operação não realizada! Quantidade de saques execedido!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R$ {valor:.2f}\n"
            quant_saque += 1
            print("Saque realizado com sucesso!")

        else:
            print("Ocorreu uma FALHA! Valor inválido! Informe um valor válido!")

        # Verificar extrato na conta	elif opcao == 3:
        print("\n ************  EXTRATO  ************")
        print("Não foram realizadas transações." if not extrato else extrato)
        print(f"\n Saldo Disponível R$ {saldo:.2f}")
        print("\n ***********************************")

    # Opção de encerrar atendimento
    elif opcao == 0:
        break

    # Se usuário digitar opção fora do menu
    else:
        print("Digite uma opção válida!")