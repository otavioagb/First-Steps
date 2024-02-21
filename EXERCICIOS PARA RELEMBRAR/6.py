# Contar a quantidade de vogais em uma palavra: 
# Desenvolva uma função que receba uma palavra como entrada 
# e retorne a quantidade de vogais presentes na palavra.

sum=0
list_word=[]
word=str(input('Enter a word: ')).lower()

for y in word:
    list_word.append(y)

for x in list_word:
    if x in 'aeiou':
        sum+=1

print(sum)
