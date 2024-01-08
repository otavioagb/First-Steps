import math
import random  
print('Em uma aula de matemática a professora pede para você escolher quatro nomes diferentes. ')
print('Escreva abaixo estes quatro nomes:')
n1=input('Primeiro:')
n2=input('Segundo:')
n3=input('Terceiro:')
n4=input('Quarto:')
lista=[n1,n2,n3,n4]
escolhido=random.choice(lista)
angulo=float(input(f'O(a) {escolhido} será o(a) próximo(a) a escolher um número entre 1 a 360, ajude escolhendo um número primeiro:'))
print(f'O número que você escolheu possui os seguintes valores:')
seno=math.sin(math.radians(angulo))
cosseno=math.cos(math.radians(angulo))
tangente=math.tan(math.radians(angulo))
print(f'O seno de {angulo:.0F} é {seno:.2f}, o cosseno {cosseno:.2f} e a tangente {tangente:.2f}')