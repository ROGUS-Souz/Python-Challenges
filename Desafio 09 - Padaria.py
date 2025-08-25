# Escreva uma algoritmo que o pedido da padaria. Coxinha 5$, Pastel 7$, Café 4$, Suco 6$.
# O algoritmo deve perguntar o que o cliente deseja e a quantidade. No final deve mostrar o total da compra.

print("Bem-vindo à Padaria!")
print("Nosso cardápio:")
print("1. Coxinha - R$5,00")
print("2. Pastel - R$7,00")
print("3. Café - R$4,00")
print("4. Suco - R$6,00")
print("5. Finalizar pedido")

total = 0

while True:
    escolha = input("Digite o número do item que deseja (ou 5 para finalizar): ")

    if escolha == '5':
        break

    quantidade = int(input("Digite a quantidade desejada: "))

    if escolha == '1':
        total += 5 * quantidade
    elif escolha == '2':
        total += 7 * quantidade
    elif escolha == '3':
        total += 4 * quantidade
    elif escolha == '4':
        total += 6 * quantidade
    else:
        print("Opção inválida, por favor tente novamente.")


print(f"O total da sua compra é: R${total:.2f}")
