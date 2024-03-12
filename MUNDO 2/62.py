terms=10
c=1

print('='*22)
print(f'{terms} TERMS OF AN A.P.'.center(22))
print('='*22)

f_t=int(input('Type the fist term: '))
r=int(input('Reason: '))
print('-'*70)

term=f_t

while c <=10:

        print(f'{term} => ', end='')
        term+=r
        c+=1

print('PAUSE')

print('-'*70)
script=print('''[0] Exit
[1] Enter more terms''')
choice = int(input('Choose and enter the desired NÚMBER: '))

while choice != 0: 

    if choice == 1:

        while choice >= 1:

            print('='*22)
            print(f'{terms} TERMS OF A A.P.'.center(22))
            print('='*22)

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