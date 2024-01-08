frase=input('Digite uma frase: ').strip().upper()
palavras=frase.split()
junto=''.join(palavras)
inverso=''
print(f'Sua frase é: {junto}')
for c in range(len(junto)-1,-1,-1):
    inverso+=junto[c]
print(f'Sua frase ao contrario fica: {inverso}')
if inverso==junto:
    print('Temos um palíndromo')
else:
    print('Tente novamente')
    