# Crie um sistema de login com senha pré-definida (ex.: "python123"). 
# O usuário tem 3 tentativas. A cada erro, mostre "Senha incorreta. 
# Tentativas restantes: X". Se acertar, mostre "Acesso permitido". 
# Se esgotar as tentativas, mostre "Conta bloqueada". 
# Use `for in range(3)` e `break` se acertar.

senha = 1234

while True:
    try:
        login = int(input('Qual a senha? '))
    except ValueError:
        print('Só permitido números')  
    for i in range(4,-1,-1):
        if i == 1:
            print('Conta Bloqueada')
        elif login != senha:
            i = i - 1
            print('Senha incorreta')
            print(f'Você tem mais {i} chances.')
            login = int(input('Qual a senha? '))
        elif login == senha:
            print('Acesso permitido')
    break