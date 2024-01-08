#Soma dos valores pares
#Soma dos valores da terceira linha
#O maior valor da segunda linha

matriz=[ [] , [] , [] ]
sum=column=biggest_line2=0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Enter a number for [{l},{c}]: ')))
        if matriz[l][c] % 2 == 0:
            sum+=matriz[l][c]

print()

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^3}]', end='')
    print('')

print('='*30)

#A
print(f'The total of even typed numbers is {sum}')

#B
for l in range(0, 3):
    column+=matriz[l][2]
print(f'The total in the thirth column is {column}')

#C
for c in range(0, 3):
    if c == 0:
        biggest_line2 == matriz[1][c]
    elif matriz[1][c] > biggest_line2:
        biggest_line2 = matriz[1][c]
print(f'The biggest value of second line is {biggest_line2}')