def fatorial(n, show=False):
    sum=1
    for x in range(n, 1, -1):  
        sum*=x 
    if show == True:
        for x in range(n, 1, -1):
           print(f'{x} x ', end='')
        return f'1 = {sum}'
    else:
        return sum

print(fatorial(9, True))