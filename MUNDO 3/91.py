from random import randint
from time import sleep
from operator import itemgetter

dice_moves={'Player 1':randint(1,6),
            'Player 2':randint(1,6),
            'Player 3':randint(1,6),
            'Player 4':randint(1,6)}
ranking=[]
print('Drawed numbers:')
for k, v in dice_moves.items():
    print(f'{k} drew: {v}')
    sleep(1)
ranking=sorted(dice_moves.items(), key=itemgetter(1), reverse=True)
for k, v in enumerate(ranking):
    print(f'{k+1}° position: {v[0]} with {v[1]}')
