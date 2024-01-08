print('='*21)
print('10 TERMOS DE UMA P.A.')
print('='*21)
pt=int(input('Digite o primeiro termo: '))
r=int(input('Razão: '))
termo=pt
c=1
while c <=10:
    print(f'{termo} => ', end='')
    termo+=r
    c+=1
print('FIM')