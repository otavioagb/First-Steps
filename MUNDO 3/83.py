expression=str(input('Type an expression: '))
parentheses=[]

for s in expression:
    if s == '(':
        parentheses.append('(')

    elif s == ')':
        if len(parentheses) > 0:
            parentheses.pop()
        else:
            parentheses.append(')')
            break

if len(parentheses) == 0:
    print('Valid expression')

else:
    print('Invalid expression')