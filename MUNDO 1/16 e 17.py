import math

b=int(input('Digite a medida do cateto oposto: '))
c=int(input('Digite a medida do cateto adjacente: '))

a=(b**2)+(c**2)
c1=int(math.sqrt(a))

print(f'A parte INTEIRA da hipotenusa é {c1}cm.')