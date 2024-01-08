#  cadastrar em um dict: nome, ano de nascimento (convertendo para idade),
#  se tem numero carteira de trabalho (Y/N), se diferente de N 
#  ler ano de contratação e salário. Calcular tempo de aposentadoria 
#  considerenado 35 anos contribuição
from datetime import datetime

data={'name':str(input('Name: ').strip()),
      'age':int(input('Year of birth: ')),
      'ctps':str(input('CTPS [Y/N]: ').strip().upper())}
if data['ctps'] != 'N':
    data['retire']=int(input('Year of contract: '))
    data['remuneration']=float(input('Remuneration: '))
    data['retire']=(data['retire']-data['age'])+35
data['age']=datetime.now().year - data['age']
for k, v in data.items():
    if v == '':
        break
    print(f'The {k} has value {v}') 