'''
This script is a command line implemented game for guessing a random number between a range.
The lower and upper bounds of the range are the first and second arguments of the command line, respectively.
The user then continues to guess integers within the range
'''


import sys
from random import randint


command_line_arguments = sys.argv
print(command_line_arguments)

command_line_passed = False
try:
    if len(command_line_arguments) == 3:
        lower = int(command_line_arguments[1])
        upper = int(command_line_arguments[2]) + 1
        print(f'The lower range of the guessing game is {lower}')
        print(f'The upper range of the guessing game is {upper}')
        command_line_passed = True
except SystemError:
    print('This script requires two command line arguments: the lower and upper range of the guessing game.')

if command_line_passed:
    mystery_number = randint(lower, upper)
    
    
    def enter_guess(g):
        print(f'Your guess was {g}')
        if type(g) == int:
            if g in list(range(lower, upper)):
                if g == mystery_number:
                    print('Do do doooo! You won the game you champ, you!')
                else:
                    print('w-wu-waaaughwow. What a shame! Maybe give it another go?')
            else:
                print('This number is out of range')
    
    
    while True:
        try:
            guess = int(input(f'Guess a number between {lower} and {upper}:  '))
            g = enter_guess(guess)
            if guess == mystery_number:
                break
        except ValueError:
            print('That\'s not a number, silly!')
        finally:
            print('You have completed your game. Feel free to play again any 
