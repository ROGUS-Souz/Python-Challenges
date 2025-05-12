# Desafio 6: Gerenciador de Senhas
#Objetivo:
#Criar um sistema que valide senhas de usuário com regras específicas.
#O programa deve pedir uma senha repetidamente até que todas as regras sejam atendidas.
#Regras da Senha:
#Ter no mínimo 8 caracteres. len(senha) >= 8
#Conter pelo menos 1 letra maiúscula e 1 minúscula. .upper() e .lower()
#Ter pelo menos 1 número. .isdigit()
#Incluir 1 caractere especial (!@#$%^&*). .isalpha()
#Não permitir espaços. isspace()
#Requisitos do Código:
#Use um loop while para pedir a senha até ser válida.
#Utilize if/elif/else para verificar cada regra.
#Mostre mensagens de erro específicas (ex.: "Falta letra maiúscula").
#Ao acertar, exiba: "Senha válida! ✅".
# .isupper() # Verifica se contém letra maiúscula
# .islower() # Verifica se contém letra minúscula
# .isdigit() # Verifica se contém número
# .isalpha() # Verifica se contém caractere especial
# .isspace() # Verifica se contém espaço
# .isalnum() # Verifica se contém apenas letras e números
print('''Bem-vindo ao Gerenciador de Senhas!
Você deve criar uma senha que atenda às seguintes regras:
1. Ter no mínimo 8 caracteres.
2. Conter pelo menos 1 letra maiúscula e 1 minúscula.
3. Ter pelo menos 1 número.
4. Incluir 1 caractere especial (!@#$%^&*)
5. Sem espaços.''')

while True:
    senha = input("Digite uma senha: ")
    erro = False
    
    # Verifica comprimento
    if len(senha) < 8:
        print("A senha deve ter no mínimo 8 caracteres.")
        erro = True
    
    # Verifica se tem pelo menos 1 minúscula
    if not any(c.islower() for c in senha):
        print("A senha deve conter pelo menos 1 letra minúscula.")
        erro = True
        
    # Verifica se tem pelo menos 1 maiúscula
    if not any(c.isupper() for c in senha):
        print("A senha deve conter pelo menos 1 letra maiúscula.")
        erro = True
        
    # Verifica se tem pelo menos 1 número
    if not any(c.isdigit() for c in senha):
        print("A senha deve conter pelo menos 1 número.")
        erro = True
        
    # Verifica se tem pelo menos 1 caractere especial
    especiais = '!@#$%^&*'
    if not any(c in especiais for c in senha):
        print("A senha deve conter pelo menos 1 caractere especial (!@#$%^&*).")
        erro = True
        
    # Verifica se tem espaços
    if any(c.isspace() for c in senha):
        print("A senha não pode conter espaços.")
        erro = True
        
    # Se não houve erros, senha é válida
    if not erro:
        print("Senha válida! ✅")
        break

