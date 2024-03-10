dist=int(input('Quanto km terão a sua viagem? '))

preco1=dist*0.5
preco2=dist*0.45

print('='*60)
print('Viagens superiores a 200Km tem o valor de R$ 0,45 por Km.')
print('Já as inferiores no valor de R$ 0,50.\nSendo assim:')

if dist <= 200:
    print(f'  => O valor da sua passagem é de R$ {preco1}')
else:
    print(f'  => O valor da sua passagem é de R$ {preco2}')