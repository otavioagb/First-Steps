def grades(sit=False):
    
    cont=biggest=lowest=average=0
    grades=[]
    data={}
    
    while True:

        cont+=1

        grade=float(input(f'Grade {cont}: '))
        grades.append(grade)

        if cont == 1:            
            biggest = grade
            lowest = grade
            
        elif cont != 1:
            if grade >= biggest:
                biggest = grade     
            elif grade <= lowest:
                lowest = grade

        choice=str(input('Continue [Y/N]? ')).strip().upper()

        while choice not in 'YN':
            choice=str(input('Continue [Y/N]? ')).strip().upper()

        if choice == 'N':
            average=sum(grades)/cont
            data['Total']=cont
            data['Biggest']=biggest
            data['lowest']=lowest
            data['Average']=average
            break

    if sit:

        if average >= 7:
            sit='Good'
            data['Situation']= sit
        elif average < 7 and average >= 5:
            sit='Ok'
            data['Situation']= sit
        else:
            sit='Bad'
            data['Situation']= sit
            
    return data

print(grades())