casa=int(input('Digite o valor da casa: '))
salario=int(input('Qual o seu salário? '))
tempo=int(input('Em quantos anos pretende pagar a casa? '))
prestacao=casa/(tempo*12)
aceito=(salario*0.3)+salario
if prestacao <= aceito:
    print('O seu empréstimo foi aceito!')
else: 
    print('O seu empréstimo foi negado!')