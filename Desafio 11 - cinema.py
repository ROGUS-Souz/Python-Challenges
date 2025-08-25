# Criar um sistema de cinema que cobra peços diferentes para diferentes idades.
# Crianças com menos de 3 anos não pagam, crianças de 3 a 12 pagam R$15,00, maiores de 12 anos pagam R$30,00.
# Coloque no final total de pessoas que compraram o ingresso, total arrecadado e a média de idade do grupo.

total = 0
pessoas = 0

print("Bem-vindo ao sistema de venda de ingressos do cinema!")
print("Idades menores que 3 anos não pagam, de 3 a 12 anos pagam R$15,00, maiores de 12 anos pagam R$30,00.")
print("-------------------------------")




while True:
    print("Selecione uma das opções para continuar")
    print("1 - Comprar ingresso")
    print("2 - Sair")
    ingresso = input("Digite a opção desejada (1 ou 2): ")
    if ingresso == '2':
        break
    elif ingresso != '1':
        print("Opção inválida. Tente novamente.")
        continue
    idade = int(input("Digite a idade da pessoa: "))

    if idade < 0:
        print("Idade inválida. Tente novamente.")
        continue
    if idade < 3:
        preco = 0
        total = preco
    elif idade <= 12:
        preco = 15
        total = preco
    else:
        preco = 30
        total = preco
    pessoas += 1
    total += preco

media = total / pessoas

print("-------------------------------")
print(f"Total de pessoas que compraram ingresso: {pessoas}")
print(f"Total arrecadado: R${total:.2f}")
print(f"Média de idade do grupo: {media:.2f} anos")
