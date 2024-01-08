import random
num=random.randrange(0,5)
print('O computador pensará em um número de 0 a 5.')
chute=int(input('Tente adivinhar qual seria:'))
if chute == num:
    print('Você venceu!')
else:
    print('Você perdeu!')
print(f'O número escolhido foi {num}')