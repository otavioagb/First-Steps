# Ordenar uma lista em ordem crescente: 
# Crie uma função que receba uma lista de números como entrada
# e retorne a mesma lista ordenada em ordem crescente.

numbers_list=[]

for x in range(1,6):
    choice=int(input(f'{x}° Number: '))
    numbers_list.append(choice)

print(sorted(numbers_list))
