def find_file(txt):
    try:
        a = open(f'MUNDO 3/ex115/{txt}', 'rt')
        a.close()
    except (FileNotFoundError):
        return False
    else:
        return True
    
def create_file(file):
    try:
        a = open(f'MUNDO 3/ex115/{file}', 'wt+')
    except:
        print('Error creating file')
    else:    
        print(f'File \"{file}\" create successfully')
        a.close()

def read_file(file):
    try:
        a=open(file, 'rt')
    except:
        print('Error reading file!')
    else:
        for line in a:
            dado=line.split(';')
            dado[1]=dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>4} years')
    finally:
        a.close()

def new_person(file, name='unknown', age=0):
    try:
        a=open(file, 'at')
    except:
        print('Error opening file!')
    else:
        a.write(f'{name};{age}\n')
        print(f'{name} registered successfully')
    finally:
        a.close()
