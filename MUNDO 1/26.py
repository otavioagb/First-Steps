frase=str(input('Digite uma frase: ')).strip().lower()

fraseA=frase.count('a')
pposicao=frase.find('a')+1
uposicao=frase.rfind('a')+1

print('='*45)
print(f'A letra A aparece {fraseA} vezes na frase')
print(f'A primeira letra A apareceu na posição {pposicao}')
print(f'A última letra A apareceu na posição {uposicao}')