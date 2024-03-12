c=sum=0

print('='*18)
print('Type 999 to cancel')
print('='*18)

while True:

    num=int(input('Type a number: '))

    if num == 999:
        break
    
    c+=1
    sum+=num

print(f'The sum of {c} numbers was {sum}')
