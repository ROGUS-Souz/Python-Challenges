# Escreva um algoritmo que permita cadastrar jogos de videogame e qual sua plataforma.
# O usuário deve informar o nome do jogo e a plataforma (PS4, PS5, Xbox, Nintendo Switch).
# Crie um menu de opções contendo: Criar, Listar e Sair.
# Crie um arquivo texto para salvar os dados dos jogos cadastrados.
# Crie uma função para cada opção do menu.

# Função para validar a entrada do usuário
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

# Função verificar arquivo
def existeArquivo(nome):
    """
    Verifica se o arquivo existe.

    Parâmetros:
    nome (str): O nome do arquivo a ser verificado.

    Retorna:
    bool: True se o arquivo existir, False caso contrário."""
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

# Função Criar arquivo
def criarArquivo(nome):
    """
    Cria um arquivo com o nome fornecido.
    
    Parâmetros:
    nome (str): O nome do arquivo a ser criado.
    """
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("Houve um erro na criação do arquivo.")
    else:
        print(f"Arquivo {nome} criado com sucesso!")

# Função para criar um novo cadastro de jogo
def criarJogo(nomeArquivo):
    """
    Cria um novo cadastro de jogo e salva no arquivo fornecido.
    
    Parâmetros:
    nomeArquivo (str): O nome do arquivo onde o jogo será salvo.
    """
    nome_jogo = input("Digite o nome do jogo: ")
    plataforma = input("Digite a plataforma (PS4, PS5, Xbox, Nintendo Switch): ")
    jogo = f"{nome_jogo} - {plataforma}\n"
    try:
        a = open(nomeArquivo, 'at')
    except:
        print("Houve um erro no cadastro do jogo.")
    else:
        a.write(jogo)        
    finally:
        a.close()


# Função para Listar os jogos cadastrados
def listarJogos(nomeArquivo):
    """
    Lista os jogos cadastrados no arquivo fornecido.
    
    Parâmetros:
    nomeArquivo (str): O nome do arquivo onde os jogos estão salvos."""
    try:
        a = open(nomeArquivo, 'rt')
        
    except:
        print("Houve um erro na listagem dos jogos.")
    else:
        print(a.read())   
    finally:
        a.close()


# Laço principal do programa
arquivo = 'jogos.txt'
if existeArquivo(arquivo):
    print("Arquivo encontrado com sucesso!")
else:
    print("Arquivo não encontrado! Criando um novo arquivo...")
    criarArquivo(arquivo)

while True:
    print("Menu de Opções:")
    print("1. Criar")
    print("2. Listar")
    print("3. Sair")
    op = validaInt("Escolha uma opção (1-3): ", 1, 3)

    if op == 1:
        # Chamar a função para criar um novo cadastro de jogo
        print("Criando um novo cadastro de jogo...")
        criarJogo(arquivo)
    elif op == 2:
        # Chamar a função para listar os jogos cadastrados  
        print("Listando jogos cadastrados...")
        listarJogos(arquivo)
    elif op == 3:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")