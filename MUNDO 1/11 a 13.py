h=float(input('Qual a altura da sua parede?'))
l=float(input('Qual a largura dela?'))
salario=float(input('Quanto voçê ganha hoje?'))
area=h*l
tinta=area/2
ptinta=200.00
ptintadesc=ptinta*0.95
print(f'A quantidade de tinta necessaria será de {tinta:.2f}L, devido aos {area:.2f}m2. ', end='')
print(f'A tinta sendo paga à vista fica no valor de R$ {ptintadesc:.2f}, ', end='')
print(f'caso seja parcelado R$ {ptinta:.2f}.')
print(f'O valor da tinta representa {(ptinta*100)/salario:.2f}% do seu salário, ', end='')
print(f'se for pago à vista o valor representará {(ptintadesc*100)/salario:.2f}%.')