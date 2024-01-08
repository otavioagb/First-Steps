print('Olá, tudo bem?')
input('Como foi sua viagem?')
km=float(input('Gostaria de saber quantos Km você andou com o carro:'))
dias=float(input('Quanto tempo o carro ficou alugado?'))
temp=float(input('Estava muito quente? Quantos graus °C estava quando você o alugou?'))
f=((9*temp)/5)+32
total=(dias*20) + (km*0.5)
print(f'Nesse dia estavam {f}°F. Espero que tenha tomado bastante água.')
print(f'O carro ficou no total de R$ {total}.')