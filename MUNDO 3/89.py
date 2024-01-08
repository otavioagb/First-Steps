name_grade=[]

while True:

    name=str(input('Name: '))
    grade1=float(input('1° Grade: '))
    grade2=float(input('2° Grade: '))
    average=(grade1+grade2)/2
    name_grade.append([name, [grade1, grade2], average])

    choice=str(input('Do you wanna continue [Y/N]? ')).upper().strip()
    while choice not in 'YN':
        choice=str(input('Do you wanna continue [Y/N]? ')).upper().strip()
    if choice in 'N':
        break

print('='*29)
print(f'{"N°":^4} {"Name":^16} {"Average":^7}')
print('='*29)

for i, a in enumerate(name_grade):
    print(f'{i:^4} {a[0]:^16} {a[2]:^7}')