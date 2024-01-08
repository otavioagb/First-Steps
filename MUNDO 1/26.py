frase=str(input('Digite uma frase: ').strip())
fraseA=frase.lower().count('a')
pposicao=frase.lower().find('a')+1
uposicao=frase.lower().rfind('a')+1
print(f'A letra A aparece {fraseA} vezes na frase')
print(f'A primeira letra A apareceu na posição {pposicao}')
print(f'A última letra A apareceu na posição {uposicao}')