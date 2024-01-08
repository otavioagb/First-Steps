#ler 5 valores e guardar em uma lista    OK
#mostrar o maior e o menor e suas posições  

values=[]
biggest=int(0)
lowest=int(0)

for n in range(0,5):
    values.append(int(input('Enter a number: ')))
    if n == 0:
        lowest=biggest=values[n]

    if lowest >= values[n]:
        lowest=values[n]

    if biggest <= values[n]:
        biggest=values[n]



print(values)

print(f'The biggest number: {biggest} in ', end='')
for i, v in enumerate(values):
    if v == biggest:
        print(f'{i+1}...', end='')        
print('position')

print(f'The lowest number: {lowest} in ', end='')
for i, v in enumerate(values):
    if v == lowest:
        print(f'{i+1}...', end='')
print('position')