def metade(num=0):
    c=num/2
    return c

def dobro(num=0):
    c=num*2
    return c

def aumentar(num=0, taxa=0):
    c=num+(num*taxa/100)
    return c

def diminuir(num=0, taxa=0):
    c=num-(num*taxa/100)
    return c

def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.',',')