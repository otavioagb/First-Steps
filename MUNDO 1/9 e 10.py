n=float(input('Digite quanto você possui de patrimônio: R$ '))

nd=float(n/4.86) 
nr=float(n*4.86)

print(f'Você possui {nd:.2f} em dólares')
print(f'Para possuir nominalmente o mesmo tanto em dolares precisa-se de R$ {nr:.2f}')
n2=(n*2)
n3=(n*3)
n4=(n*4)
n5=(n*5)
n6=(n*6)
n7=(n*7)
n8=(n*8)
n9=(n*9)
print('Aqui está quando você teria caso duplicasse, triplicasse... seu patrimônio:')
print(f' {n2}\n {n3}\n {n4}\n {n5}\n {n6}\n {n7}\n {n8}\n {n9}')