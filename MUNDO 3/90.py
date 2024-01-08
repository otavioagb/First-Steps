data={}

data['name']=str(input('Name: '))
data['average']=float(input('Average: '))
if data['average'] >= 7:
    data['situation']='Approved'
else:
    data['situation']='Disapproved'

print('='*22)

print(f'''Name: {data["name"]}
Average: {data["average"]}
Situation: {data["situation"]}''')

print('='*22)