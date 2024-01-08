def leiaint(x):
        while True:
            try:
                num=int(input(x))
            except:
                print(f'Error, only integer numbers. Please, try again!')
                continue
            else:
                return num
            
def leiafloat(x):
    while True:
        try:
            num=float(input(x))
        except:
            print(f'Error, only float numbers. Please, try again!')
            continue
        else:
            return f'{num:.1f}'
         

#Main Program
i=leiaint('Integer number: ')
r=leiafloat('Float number: ')
print(f'The integer number is {i} and float number {r}')