#perguntar o valor a ser sacado, deve ser inteiro
#deve retornar o numero de cedulas a serem entregues
#50, 20, 10 e 1

print('='*24)
print('      CASH MACHINE')
print('='*24)

w=int(input('Withdraw value:  R$ '))
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
