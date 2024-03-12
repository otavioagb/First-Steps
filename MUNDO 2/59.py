from time import sleep

exit=False
maior=menor=0
choice=4

while not exit:

    if choice != 5:

        if choice == 1:
            print(f'Somando... '),sleep(1),print(f'{n1+n2}')

        elif choice == 2:
            print(f'Multiplicando... '),sleep(1), print(f'{n1*n2}')

        elif choice == 3:
            if n1 < n2:
                maior = n2
                print(f'O número {maior} é o maior')
            elif n1 > n2:
                menor = n2
                print(f'O número {n1} é o maior')

        elif choice == 4:
            n1=int(input('Digite um número: '))
            n2=int(input('Digite mais um: '))

        print('='*30)
        print("""[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa""")
        print('='*30)
        choice=int(input('Digite o NÚMERO da função desejada: '))
    
    elif choice == 5:
        exit=True
        print('Encerrando!')