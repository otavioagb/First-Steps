from random import randint

types = ('rock', 'paper', 'scisors')

winning_results = [
    [0, 2],
    [1, 0],
    [2, 1]
]

computer_choice = randint(0, 2)
user_choice = int(input('''
Your choice: 
[0]: rock
[1]: paper
[2]: scisors

R:'''))

print(f'[COMP] {types[computer_choice]} vs {types[user_choice]} [YOU]')

if (computer_choice == user_choice):
    print('Draw! :(')
elif [user_choice, computer_choice] in winning_results:
    print('Winnner winner chicken dinner :) :)')
else:
    print('Sorry, you lost!')