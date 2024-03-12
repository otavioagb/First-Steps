num1=int(input('Digite um número: '))
num2=int(input('Digite outro número: '))

if num1 < num2:
    print(f'O segundo valor é maior.')
elif num1 > num2:
    print(f'O primeiro valor é maior.')
elif num1 == num2:
    print('Ambos números são iguais.')