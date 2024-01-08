# ler o nome do jogador
# ler quantas partidas ele jogou
# ler quantos gols por partida e salvar em um lista 
# somatorio de gols
# escolher se continua ou não

# tabular usando as próprias keys do dicionário
# apresentar codigo, nome, gols (lista), total

# ler um menu que escolhe um jogador para apresentar 
# o aproveitamento por partida tendo o flag com o numero 999

player={}
matches=[]
team=[]

while True:

    player.clear()
    player['Name']=str(input('Name: ')).strip().capitalize()
    tot = int(input(f'How many matches does {player["Name"]} played? '))
    matches.clear()
    for c in range(1, tot+1):
        matches.append(int(input(f'  => How many goals at the match {c}? ')))
    player['Goals']=matches[:]
    player['Total']=sum(matches)
    team.append(player.copy())
    choice=str(input('Do you wanna continue [Y/N]? ')).strip().upper()
    while choice not in 'YN':
        choice=str(input('Do you wanna continue [Y/N]? ')).strip().upper()
    if choice == 'N':
        break

print('='*30)
print(f'{"Code":^4}{"Name":^11}{"Goals":^10}{"Total":^5}')
print('='*30)

for k, v in enumerate(team):
    print(f'{k:^4}', end='')
    print(f'{str(v["Name"]):^11}{str(v["Goals"]):^10}{str(v["Total"]):^5}')
    print('-'*30)
    
while True:

    search=int(input('Enter the player code number or 999 to exit: ').strip())
    if search == 999:
        break
    while search < 0 or search > len(team)-1:  
        print('Invalid number! Only code numbers in the range.')
        search=int(input('Enter the player code number or 999 to exit: ').strip())
        if search == 999:
            break
    else:
        print(f'Datas from {team[search]["Name"]}:')
        for pos, value in enumerate(team[search]["Goals"]):
            print(f'   -On {pos}° match, {value} goals')