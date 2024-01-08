teams=('','Botafogo','Bragantino','Flamengo','Palmeiras','Athletico-PR','Grêmio',
'Atlético-MG','Fortaleza','Fluminense','São Paulo','Cuiabá','Internacional','Bahia',
'Cruzeiro','Corinthians','Goiás','Vasco da Gama','Santos','Coritiba','América-MG')

print('='*25)
print('  CAMPEONATO BRASILEIRO')
print('='*25)

for a in range(1, 6):
    print(f'{a}º: ', (teams[a]))

print('-'*25)

for b in range(17,21):
    print(f'{b}º: ', (teams[b]))

print('='*25)
print('     ALFABETIC ORDER')
print('='*25)

sort=sorted(teams)
for c in range(0, 21):
    print(sort[c])

print('='*25)

choice=input('Enter a team name to discover his placement: ').capitalize()
while choice not in teams:
    choice=input('This team is not listed. Try again: ').capitalize()
    if choice in teams:
        print('-'*25)
        print('This team is on',teams.index(choice),'º position.')