#ler 5 valores e cadastra-los em uma lista    ok 
#coloca-los em ordem a cada digitação sem usar o SORT    ok 
#apresentar em qual posicao o numero esta a cada valor digitado 

list_num=[]

for n in range(0, 5):
    
    num=int(input('Enter a number: '))
    if n == 0 or num > list_num[-1]:
        list_num.append(num)
        print('This is the last number')
    else:
        pos=0
        while pos < len(list_num):
            if num <= list_num[pos]:
                list_num.insert(pos, num)
                print(f'Add in {pos}º position')
                break
            pos+=1

print('='*30)
print(list_num)