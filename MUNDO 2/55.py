maior=menor=0

print('-'*28)
for c in range(1,6):
    peso=float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
    print('-'*28)

print(f'''O maior peso lido foi de {maior:.2f}
O menor peso lido foi de {menor:.2f}''')