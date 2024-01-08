var=[]
var_even=[]
var_odd=[]


while True:

    num=var.append(int(input('Enter a number: ')))
    choice=str(input('Do you wanna continue [Y/N]: ')).strip().upper()
    while choice not in 'YN':
        choice=str(input('Do you wanna continue [Y/N]: ')).strip().upper()
    if choice == 'N':
        break

for c in range(0, len(var)):
    if var[c] % 2 == 0:
        var_even.append(var[c])
    else:
        var_odd.append(var[c])

print(f'''The listed numbers was: {var}
The even numbers: {var_even}
the odd numbers: {var_odd}''')