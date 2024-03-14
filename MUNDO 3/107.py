from ex107 import moeda


p=float(input('Number: R$ '))
print(f'The half of {p} is {moeda.metade(p)}')
print(f'The double of {p} is {moeda.dobro(p)}')
print(f'Increasing 10%, we have {moeda.aumentar(p, 10)}')
print(f'Decreasing 13%, we have {moeda.diminuir(p, 13)}')