num=int(input('Digite um número: '))

for c in range(0,10):
    print(f'{c} x {num} = ', end='')
    print(num*c)