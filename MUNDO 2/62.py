terms=10
c=1

print('='*18)
print(f'{terms} TERMS OF A A.P.')
print('='*18)
ft=int(input('Type the fist term: '))
r=int(input('Reason: '))
term=ft

while c <=10:

        print(f'{term} => ', end='')
        
        term+=r
        c+=1
print('PAUSE')

script=print('''Choose and type the desired NÚMBER:
[0] Exit
[1] Enter more terms''')
choice = int(input(''))

while choice != 0: 

    if choice == 1:

        while choice >= 1:

            print('='*18)
            print(f'{terms} TERMS OF A A.P.')
            print('='*18)

            for a in range(0,choice):
                term+=r
                print(f'{term} => ', end='')
            choice=int(input('How many terms? '))
            terms+=choice

    else:
        print('Invalid choice, try again!')
        print(script,'\n',choice)

print('END')
print('Closing...')