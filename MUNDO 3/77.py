tupla=('celular', 'infantil', 'idoso', 'abelha')
vogal='aeiou'
for word in tupla:
    print(f'\nFor word {word} we have: ', end='')
    for lyric in word:
        if lyric in vogal:
            print(lyric, end='')
print('')