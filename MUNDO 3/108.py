from ex108 import moeda

#parametro com moeda personalizavel, ex 'U$'

p=float(input('Number: R$ '))

print(f'The half of {moeda.moeda(p)} is {moeda.moeda(moeda.metade(p))}')
print(f'The double of {moeda.moeda(p)} is {moeda.moeda(moeda.dobro(p))}')
print(f'Increasing 10%, we have {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Decreasing 13%, we have {moeda.moeda(moeda.diminuir(p, 13))}')