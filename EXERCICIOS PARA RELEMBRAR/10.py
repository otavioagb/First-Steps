# Calcular o valor do juros compostos: 
# Desenvolva uma função que calcule o valor final de um investimento 
# com base em uma taxa de juros e um período de tempo.

# m=c*(1+i)^t

starting_capital=float(input('Starting capital: '))
tempo_meses=int(input('Months: '))
tax=float(input('Tax: '))
real_tax=tax/100

calculo_taxa=(1+real_tax)**tempo_meses
calculo_montate=calculo_taxa*starting_capital

print(f'R$ {calculo_montate:.2f}')