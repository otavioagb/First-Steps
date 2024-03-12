from random import randint

comp=randint(0, 10)

print('Vamos tentar advinhar um número entre 0 e 10.')

got_it = False
guesses = 0

while not got_it:

    player = int(input('Qual é o seu palpite? '))
    guesses += 1

    if player == comp:
        got_it = True
    else:
        if player < comp:
            print('Mais, tente de novo')
        elif player > comp:
            print('Menos, tente de novo')

print(f'Parabéns, você got_it em {guesses} tentativas')