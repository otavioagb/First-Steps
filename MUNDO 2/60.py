num = int(input('Digite um número: '))
exit = False
fatorial=num
for f in range(num-1,0,-1):
    fatorial*=f

while not exit:
    print(fatorial)
    exit = True
#     print('''Selecione o NÚMERO do que deseja fazer:
# [1] Escolher outro número
# [2] Encerrar o programa''')
#     choice=''
#     if choice == 1:
        
#     elif choice == 2:

#     else:
#         print('Opção invalida, tente novamente!')