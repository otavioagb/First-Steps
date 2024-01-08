#digitar varios valores e inclui-los em uma lista   ok
#numeros repetidos nao sao considerados   ok 
#exibir todos os valores em ordem crescente após pausar   ok

num=[]

while True:
    
    add=int(input('Enter a number: '))

    if add not in num:
        num.append(add)
        choice=str(input('Do you want to continue [Y/N]? ')).upper().strip()
        while choice not in 'YyNn':
            choice=str(input('Do you want to continue [Y/N]? ')).upper().strip()
        if choice == 'N':
            print('='*35)
            break
    else:
        print('You already entered this number. Try again!')

org=sorted(num)
print('These are the organized numbers:')
for n in range(0, len(org)):
    print(org[n], end='-> ')
print('END')