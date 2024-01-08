def area(larg, comp):
    a = larg * comp
    print(f'{larg} x {comp} = {a}')

print('='*19)
print(F'{"LAND AREA":^19}')
print('='*19)
l=float(input('Width: '))
c=float(input('Length: '))
area(l, c)