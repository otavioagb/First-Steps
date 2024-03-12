soma_idade=media_idade=maior_idade=total_mulheres_menos_20=0
name_older=''

for p in range(1,5):

    print('-'*5, f'{p}ª PESSOA', '-'*5)

    name=str(input('Nome: ')).strip()
    age=int(input('Idade: '))
    sex=str(input('Sexo [M/F]: ')).strip()

    soma_idade+=age

    if p == 1 and sex in 'Mm':
        maior_idade = age
        nome = name_older
    if sex in 'Mm' and age > maior_idade:
        maior_idade = age
        name_older = name
    if sex in 'Ff' and age < 20:
        total_mulheres_menos_20+=1

media_idade = soma_idade/4

print('='*50)
print(f'A média de idade do grupo é de {media_idade} anos')
print(f'O homem mais velho tem {maior_idade} anos e se chama {name_older}')
print(f'Ao todo têm {total_mulheres_menos_20} que possuem menos de 20 anos.')