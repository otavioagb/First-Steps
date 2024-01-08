def leiadinheiro(num):
    while True:
        entrada=str(input(num)).replace('.',',').strip()
        if entrada.isalpha() or entrada=='':
            print(f'ERRO: Preço \"{entrada}\" inválido, tente novamente!')
        else:
            return float(entrada)   