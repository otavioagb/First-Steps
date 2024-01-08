print('-'*29)
print('        PRICE LISTING')
print('-'*29)
lista=('pencil', 1,
       'pen', 3,
       'cellphone', 500,
       '4x glasses', 10)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<19}', end='')
    else:
        print(f'R$ {lista[pos]:>7.2f}')
print('-'*29)