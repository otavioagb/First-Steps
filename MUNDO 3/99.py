from random import randint
from time import sleep


def biggest(t):

    print('='*25)
    print('Analyzing past data:')

    biggest=0

    for x in range(0, t):
        
        num=randint(0, 10)

        if x == 0:
            biggest=num
        else:
            if num >= biggest:
                biggest=num
        print(num, end=' => ')

    print('END')
    print(f'''It was informed {t} values 
The biggest number was {biggest}''')
    sleep(2)

biggest(6)
biggest(3)
biggest(2)
biggest(1)
biggest(0)