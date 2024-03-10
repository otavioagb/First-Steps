cidade=str(input('Onde você nasceu? ')).strip().lower()

cidade1=cidade.split()

print('Sua cidade termina com Santo?',(cidade1[-1] == 'santo'))