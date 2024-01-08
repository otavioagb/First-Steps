from random import randint
print('Jogaremos Pedra, Papel e Tesoura')
print('=_' * 5 + '=')
print('''[0] Pedra
[1] Papel
[2] Tesoura''')
print('=_' * 5 + '=')
escolha=int((input('Sua jogada: ')))
tipo=('pedra','papel','tesoura')
computador=randint(0,2)
tipo_texto=tipo[computador]

if computador == 0: #pedra
    if escolha == 0:
        print(f'Empate, o computador escolheu {tipo_texto}')
    elif escolha == 1:
        print(f'Vitória, o computador escolheu {tipo_texto}')
    elif escolha == 2:
        print(f'Derrota, o computador escolheu {tipo_texto}')
    else:
        print('Jogada inválida, tente novamente.')

elif computador == 1: #papel
    if escolha == 0:
        print(f'Vitória, o computador escolheu {tipo_texto}')
    elif escolha == 1:
        print(f'Empate, o computador escolheu {tipo_texto}')
    elif escolha == 2:
        print(f'Derrota, o computador escolheu {tipo_texto}')
    else:
        print('Jogada inválida, tente novamente.')

elif computador == 2: #tesoura
    if escolha == 0:
        print(f'Vitória, o computador escolheu {tipo_texto}')
    elif escolha == 1:
        print(f'Derrota, o computador escolheu {tipo_texto}')
    elif escolha == 2:
        print(f'Empate, o computador escolheu {tipo_texto}')
    else:
        print('Jogada inválida, tente novamente.')