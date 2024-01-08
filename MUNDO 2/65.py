#ler varios numeros
#no final, mostrar a media de todos os valores
#no final, escrever o maior e o menor dos valores lidos
#cotinuar ou nao? repetidas vezes

sum=num=c=bigger=smaller=0
exit=False

print('='*33)
print('Type Y to cancel or S to continue')
print('='*33)

while not exit:

    num=int(input('Type a number: '))
    sum+=num
    c+=1
    if c == 1:
        bigger = smaller = num
    else:
        if num > bigger:
            bigger = num
        if num < smaller:
            smaller = num
    choice=str(input('Do you wanna contine [Y/N]?')).upper()
    if choice == 'Y':
        exit=False
    elif choice == 'N':
        exit=True
    else:
        print('Invalid choice, try again!')
        exit=True

print(f'''The media of all summed values was {sum/c:.2f}
The smallest number is {smaller} and the largest {bigger}''')