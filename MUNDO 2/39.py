ano=int(input('Qual seu ano de nascimento? '))

idade=2023-ano  
anos=18-idade 
anos1=idade-18

if idade == 18:
    print(f'Quem nasceu em {ano} tem {idade} anos, é hora de se alistar.')
elif idade <= 17:
    print(f'Quem nasceu em {ano} tem {idade} anos. Você ainda se alistará, faltam {anos} anos para se alistar.')
elif idade >= 19:
    print(f'Quem nasceu em {ano} tem {idade} anos. Você deveria ter se alistado há {anos1} anos.')