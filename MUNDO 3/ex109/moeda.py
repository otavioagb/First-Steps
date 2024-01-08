def metade(num=0, f=False):
    c=num/2
    if f == True:
        return f'{"R$"}{num:.2f}'.replace('.',',')
    return c

def dobro(num=0, f=False):
    c=num*2
    if f == True:
        return f'{"R$"}{num:.2f}'.replace('.',',')
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