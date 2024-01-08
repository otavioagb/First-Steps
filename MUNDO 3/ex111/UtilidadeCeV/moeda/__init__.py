def metade(num=0, f=False):
    c=num/2
    if f == True:
        return f'{"R$"}{c:.2f}'.replace('.',',')
    return c

def dobro(num=0, f=False):
    c=num*2
    if f == True:
        return f'{"R$"}{c:.2f}'.replace('.',',')
    return c

def aumentar(num=0, taxa=0, f=False):
    c=num+(num*taxa/100)
    if f == True:
        return f'{"R$"}{c:.2f}'.replace('.',',')
    return c

def diminuir(num=0, taxa=0, f=False):
    c=num-(num*taxa/100)
    if f == True:
        return f'{"R$"}{c:.2f}'.replace('.',',')
    return c

def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.',',')

def resumo(num=0, taxaa=10, taxar=5):
    print('='*32)
    print(f'{"VALUE RESUM":^32}')
    print('='*32)

    print(f'Analyzed price: \t{moeda(num):}')
    print(f'Doble of price: \t{dobro(num, True)}')
    print(f'Half of price:\t\t{metade(num, True)}')
    print(f'{taxaa}% of increase:\t{aumentar(num, taxaa, True)}')
    print(f'{taxar}% of reduction:\t{diminuir(num, taxar, True)}')

    print('='*32)