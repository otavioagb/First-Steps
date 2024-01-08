from random import randint
comp=randint(0, 10)
print('Vamos tentar advinhar um número entre 0 e 10.')
acertou = False
palpites = 0
while not acertou:
    player = int(input('Qual é o seu palpite? '))
    palpites += 1
    if player == comp:
        acertou = True
    else:
        if player < comp:
            print('Mais, tente de novo')
        elif player > comp:
            print('Menos, tente de novo')
print(f'Parabéns, você acertou em {palpites} tentativas')