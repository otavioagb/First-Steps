print('Defina três valores para validar a formação de um triângulo.')
a=int(input('1° valor: '))
b=int(input('2° valor: '))
c=int(input('3° valor: '))

menorQ=a

print('='*40)
if a<b+c and b<a+c and c<a+b:
    print('É possivel formar um triângulo')
else:
    print('Não é possivel formar um triângulo')
