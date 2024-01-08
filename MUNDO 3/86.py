matriz=[ [] , [] , [] ]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c]=int(input(f'Enter a vulue for [{l}, {c}]: '))

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^3}]', end='')
    print('')