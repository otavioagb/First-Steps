from ex109 import moeda

#parametro com moeda personalizavel, ex 'U$'
#parametro personalizavel para moeda, ex: de 100.0 para 'R$100,00'

p=float(input('Number: R$'))
print(f'The half of {moeda.moeda(p)} is {moeda.metade(p)}')
print(f'The double of {moeda.moeda(p)} is {moeda.dobro(p)}')
print(f'Increasing 10%, we have {moeda.aumentar(p, 10)}')
print(f'Decreasing 13%, we have {moeda.diminuir(p, 13)}')

