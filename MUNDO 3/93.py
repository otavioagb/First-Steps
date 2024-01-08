data={'name':str(input('Name: ').strip().capitalize())}
match=int(input(f'Hoy many matches does {data["name"]} played: '))
data['goals']=[]
total=0

for goals in range(1, (match+1)):
    data['goals'].append(int(input(f'How many goals at the match {goals}: ')[:]))

for x in data['goals']:
    total+=x
data['total']=total

print('='*25)

for k, v in data.items():
    print(f'The {k} has value {v}')

print('='*25)

print(f'{data["name"]} played {match} matches.')
for k, v in enumerate(data['goals']):
    print(f'=> On match {k+1}, he did {v} goals.')
