data_list=list()
data=list()
heaviest=lightest=0

while True:

    #READING
    data.append(input('Name: '))
    data.append(float(input('Weight: ')))

    #LOGIC
    if len(data_list) == 0:
        heaviest=lightest=data[1]
    else:
        if data[1] > heaviest:
            heaviest = data[1] 
        if data[1] < lightest:
            lightest = data[1]

    #COMMANDS
    data_list.append(data[:])
    data.clear()

    #MENU CONTINUE
    choice=str(input('Do you wanna continue [Y/N]? ')).upper().strip()
    while choice not in 'YN':
        choice=str(input('Do you wanna continue [Y/N]? ')).upper().strip()
    if choice == 'N':
        break

#RESOLUTIONS

#A
print(f'It was registered {len(data_list)} people')

#B
print('The haviest was ', end='')
for p in data_list:
    if p[1] == heaviest:
        print(f'({p[0]})', end=' ')
print(f', with {heaviest}KG')

#C
print('The lightest was ', end='')
for p in data_list:
    if p[1] == lightest:
        print(f'({p[0]})', end=' ')
print(f', with {lightest}KG')