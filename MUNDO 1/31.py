dist=int(input('Quanto km terão a sua viagem? '))
preco=dist*0.5
preco1=dist*0.45
print('Viagens superiores a 200Km tem o valor de R$ 0,45 por Km, ', end='')
print('já as inferiores no valor de R$ 0,50.\nSendo assim:')
if dist <= 200:
    print(f'O valor da sua passagem é de R$ {preco}')
else:
    print(f'O valor da sua passagem é de R$ {preco1}')