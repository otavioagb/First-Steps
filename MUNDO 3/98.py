#funcao contador recebe inicio, fim e passo
# A) De 1 a 10, de 1 em 1                          usar o sleep para todos
# B) De 10 a 0, de 2 em 2
# C) Contagem personalziada, inicio, fim e passo

#OBS: Numeros negativos funcionam igual os positivos
#     0 considera 1
#     Caso o intervalo passe do fim encerra o anterior

from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p=1
    print('='*21)
    print(f'De {i} a {f} de {p} em {p}:')
    print('='*21)
    sleep(2)

    if i <= f:
        cont = p
        while i < f:
            print(i, end=' => ', flush=True)
            sleep(0.5)
            i+=cont
        print('FIM')     

    elif i>=f:
        cont=p
        while i > f:
            print(i, end=' => ', flush=True)
            sleep(0.5)
            i-=cont
        print('FIM')

contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é sua vez de escolher os números: ')
i=int(input('Inicio: '))
f=int(input('FIM: '))
p=int(input('Passo: '))
contador(i, f, p)