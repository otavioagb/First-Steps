num=int(input('Digite um número até 9999:'))
u=num//1%10
d=num//10%10
c=num//100%10
m=num//1000%10
print(f'De acordo com o número escolhido, {num}, temoos:')
print(f'A unidade {u}')
print(f'A dezena {d}')
print(f'A centena {c}')
print(f'O milhar {m}')