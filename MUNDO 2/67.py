print('='*34)
print(' Type a negative number to cancel')

while True:
    print('='*34)
    num=int(input('A multiplication table number: '))
    print('='*34)
    if num < 0:
        print('Closing...')
        break
    for m in range(0,11):
        print(f'{num} x {m} = {num*m}')
    