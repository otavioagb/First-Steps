def vote():

    year=int(input('When were you born? '))

    res=2023-year

    if res < 18:
        return f'With {res} years old: {"DENIED VOTE"}'
    elif res >= 18 and res <= 70:
        return f'With {res} years old: {"MANDATORY VOTE"}'
    else:
        return f'With {res} years old: {"OPTIONAL VOTE"}'
print('')

print(vote())