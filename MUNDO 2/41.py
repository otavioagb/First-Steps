idade=int(input('Digite sua idade:'))
print('De acordo com a Confederação Nacional de Nataçao, ', end='')
if idade <= 9:
    print('sua categoria é Mirin.')
elif idade >= 10 and idade <= 14:
    print('sua categoria é Infatil.')
elif idade >= 15 and idade <= 19:
    print('sua categoria é Junior.')
elif idade == 20:
    print('sua categoria é Senior.')
elif idade > 20:
    print('sua categoria é Master.')