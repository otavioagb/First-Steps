# Calcular o fatorial de um número: 
# Crie uma função que calcule o fatorial de um número dado como entrada. #numero*antecessor>0

def fatorial(number):
    sum=1
    for x in range(number, 0, -1):
        sum*=x
    print(sum)

number=int(input('Enter a number: '))  
fatorial(number)