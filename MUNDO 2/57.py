sex=(input('Informe seu sexo: ')).strip().upper()[0]
while sex not in 'MmFf':
    sex = input('Dados invalidos. Por favor, informe seu sexo: ').strip().upper()[0]
print('Dados cadastrados com sucesso!')