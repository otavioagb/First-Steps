#ler varios numeros 
#parar quando escrever 999 
#somar quantas tentativas
#somar todos os numeros digitados

print('''While you do not hit the number, the game do not will stop!
Clue: Same numbers''')

soma=0
total_sum=0
num=''

while num != 999:
    num=int(input('Type a number: '))
    soma+=1
    total_sum+=num

print(f'''You hit it in {soma} tries
The sum of all the numbers was {total_sum-999} deconsidering the flag 999''')