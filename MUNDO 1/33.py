print('Vamos escolher 3 números.')
a=int(input('Digite um número: '))
b=int(input('Digite outro: '))
c=int(input('Digite mais um: '))
menor=a
maior=a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c
print(f'O menor valor é {menor}')
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior=c
print(f'O maior valor é {maior}')