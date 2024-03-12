num=int(input('Digite um número inteiro: '))

print('Escolha a base de conversão:')
print('(1) Binário\n(2) Octal\n(3) Hexadecimal')
tipo=int(input('Qual opção escolhida? '))

if tipo == 1:
    print(f'O {num} convertido para Binário é {bin(num)[2:]}')
elif tipo == 2:
    print(f'O {num} convertido para Octal é {oct(num)[2:]}')
elif tipo == 3:
    print(f'O {num} convertido para Hexatecimal é {hex(num)[2:]}')
else:
    print('A opção escolhida é invalida, tente novamente.')