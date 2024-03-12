from random import randint

print('='*22)
print('''Let's play odd or even''')
print('='*22)

sum=even=0

while True:

    num=int(input('Type a number: '))
    choice=input('Odd or even [O/E]? ').upper()

    comp_choice=randint(0,10)
    even=num
    total=num+comp_choice

    if total % 2 == 0:
    
        sum+=1

        print('-'*30)
        print(f'''You chose {num} and computer {comp_choice}
Total of {total} is even.''')
        print('-'*30)
        print('''You won, let's try again...''')
        print('='*30)

    else:
        print('-'*30)
        print(f'Game Over. You won {sum} times')
        break