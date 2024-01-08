from ex115.modulos.interface import *
from ex115.modulos.file import *
from time import sleep

file='data.txt'
msg=['Show registered people', 'Register a new person', 'Exit the system']
options=['REGISTERED PEOPLE', 'NEW PERSON', 'EXITING']

print('-'*40)
find_file(file)
if find_file(file) == True:
    print(f'File \"{file}\" found successfully')
else:
    create_file(file)
sleep(1)

choice=True
while True:
    try:
        menu(msg)
        choice=int(input('Your choice: '))
    except (ValueError):
        print('ERROR! Only menu numbers: ')
        continue
    else:
        sleep(1)
        cabecalho(options[choice-1])
    if choice == 1:
        read_file(file)
    elif choice == 2:
        name=str(input('Name: ')).strip().title()
        age=int(input('Age: '))
        new_person(file, name, age)
    else:
        choice=True
    sleep(2)