# Desafio 02 - Lógica de Programação - Triângulos e seus valores
# Peça 3 valores (lados de um triângulo) e determine se é:
# - Equilátero (todos lados iguais)
# - Isósceles (dois lados iguais)
# - Escaleno (todos lados diferentes)
# - Inválido (não forma triângulo: soma de 2 lados <= terceiro lado)
# Use `if/elif/else` e operadores lógicos (`and/or`).

# Iniciar o Loop para solicitar os lados do triângulo
while True:
    try:
        a = float(input("Digite o primeiro lado do triângulo: "))
        b = float(input("Digite o segundo lado do triângulo: "))
        c = float(input("Digite o terceiro lado do triângulo: "))
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")
    if a <= 0 or b <= 0 or c <= 0: # A primeira verificação é se os lados são maiores que zero para excluir valores negativos ou zero
        # Se algum lado for menor ou igual a zero, não é um triângulo válido
        print("Os lados do triângulo devem ser maiores que zero. Tente novamente.")    
        continue
    if a + b <= c or a + c <= b or b + c <= a:
       print("Os lados não formam um triângulo.")  # Verifica se a soma de dois lados é menor ou igual ao terceiro lado
       continue
    if a == b == c:
        print("Os lados formam um triângulo equilátero.")
    elif a == b or a == c or b == c:
        print("Os lados formam um triângulo isósceles.")
    else: 
        print("Os lados formam um triângulo escaleno.")

        
    break # Encerra o loop após a verificação dos lados do triângulo

        