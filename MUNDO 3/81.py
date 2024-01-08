numbs=[]
cont=0

while True:

    cont+=1
    num=numbs.append(int(input('Enter a number: ')))

    choice=str(input('Do you wanna continue [Y/N]? ')).strip().upper()
    while choice not in 'YyNn':
        choice=str(input('Do you wanna continue [Y/N]? ')).strip().upper()
    if choice in 'N':
        print('These are you listed numbers:')
        print(numbs)
        break

contrary=sorted(numbs, reverse=True)

print('='*25)
print(f'''You enter {cont} elements
The list in descending order {contrary}''')
if 5 not in numbs:
    print('The elemente 5 do not shows up')
else:
    print('The elemente 5 shows up')