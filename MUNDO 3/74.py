from random import randint

menor=1
print('='*23)
tupla=((randint(1,10)),(randint(1,10)),(randint(1,10)),(randint(1,10)),(randint(1,10)))
print('The chose numbers was:')
print('='*23)
for n in tupla:
    print(n, end=' - ')
print('END')

print('='*23)
print(f'''The biggest number is {max(tupla)}
The lowest number is {min(tupla)}''')
