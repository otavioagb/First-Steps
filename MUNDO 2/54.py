maior=menor=0

print('='*23)
print('Digite o ano que nasceu')
print('='*23)

for c in range(1,8):
    ano=int((input(f'{c}° Pessoa: ')))
    idade = 2023 - ano
    if idade < 18:
        menor+=1
    elif idade > 18:
        maior+=1
    print('-'*23)

print(f'{maior} pessoas são maior(es) de idade e {menor} menor(es) de idade.')

   
