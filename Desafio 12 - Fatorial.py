# Escrever um programa que leia um número inteiro positivo N e calcule o seu fatorial.
# faça uma validação para aceitar apenas números positivos.
# crie o help() para as funções criadas.

def fatorial(num):
    """
    Calcula o fatorial de um número inteiro positivo.
    
    num (int): O número inteiro positivo para calcular o fatorial.

    retorna:
    int: O fatorial do número fornecido.
    """
    fat = 1
    if num == 0:
        return fat
    
    for i in range(1, num + 1, 1):
        fat *= i
    
    return fat


def validaInt(pergunta, min, max):
    """
    Valida se o número está dentro do intervalo fornecido.
    
    Parâmetros:
    pergunta (int): O número inteiro positivo para calcular o fatorial.
    min (int): O valor mínimo permitido (inclusive).
    max (int): O valor máximo permitido (inclusive).

    Retorna:
    int: O número fornecido.
    """
    x = int(input(pergunta))
    while x < min or x > max:
        x = int(input(pergunta))
    
    return x
        

a = validaInt("Digite um número inteiro positivo: ", 0, 100)

print(f"O fatorial de {a} é {fatorial(a)}")