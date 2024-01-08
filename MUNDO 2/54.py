#ler o ano de nascimento de 7 pessoas 
#depois mostrar quantas não atingiram a maioridade e quantas ja
maior=0
menor=0
for c in range(1,8):
    ano=int((input('Digite o ano que nasceu: ')))
    idade = 2023 - ano
    if idade < 18:
        menor+=1
    elif idade > 18:
        maior+=1
print(f'{maior} pessoas são maior(es) de idade e {menor} menor(es) de idade.')

   
