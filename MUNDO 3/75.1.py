# a - vezes que apaceram o num 9
# b - posição do primeiro 3
# c - quais numeros digitados sao pares

tupla=(int(input('Enter a number: ')),
int(input('Another number: ')),
int(input('One more: ')),
int(input('The last one: ')))

print('='*30)

print(f'You enter the numbers {tupla}')
if 9 not in tupla:
    print('The number 9 not showed up')
elif 9 in tupla:
    print(f'The value 9 showed up {tupla.count(9)} times')

if 3 not in tupla:
    print('The number 3 not showed up')
elif 3 in tupla:
    print(f'The first value 3 showed up {tupla.index(3)+1}º position')

print('The even numbers is:')
cont=0
for n in tupla:
    if n % 2 == 0:
        cont+=1
        print(n, end=' ')
if cont <= 0:
    print('There is no even numbers')
print('')