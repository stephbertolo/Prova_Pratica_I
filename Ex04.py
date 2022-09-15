saldo = 0.0

consulta = 1
saque = 2
deposito = 3
sair = 4

continuarTransacao = True

print("Escolha uma das opções: \n"
      "1 - Consulta \n"
      "2 - Saque \n"
      "3 - Deposito \n"
      "4 - Sair")

while continuarTransacao:
    escolha = int(input("Qual a opção desejada? "))

    if escolha == 1:
        print("Seu saldo é: " + str(saldo))

        continuar = int(input("Deseja continuar? \n"
                              "1 - Sim \n"
                              "2 - Não \n"))
        if continuar == 1:
            continuarTransacao = True
        else:
            continuarTransacao = False

    elif escolha == 2:
        dinheiroSacado = float(input("Quanto deseja sacar? "))
        if dinheiroSacado > saldo:
            print("Saldo insuficiente!")
        else:
            saldo = saldo - dinheiroSacado
            print("Seu saldo agora é: " + str(saldo))

        continuar = int(input("Deseja continuar? \n"
                              "1 - Sim \n"
                              "2 - Não \n"))

    elif escolha == 3:
        dinheiroDepositado = float(input("Quanto deseja depositar? "))
        saldo = saldo + dinheiroDepositado
        print("Seu saldo agora é: " + str(saldo))

        continuar = int(input("Deseja continuar? \n"
                              "1 - Sim \n"
                              "2 - Não \n"))

    else:
        break





