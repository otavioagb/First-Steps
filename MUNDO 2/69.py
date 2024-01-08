#quantos total + 18
#quntos homens total
#quanta mulheres menos de 20

sum_more18=sum_m=sum_yless20=0

while True:
    print('='*23)
    print('   REGISTER A PERSON')
    print('='*23)

    age=int(input('Age: '))
    if age > 18:
        sum_more18+=1
    sex=' '
    while sex not in 'MW':
        sex=input('Sex [M/W]: ').upper().strip()
    if sex == 'M':
        sum_m+=1    
    if sex == 'W' and age < 20:
        sum_yless20+=1

    choice=' '
    while choice not in 'YN':
        choice=input('Continue? [Y/N] ').upper().strip()
    if choice == 'N':
        break

print('='*23)
print(f'''\nMore 18y: {sum_more18} 
Total men: {sum_m}
Yomen less 20y: {sum_yless20}

CLOSING...''')



