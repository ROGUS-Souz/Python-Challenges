# Desafio 3: Contador de Vogais e Consoantes
# Objetivo:
# Crie um programa que conte quantas vogais e consoantes 
# existem em uma palavra digitada pelo usuário, ignorando números, símbolos e espaços.

# Requisitos:
# Use um loop for com range(len(palavra)) para percorrer cada letra.
# Utilize if/elif/else para classificar vogais e consoantes.
# Considere apenas letras maiúsculas/minúsculas (ignore caracteres especiais).
# Exiba os resultados no formato:

print(' Bem vindo ao contador de vogais e consoantes!')
print(' Digite uma palavra e eu contarei quantas vogais e consoantes existem nela!')
print(' Lembre-se de que números, símbolos e espaços não serão contados. Além disso,')
print(' a palavra não pode ser um número.')
print(' Vamos lá!')
print('--------------------------------------------------')

palavra = input("Digite uma palavra: ").lower()
vogais = ['a','e','i','o','u']
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
contador_vogais = 0
contador_consoantes = 0
contador_outras = 0

if palavra.isnumeric():
    print("A palavra não pode ser um número.")
    palavra = input("Digite uma palavra: ").lower()

for letras in range(len(palavra)):
    if palavra[letras] in vogais:
        contador_vogais += 1
    elif palavra[letras] in consoantes:
        contador_consoantes += 1
    else:
        contador_outras += 1

print(palavra)
print(f"Total de vogais: {contador_vogais}")
print(f"Total de consoantes: {contador_consoantes}")
print(f"Total de outros caracteres: {contador_outras}")
print(f"Total de letras: {contador_vogais + contador_consoantes}")