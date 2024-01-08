d1=float(input('Digite uma distância com até 10 digitos:'))
d2=float(input('Digite outra distância com até 5 digitos:'))
r=d1+d2
rcm=r*1000
rmm=rcm*1000
print(f'O total foi de {r:.2f}M. ', end='')
print(f'Resultando em {rcm:.2f}Cm ', end='')
print(f'e {rmm:.2f}Mm.')
print(f'A média entre {d1} e {d2} é igual a {r/2:.2f}')   