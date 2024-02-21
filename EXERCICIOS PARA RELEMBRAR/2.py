# Verificar se um número é par ou ímpar: 
# Desenvolva um programa que receba um número como entrada e determine se ele é par ou ímpar.

from random import randint

num=randint(0,1000)
if num % 2 == 0:
    print(f'The number {num} is an even number.')
else:
    print(f'The number {num} is an odd number')