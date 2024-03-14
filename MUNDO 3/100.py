from random import randint
from time import sleep 


def draw(x):

    print(f'These are the drawed numbers:')

    for h in range(0, 5):
        x.append(randint(0, 10))
        print(x[h], end=' => ', flush=True)
        sleep(0.3)
    print('END')
    print('='*29)
    sleep(2)   

def even_numbers(x):

    sum=0

    for h in x:
        if h % 2 == 0:
            sum+=h
            
    print(f'''The total of EVEN numbers is: 
             {sum}
{"="*29}''')

num=[]
draw(num)
even_numbers(num)
