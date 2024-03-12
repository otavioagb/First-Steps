print('='*30)
print('10 TERMOS DE UMA P.A.'.center(30))
print('='*30)

f_t=int(input('Digite o primeiro termo: '))
r=int(input('Razão: '))

term=f_t
c=1

while c <=10:
    print(f'{term} => ', end='')
    term+=r
    c+=1
print('FIM')