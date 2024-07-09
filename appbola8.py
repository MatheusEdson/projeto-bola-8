import random

ball = """
   _________
  /-        \   \
  
 / --      - \   \
 
[[   ( 8 )   ]]
 \--       --/
  \-       -/
   ---------
"""
print(ball)
name = input('"A bola mágica pergunta seu nome" \n Diga seu nome:  ')

question = input('\n "A bola mágica vai responder sua pergunta" \n Diga sua pergunta: ')
answer = ""

random_number = random.randint(1, 9)
# print(random_number)

if random_number == 1:
  answer = "Claro que sim!"
elif random_number == 2:
  answer = "Você pode contar com isso!"
elif random_number == 3:
  answer = "Sem duvida!"
elif random_number == 4:
  answer = "Hmm, não tenho certeza!"
elif random_number == 5:
  answer = "Pergunte novamente mais tarde!"
elif random_number == 6:
  answer = "Melhor não te dizer agora!"
elif random_number == 7:
  answer = "Minhas fontes dizem que não!"
elif random_number == 8:
  answer = "Definitivamente não!"
elif random_number == 9:
  answer = "Depende de você!"
else:
  answer = "Error"


print( '\n "' + name + '"' + " Pergunta: " + question)

print( '\n "A bola mágica diz:" '+ '\n"'+ answer + '"')