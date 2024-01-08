vel=int(input('Qual a velocidade atual do carro? '))
mul=float((vel-80)*7)
if vel <= 80:
    print('Continue assim! Tenha um bom dia!')
else:
    print('Multado! Você ultrapassou o limite de 80km/h.')
    print(f'Você deve pagar uma multa de R$ {mul:.2f}')