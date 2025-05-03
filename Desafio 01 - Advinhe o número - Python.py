# Crie um jogo onde o programa gera um número aleatório entre 1 e 100, 
# e o usuário tem 5 tentativas para adivinhar. A cada palpite, o programa 
# deve dizer se o número correto é maior ou menor. Use while, if/elif/else, 
# e break se acertar antes das 5 tentativas.

import random

a = random.randint(1,100)
b = 0
print('Bem-vindo ao jogo de adivinhação!')
print('Eu escolhi um número entre 1 e 100. Você tem 5 tentativas para adivinhar.')

while b < 5:
   try:
        c = int(input('Advinhe um número entre 0 e 100: '))
   except ValueError: # Se o número não for um inteiro, não permite que o erro pare o programa.
        print('Por favor, insira um número inteiro.')
        continue # Verifica se o número é um número inteiro. Retorna ao início do loop se não for.
   if c < 0 or c > 100:
        print('Número fora do intervalo. Tente novamente.')
        continue # Verifica se o número está dentro do intervalo permitido.  Retorna ao início do loop se não for.
   
   b +=1

   if a == c:
     print('Acertou o número era ' + str(a) + '!') # Pode ser escrito dessa forma (f'Acertou o número era {a}!')
     print('Você acertou em ' + str(b) + ' tentativas!')
     break
   elif a!= c:
        print('Errou, tente novamente')     
   if c < a:
        print('O número secreto é MAIOR que', c)
   else:
        print('O número secreto é MENOR que', c)
   if 1 <= a and a <= 10:
     print('Seu numero esta entre 1 e 10')
   elif 11 <= a and a <= 20:
        print('Seu numero esta entre 11 e 20')
   elif 21 <= a and a <= 30:
        print('Seu numero esta entre 21 e 30')
   elif 31 <= a and a <= 40:
        print('Seu numero esta entre 31 e 40')
   elif 41 <= a and a <= 50:
        print('Seu numero esta entre 41 e 50')
   elif 51 <= a and a <= 60:
        print('Seu numero esta entre 51 e 60')
   elif 61 <= a and a <= 70:
        print('Seu numero esta entre 61 e 70')
   elif 71 <= a and a <= 80:
        print('Seu numero esta entre 71 e 80')
   elif 81 <= a and a <= 90:
        print('Seu numero esta entre 81 e 90')
   elif 91 <= a and a <= 100:
        print('Seu numero esta entre 91 e 100')     

if b == 5 and a != c:
        print('Numero de tentativas excedido!' + ' O número era ' + str(a))
        print('Você perdeu!')
else:
        print('Vamos jogar novamente?')