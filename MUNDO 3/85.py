#LER 7 VALORES E CADASTRA-LOS EM UMA LISTA
#SEPARA-LOS DENTRO DA LISTA ENTRE PARES E IMPARES
#NO FINAL MOSTRA OS PARES E IMPARES EM ORDEM CRESCENTE 

num_even_odd = [ [] , [] ]

for v in range(1, 8):
    num=int(input(f'Enter the {v}° number: '))
    if num % 2 == 0:
        num_even_odd[0].append(num)
    else:
        num_even_odd[1].append(num)

num_even_odd[0].sort()
num_even_odd[1].sort()

print('The even numbers is: ')
for n in num_even_odd[0]:
        print(n, end=' -> ')
print('END')

print('The odd numbers is: ')
for n in num_even_odd[1]:
        print(n, end=' -> ')
print('END')