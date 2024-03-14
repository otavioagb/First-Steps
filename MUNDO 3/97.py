x=['Gustavo Guanabara', 'Curso de Python no Youtube', 'CeV']

def write(y):
    
    print('='*(len(y)+4))
    print(f'  {y}')
    print('='*(len(y)+4))

for y in x:
    write(y)