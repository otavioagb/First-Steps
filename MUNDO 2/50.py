soma=0

for seis in range (6):
    num=int(input('Digite um número: '))
    if num%2==0:
        soma+=num
        
print(f'A soma dos número pares foi {soma}')