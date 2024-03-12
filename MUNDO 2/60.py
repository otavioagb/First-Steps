print('='*20)
print('Fatoração'.center(20))
print('='*20)

num = int(input('Digite um número: '))

exit = False
fatorial=num

for f in range(num-1,0,-1):
    fatorial*=f

while not exit:
    print(fatorial)
    exit = True