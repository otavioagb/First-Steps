def cabecalho(txt):
    print('='*40)
    print(f'{txt:^40}')
    print('='*40)

def menu(options):
    cabecalho('MAIN MENU')
    opt=1
    for option in options:
        print(f'{opt}° Option - {option}')
        opt+=1
    print('='*40)
