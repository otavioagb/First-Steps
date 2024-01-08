print('Defina três valores para descobrir qual tipo de triângulo será formado.')
a=int(input('1° valor: '))
b=int(input('2° valor: '))
c=int(input('3° valor: '))
if a == b == c:
    print('O triângulo é equilátero.')
elif a != b != c:   
    print('O triângulo é escaleno')
else:
    print('O triângulo é isósceles.')
