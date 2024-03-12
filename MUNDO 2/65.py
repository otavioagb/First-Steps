sum=num=c=higger=lowest=0
exit=False

print('='*33)
print('Type N to cancel or Y to continue')
print('='*33)

while not exit:

    num=int(input('Type a number: '))

    sum+=num
    c+=1

    if c == 1:
        higger = lowest = num
    else:
        if num > higger:
            higger = num
        if num < lowest:
            lowest = num

    choice=str(input('Do you wanna contine? [Y/N] ')).upper()

    if choice == 'Y':
        exit=False
    elif choice == 'N':
        exit=True
    else:
        print('Invalid choice, try again!')
        exit=True

print(f'''The average of all summed values was {sum/c:.2f}
The lowest number is {lowest} and the higger {higger}''')