datas=[]
average=sum=0
    
while True:

    data={'name':str(input('Name: ').capitalize().strip()),
          'gender':str(input('Gender [M/F]: ').upper()),
          'age':int(input('Age: '))}
    datas.append(data)
    choice=str(input('Do you wanna continue [Y/N]: ').upper())
    while choice not in 'YN':
        choice=str(input('Do you wanna continue [Y/N]: ').upper())
    sum+=data['age']
    if choice == 'N':
        break

print('='*30)

#A
if len(datas) >= 1:
    print(f'The group has {len(datas)} person')
else:
    print(f'The group has {len(datas)} people')
print('-'*30)

#B
print(f'The age average is {sum/len(datas):.2f}')
print('-'*30)

#C
print('Women in the group:')
for x in datas:
    if x['gender'] in 'F':
        print(f'{x["name"]}', end=' => ')
print('END')
print('-'*30)

#D
print('People above average age:')
for x in datas:
    if x['age'] >= sum/len(datas):
        print(f'{x["name"]}', end=' => ')
print('END')
print('-'*30)