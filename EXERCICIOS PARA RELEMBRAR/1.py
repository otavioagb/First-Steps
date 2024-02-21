# Calcular a média de uma lista de números: 
# Crie um programa que receba uma lista de números e retorne a média dos valores presentes na lista.

from random import randint

numbers=[]
cont=sum=0

while True:
    numbers.append(randint(0,1000))
    cont+=1
    if cont == 10:
        break
for x in numbers:
    sum+=x

average=sum/cont

print(f'The drawned numbers was:\n{numbers}\nThe total is {sum}\nThe average is {average}')