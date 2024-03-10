salario=int(input('Digite seu salário: '))

salario10=salario*0.1+salario
salario15=salario*0.15+salario

if salario >= 1250:
    print(f'Você terá um aumento de {salario10}')
else:
    print(f'Você terá um aumento de {salario15}')