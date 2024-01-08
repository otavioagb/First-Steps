def form():
    name=str(input('Name: '))
    if name == '':
        name='<unknown>'
    goals=input('Goals: ')
    if goals.isnumeric():
        goals=int(goals)
    else:
        goals=0
    return f'The player {name} scored {goals} goals'


print(form())
