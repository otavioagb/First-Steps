valor=float(input('Digite o valor dos produtos:' ))

print('Estas são as formas de pagamento:')
print('''[1] Dinheiro/Cheque - 10% de desconto
[2] À vista no cartão - 5% de desconto
[3] Em até 2x no cartão - Preço normal
[4] 3x ou mais no cartão - 20% de juros''')
pag=int(input('Qual a forma de pagamento:'))

if pag == 1:
    print(f'Total R$ {valor*0.9:.2f}')
elif pag == 2:
    print(f'Total R$ {valor*0.95:.2f}')
elif pag == 3:
    print(f'Total R$ {valor:.2f}')
elif pag == 4:
    print(f'Total R$ {valor*1.2:.2f}')
else: 
    print('Opção invalida, tente novamente.')