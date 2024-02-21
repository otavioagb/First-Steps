# Encontrar o maior elemento em uma lista: 
# Escreva um programa que encontre o maior elemento em uma lista de números.

numbers=[]
biggest=0

for x in range(1, 6):
    choice=int(input(f'{x}° Number: '))
    numbers.append(choice)
    if x == 1:
        biggest=choice
    else:
        if choice > biggest:
            biggest = choice 

print(numbers)
print(biggest)