import math
import random

print('Em uma aula de matemática a professora pede para você escolher quatro nomes aleatórios diferentes. ')
print('Escreva abaixo estes quatro nomes:')
n1=input('Primeiro: ').capitalize()
n2=input('Segundo: ').capitalize()
n3=input('Terceiro: ').capitalize()
n4=input('Quarto: ').capitalize()

print('='*70)
lista=[n1,n2,n3,n4]
escolhido=random.choice(lista)
angulo=float(input(f'O(a) {escolhido} será o(a) próximo(a) a escolher um número entre 1 a 360.\nAjude escolhendo um número primeiro: '))

print('='*70)
print(f'O número que você escolheu possui os seguintes valores:')
seno=math.sin(math.radians(angulo))
cosseno=math.cos(math.radians(angulo))
tangente=math.tan(math.radians(angulo))
print(f'O seno de {angulo:.0f} é {seno:.2f}, o cosseno {cosseno:.2f} e a tangente {tangente:.2f}')