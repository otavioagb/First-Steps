def cont(b):
    global a
    a=8
    b+=4
    c=2
    print(f'''A dentro vale {a}
B dentro vale {b}
C dentro vale {c}''')


a=5
cont(a)
print(f'\nA fora vale {a}')