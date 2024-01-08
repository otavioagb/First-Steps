def readint(x):
    while True:
        y=input(x)
        if y.isnumeric():
            return y 
        print('Invalid number, try again!')

#Main program
n=readint('Number: ')
print(f'You just already to enter the number {n}')  