# Verificar se um número é primo: 
# Implemente um programa que verifique se um número é primo, 
# ou seja, se é divisível apenas por 1 e por ele mesmo.

total=0
number=int(input('Enter a number: '))

for x in range(number, 0, -1):
    if number % x == 0:
        total+=1
    else:
        continue

if total >= 3:
    print(f"{number} isn't a prime number")
else:
    print(f"{number} is a prime number")