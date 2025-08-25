#Algoritmo que simula um banco. O cliente pode fazer depósitos, saques e consultar o saldo.

print("Bem-vindo ao Banco!")
print("1. Depositar")
print("2. Sacar")
print("3. Consultar Saldo")
print("4. Sair")

saldo = 0
cedulas = 0
while True:
    opcao = input("Escolha uma opção (1-4): ")

    if opcao == '1':
        valor = int(input("Digite o valor a ser depositado: R$"))
        saldo += valor
        print(f"Depósito realizado com sucesso! Saldo atual: R${saldo:.2f}")

    elif opcao == '2':
        valor = int(input("Digite o valor a ser sacado: R$"))
        if valor > saldo:
            print("Saldo insuficiente para saque.")
        else:
            saldo -= valor
            cedulas = valor
            c100 = c50 = c20 = c10 = c5 = c1 = 0
            while cedulas > 0:
                if cedulas >= 100:
                    c100 = cedulas // 100
                    cedulas = cedulas - (c100 * 100)
                    if not cedulas:
                        break
                elif cedulas >= 50:
                    c50 = cedulas // 50
                    cedulas = cedulas - (c50 * 50)
                    if not cedulas:
                        break
                elif cedulas >= 20:
                    c20 = cedulas // 20
                    cedulas = cedulas - (c20 * 20)
                    if not cedulas:
                        break
                elif cedulas >= 10:
                    c10 = cedulas // 10
                    cedulas = cedulas - (c10 * 10)
                    if not cedulas:
                        break
                elif cedulas >= 5:
                    c5 = cedulas // 5
                    cedulas = cedulas - (c5 * 5)
                    if not cedulas:
                        break
                elif cedulas:
                    c1 = cedulas
                    break

            print(f"Você sacou: {c100} cédulas de R$100, {c50} cédulas de R$50, {c20} cédulas de R$20, {c10} cédulas de R$10, {c5} cédulas de R$5 e {c1} cédulas de R$1.")
            print(f"Saque realizado com sucesso! Saldo atual: R${saldo:.2f}")          
        

    elif opcao == '3':
        print(f"Seu saldo atual é: R${saldo:.2f}")

    elif opcao == '4':
        print("Obrigado por usar nossos serviços. Até logo!")
        break

    else:
        print("Opção inválida, por favor tente novamente.")