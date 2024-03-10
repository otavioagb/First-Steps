nome=str(input('Digite seu nome: '))
tam_nome=len(nome) - nome.count(' ')
nome_lista=nome.split()

print('Seu nome em maiúsculo é:', nome.upper())
print('Seu nome em minúsculo é:', nome.lower())
print(f'O nome completo possui {tam_nome} caracteres.')
print(f'O primeiro nome possui {len(nome_lista[0])} caracteres')