print('-'*24)
print('SEQUENCE DE FIBONACCI'.center(24))
print('-'*24)

num=int(input('How many terms do you wanna display? '))

t1=0
t2=1
cont=3

print(f'{t1} -> {t2}', end='')
while cont <= num:
    t3 = t2 + t1
    print(f' -> {t3}', end='')
    t1=t2
    t2=t3
    cont += 1
print(' -> END')