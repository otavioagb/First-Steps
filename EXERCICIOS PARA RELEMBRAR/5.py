# Verificar se uma palavra é um palíndromo: 
# Implemente um programa que verifique se uma palavra é um palíndromo, ou seja,
# se pode ser lida da mesma forma tanto da esquerda para a direita quanto da direita para a esquerda.

word=str(input('Enter a word: '))
reverse_word=[]
normal_word=[]

for x in word[::-1]:
    reverse_word.append(x)

for x in word:
    normal_word.append(x)

if reverse_word == normal_word:
    print('This word is a palindrome')
else:
    print('This word is not a palindrome')