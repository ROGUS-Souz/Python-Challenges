#Calculadora de Média com Validação
#
# Peça 3 notas (0 a 10) e calcule a média.
#Valide se as notas são números e estão no intervalo permitido.
# Use listas para armazenar as notas e dicionários para classificar a média 
# (ex.: {"Excelente": >= 9}).

while True:
    try:
        nota01 = int(input("Digite a primeira nota (0 a 10): "))
        nota02 = int(input("Digite a segunda nota (0 a 10): "))
        nota03 = int(input("Digite a terceira nota (0 a 10): "))
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")
        continue
        
    validacao_da_nota = True # Variável para validar se as notas estão dentro 
    # do intervalo permitido
        
    for nota in [nota01, nota02, nota03]:
        if nota < 0 or nota > 10:
            print("Notas devem ser entre 0 e 10. Tente novamente.")
            validacao_da_nota = False
            break # Precisa do break para sair do loop for,
            # caso contrário, ele continua verificando as outras notas

    if not validacao_da_nota: # Se alguma nota não for válida, reinicia o loop
        continue
        
    # Se todas as notas forem válidas, calcula a média e classifica
    notas_para_media = [nota01, nota02, nota03]
    media = sum(notas_para_media) / len(notas_para_media)
    classificacao = {"Excelente": media >= 9,"Bom": media >= 7,"Razoável": media >= 5,
                        "Insuficiente": media < 5}
    # Exibe a média e a classificação correspondente
    for chave, valor in classificacao.items():
        if valor:
            print(f"A média é {media:.2f} - Classificação: {chave}")
        
    break
    





    