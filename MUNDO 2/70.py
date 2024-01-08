#ler o nome e o preço de varios produtos
#deve perguntar se tem mais produtos
#mostrar o gasto total
#quantos produtos custam acima de 1000
#qual o nome do produto mais barato

total=product_1000=lowest=cont=0
cheaper=''

print('='*24)
print('        SHOPPING')

while True:

    print('='*24)
    (product)=str(input('Product name: ')).strip().upper()
    price=float(input('Price:  R$ '))
    total+=price
    cont+=1

    if price > 1000:
        product_1000+=1

    if cont == 1:
        cheaper=product
        lowest=price
    else:
        if price < lowest:
            cheaper=product
            lowest=price

    choice=' '
    while choice not in 'YN':
        choice=str(input('More products? [Y/N] ')).strip().upper()
    if choice == 'N':
        break

print('='*24)
print('     TOTAL SHOPPING')
print('='*24)
print(f'''Total of shopping: R$ {total:.2f}
Products above R$ 1000,00: {product_1000} product(s)
The cheaper product was {cheaper} it cost R$ {lowest:.2f}''')