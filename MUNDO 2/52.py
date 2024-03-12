num=int(input('Digite um número: '))

total=0

for c in range(1,num+1): #Não é primo

    if num % c == 0:
        print('\033[33m',end='')
        total+=1

    else: #É primo  
        print('\033[31m',end='')
    print(f'{c} ', end='')

print(f'\n\033[mO número {num} foi divisível {total} vezes.')
if total == 2:
    print(f'E por isso ele É PRIMO.')
else:
    print(f'E por isso ele NÃO É PRIMO.')