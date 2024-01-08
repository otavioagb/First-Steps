num=('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
'onze','doze','treze','quatorze ou catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

choice=int(input('Enter a number: '))
while True:
    if choice < 0 or choice > 20:
        choice=int(input('Invalid númber, try again. Enter a number: '))
    else:
        break
print(num[choice].capitalize())