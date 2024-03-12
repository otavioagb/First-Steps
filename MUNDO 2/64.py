print('='*60)
print("While you don't hit the number, the game don't will stop!")
print('='*60)
print('Clue: Same numbers''')
print('-'*60)

soma=total_sum=0
num=''

while num != 999:
    num=int(input('Enter a number: '))
    soma+=1
    total_sum+=num

print('-'*60)
print(f'''You hit it in {soma} tries
The sum of all the numbers was {total_sum-999} deconsidering the flag 999''')