# Peça 3 notas (0 a 10) e calcule a média. Se qualquer nota for inválida (<0 ou >10), 
# peça para digitar novamente. Use `while` para validar cada nota e `if/else` para 
# classificar a média:
# - >= 9: "Excelente"
# - >= 7: "Bom"
# - >= 5: "Razoável"
# - < 5: "Insuficiente"

print('''Bem vindo a calculadora de média automática!
Com ela você poderá calcular qualquer média de número inteiros de 0 a 10.
Não é permitido números negativos ou maiores de 10.''')

while True:
    try:
        nota_01 = int(input('Digite o Primeiro número de 0 a 10: '))
        nota_02 = int(input('Digite o Segundo número de 0 a 10: '))
        nota_03 = int(input('Digite o Terceiro número de 0 a 10: '))
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")
    if nota_01 < 0 or nota_01 >10 or nota_02 < 0 or nota_02 > 10 or nota_03 < 0 or nota_03 > 10:
        print('Insira valores números que sejam positivos, inteiros e entre 0 e 10.')
        continue
    media = (nota_03 + nota_01 + nota_02) / 3
    if media >= 9:
        print('Excelente')
    elif media >= 7:
        print('Bom')
    elif media >= 5:
        print('Razoável')
    else:
        print('Ruim')
    break
print(media)
