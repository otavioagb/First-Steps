nota1=float(input('Digite a primeira nota: '))
nota2=float(input('A segunda: '))

media=(nota1+nota2)/2

if media < 5.0:
    print(f'Você ficou abaixo da média, sua media foi {media}, sendo 4.9 a referência.')
elif media >= 5.0 and media < 7.0 :
    print(f'Você está de recuperação, sua media foi {media}, sendo 5.0 a 6.9 a referência.')
elif media >= 7.0:
    print(f'Você está aprovado, sua media foi {media}, sendo a referência superior ou igual a 7.0')