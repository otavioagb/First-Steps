# O programa de deve perguntar quantos jogos serão gerados
# Cada jogo deve conter 6 números entre 1 e 60
# Os números não podem se repetir
# Tudo em uma lista composta

from random import randrange
from time import sleep

total_of_games=[]

print('='*21)
print(f'{"MEGA SENA":^21}')
print('='*21)

choice=int(input('How many games: '))

for games in range(0, choice):
    temp=[]
    for game in range(0, 6):
        random=randrange(1, 60)
        if random not in temp:
            temp.append(random)           
        if len(temp) == 6:
            total_of_games.append(temp)
            del(temp)
print('='*21)

for pos, g in enumerate(total_of_games):
    print(f'{pos+1}° Game: {sorted(g)}')
    sleep(1)