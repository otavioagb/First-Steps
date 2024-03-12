gendder=(input('Informe seu sexo: ')).strip().upper()[0]

while gendder not in 'MF':
    gendder = input('Dados invalidos. Por favor, informe seu sexo: ').strip().upper()[0]
    
print('Dados cadastrados com sucesso!')