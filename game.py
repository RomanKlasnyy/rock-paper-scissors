import random

options = []
default_game = False
name = input('Enter your name: ')
print(f'Hello, {name}')
score = 0
new_usr = True

read_f = open('rating.txt', 'r+')
for line in read_f:
    line_str = line.split()
    if name == line_str[0]:
        score = int(line_str[1])
        new_usr = False
read_f.close()


def new_user():
    o_file = open('rating.txt', 'a')
    o_file.write(f'{name} {score}\n')
    o_file.close()


gestures = input('Press Enter for a classic game or write options separated by a comma (rock,paper,scissors,lizard)')
if gestures == '':
    options = ['rock', 'scissors', 'paper']
    default_game = True
else:
    options = gestures.split(',')

print("Okay, let's start")

if default_game is True:
    while True:
        action = input()
        c_action = random.choice(options)
        if action == '!exit':
            print('Bye!')
            if new_usr:
                new_user()
            break
        if action == '!rating':
            print(f'Your rating: {score}')
            continue
        if action == 'rock' or action == 'scissors' or action == 'paper':
            if action == c_action:
                print(f'There is a draw ({action})')
                score += 50
            elif action == 'rock' and c_action == 'scissors':
                print('Well done. Computer chose scissors and failed')
                score += 100
            elif action == 'scissors' and c_action == 'paper':
                print('Well done. Computer chose paper and failed')
                score += 100
            elif action == 'paper' and c_action == 'rock':
                print('Well done. Computer chose rock and failed')
                score += 100
            elif action == 'rock' and c_action == 'paper':
                print('Sorry, but computer chose paper')
            elif action == 'scissors' and c_action == 'rock':
                print('Sorry, but computer chose rock')
            elif action == 'paper' and c_action == 'scissors':
                print('Sorry, but computer chose scissors')
        else:
            print('Invalid input')
elif len(options) % 2 != 0:
    while True:
        action = input()
        c_action = random.choice(options)
        if action == '!exit':
            print('Bye!')
            if new_usr:
                new_user()
            break
        if action == '!rating':
            print(f'Your rating: {score}')
            continue
        if action in options:
            half_list = int((len(options) - 1) / 2)
            action_id = options.index(action)
            c_action_id = options.index(c_action)
            if action == c_action:
                print(f'There is a draw ({action})')
                score += 50
            elif action_id + half_list <= len(options):
                if c_action_id > action_id >= c_action_id - half_list:
                    print(f'Sorry, but computer chose {c_action}')
                else:
                    print(f'Well done. Computer chose {c_action} and failed')
                    score += 100
            else:
                if c_action_id < action_id <= c_action_id + half_list:
                    print(f'Well done. Computer chose {c_action} and failed')
                    score += 100
                else:
                    print(f'Sorry, but computer chose {c_action}')
        else:
            print('Invalid input')
elif len(options) % 2 == 0:
    while True:
        action = input()
        c_action = random.choice(options)
        if action == '!exit':
            print('Bye!')
            if new_usr:
                new_user()
            break
        if action == '!rating':
            print(f'Your rating: {score}')
            continue
        if action in options:
            half_list = int(len(options) / 2)
            action_id = options.index(action)
            c_action_id = options.index(c_action)
            if action == c_action or action_id == c_action_id + half_list or action_id == c_action_id - half_list:
                print(f'There is a draw ({c_action})')
                score += 50
            elif action_id + half_list <= len(options):
                if c_action_id > action_id >= c_action_id - half_list:
                    print(f'Sorry, but computer chose {c_action}')
                else:
                    print(f'Well done. Computer chose {c_action} and failed')
                    score += 100
            else:
                if c_action_id < action_id <= c_action_id + half_list:
                    print(f'Well done.Tim Computer chose {c_action} and failed')
                    score += 100
                else:
                    print(f'Sorry, but computer chose {c_action}')
        else:
            print('Invalid input')
