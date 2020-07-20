import random

options = []
default_game = False
name = input('Enter your name: ')
print(f'Hello, {name}')
score = 0
old_score = 0
new_usr = True
new_rating = []

with open('rating.txt', 'r') as f:
    for line in f:
        line_str = line.strip()
        line_list = line_str.split()
        if name == line_list[0]:
            new_usr = False
            score = int(line_list[1])
            old_score = int(line_list[1])


def new_user():
    with open('rating.txt', 'a') as o_file:
        o_file.write(f'{name} {score}\n')


def update_user():
    with open('rating.txt', 'r') as fin:
        for data in fin:
            data_str = data.strip()
            data_list = data_str.split()
            print(new_rating)
            if name == data_list[0]:
                new_rating.append(f'{name} {score}')
            else:
                new_rating.append(data_str)
            new_r_str = '\n'.join(new_rating)
            with open('rating.txt', 'w') as fout:
                fout.write(new_r_str + '\n')


def help_option():
    if default_game:
        game_type = 'classic version'
    else:
        game_type = 'your optional version'
    print(f'Hi, {name}. You are playing {game_type} of the game')
    print('Your available options for the game are:')
    print(options)
    print()
    print('To play a game, type one of the options')
    print('The option beats the next half of options, but loses to the previous ones')
    print('If you win, you get +100 points. Draw: +50 points. Lose: +0 points')
    print()
    print('Type "!exit" to exit your game. Your score will be added/updated to "rating.txt"')
    print('Type "!rating" to get your current score')
    print('Type "!help" to get this message one more time')


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
            else:
                update_user()
            break
        if action == '!rating':
            print(f'Your rating: {score}')
            continue
        if action == '!help':
            help_option()
            continue
        if action == 'rock' or action == 'scissors' or action == 'paper':
            if action == c_action:
                print(f'There is a draw ({action}) (+50 points)')
                score += 50
            elif action == 'rock' and c_action == 'scissors':
                print('Well done. Computer chose scissors and failed (+100 points)')
                score += 100
            elif action == 'scissors' and c_action == 'paper':
                print('Well done. Computer chose paper and failed (+100 points)')
                score += 100
            elif action == 'paper' and c_action == 'rock':
                print('Well done. Computer chose rock and failed (+100 points)')
                score += 100
            elif action == 'rock' and c_action == 'paper':
                print('Sorry, but computer chose paper')
            elif action == 'scissors' and c_action == 'rock':
                print('Sorry, but computer chose rock')
            elif action == 'paper' and c_action == 'scissors':
                print('Sorry, but computer chose scissors')
        else:
            print('Invalid input. Type "!help" for help')
elif len(options) % 2 != 0:
    while True:
        action = input()
        c_action = random.choice(options)
        if action == '!exit':
            print('Bye!')
            if new_usr:
                new_user()
            else:
                update_user()
            break
        if action == '!rating':
            print(f'Your rating: {score}')
            continue
        if action == '!help':
            help_option()
            continue
        if action in options:
            half_list = int((len(options) - 1) / 2)
            action_id = options.index(action)
            c_action_id = options.index(c_action)
            if action == c_action:
                print(f'There is a draw ({action}) (+50 points)')
                score += 50
            elif action_id + half_list <= len(options):
                if c_action_id > action_id >= c_action_id - half_list:
                    print(f'Sorry, but computer chose {c_action}')
                else:
                    print(f'Well done. Computer chose {c_action} and failed (+100 points)')
                    score += 100
            else:
                if c_action_id < action_id <= c_action_id + half_list:
                    print(f'Well done. Computer chose {c_action} and failed (+100 points)')
                    score += 100
                else:
                    print(f'Sorry, but computer chose {c_action}')
        else:
            print('Invalid input. Type "!help" for help')
elif len(options) % 2 == 0:
    while True:
        action = input()
        c_action = random.choice(options)
        if action == '!exit':
            print('Bye!')
            if new_usr:
                new_user()
            else:
                update_user()
            break
        if action == '!rating':
            print(f'Your rating: {score}')
            continue
        if action == '!help':
            help_option()
            continue
        if action in options:
            half_list = int(len(options) / 2)
            action_id = options.index(action)
            c_action_id = options.index(c_action)
            if action == c_action or action_id == c_action_id + half_list or action_id == c_action_id - half_list:
                print(f'There is a draw ({c_action}) (+50 points)')
                score += 50
            elif action_id + half_list <= len(options):
                if c_action_id > action_id >= c_action_id - half_list:
                    print(f'Sorry, but computer chose {c_action}')
                else:
                    print(f'Well done. Computer chose {c_action} and failed (+100 points)')
                    score += 100
            else:
                if c_action_id < action_id <= c_action_id + half_list:
                    print(f'Well done.Tim Computer chose {c_action} and failed (+100 points)')
                    score += 100
                else:
                    print(f'Sorry, but computer chose {c_action}')
        else:
            print('Invalid input. Type "!help" for help')
