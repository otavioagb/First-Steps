print('='*40)
print('CASH MACHINE'.center(40))
print('='*40)

w=int(input('Withdraw INTEGER value: R$ '))

total=w
ced=50
totalced=0

while True:
    
    if total >= ced:
        total -= ced
        totalced+=1

    else:
        
        if totalced > 0:
           print(f'Total of {totalced} notes of R$ {ced} ')

        if ced == 50:
           ced = 20

        elif ced == 20:
           ced = 10

        elif ced == 10:
           ced = 1

        totalced = 0

        if total == 0:
           break
