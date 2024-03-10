ano=int(input('Digite algum ano: '))

if ano in range(0,10000000, 4):
    print('Esse é um ano bissexto.')
else:
    print('Esse não é um ano bissexto.')