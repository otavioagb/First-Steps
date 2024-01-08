import math
a=int(input('Digite a medida do cateto oposto:'))
b=int(input('Digite a medida do cateto adjacente:'))
c=(b)**2+(a)**2
c1=int(math.sqrt(c))
print(f'A parte inteira da hipotenusa é {c1:.3f}cm.')
