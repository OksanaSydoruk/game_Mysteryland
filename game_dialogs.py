
from game_class_Unit import *
from game_class_Unit import Unit

def char_select():
    # Choose your character
    print('Here are the characters you can play for: ')
    for unit in players:
        print(f'***{unit.name}:    attack strength: {unit.att}, defence strength: {unit.df}, code: {unit.code}')

    print('')
    print('To choose a character, please enter its code')
    print('To exit, type N')
    print('')
    response1 = input('Your choice:   ')

    selected = 0
    while len(response1) > 0 and selected == 0:
        for unit in players:
            if response1 == unit.code:
                print(f'Welcome, {unit.name}')
                unit_played = unit
                selected = 1
                break
            elif response1 == 'N':
                print('Bye! Hope to see you soon in Mysteryland')
                selected = 1
                break
            else:
                continue
        if selected == 0:
            response1 = input('Please enter character code letter, or N to exit the game:  ')
    return unit_played

def destination_select(unit_played):
    # Choose your destination
    print('')
    print('')
    print('If you go to the Forest, you can meet: ')
    for chr in fr_chars:
        print(f'***{chr.name}:    attack strength: {chr.att}, defence strength: {chr.df}')
    print('')

    print('If you go to the Mountain, you can meet: ')
    for chr in mt_chars:
        print(f'***{chr.name}:    attack strength: {chr.att}, defence strength: {chr.df}')
    print('')

    print('')
    print('Where do you want to go?  Forest - F, Mountain - M')
    print('To exit, type N')
    print('')
    response2 = input('Your choice:   ')

    selected = 0
    while len(response2) > 0 and selected == 0:
        if response2 == 'M':
            print(f'{unit_played.name} is going to the Mountain')
            chars = list(mt_chars)
            selected = 1
            break
        elif response2 == 'F':
            print(f'{unit_played.name} is going to the Forest')
            chars = list(fr_chars)
            selected = 1
            break
        elif response2 == 'N':
            print('Bye! Hope to see you soon in Mysteryland')
            selected = 1
            break
        else:
            response2 = input('Please enter letter for place, or N to exit the game:  ')

    return chars