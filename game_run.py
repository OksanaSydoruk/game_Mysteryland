""" Создать класс Битва. Добавить туда участников, проверку их типа и состояния, цикл битвы """

"""Соберите всю вашу игру в файлики, для каждого класса свой файл (юнит, оборудование, битва и тд...).
Создайте файл game.py в который импортируйте нужные вам классы и реализуйте запуск игры :
создание юнитов, создание оборудования, одевание оборудования на юнита, создание и запуск битвы.

Все это выкладывайте на github. А сюда на проверку давайте не файлик, а ссылку на ваш публичный репозиторий)

* По желанию - продумайте классы-наследники Юнита:
Рыцарь - Всегда атакует превым
Маг - Перед каждой атакой колдует заклинание (или увеличивает свою атаку, или понижает защиту цели на установленный %).
Вампир - при каждой атаке добавляет к своему здоровью часть (%) от нанесенного противнику урона
Все это выкладывайте на github. А сюда на проверку давайте не файлик, а ссылку на ваш публичный репозиторий)"""

import random

from game_class_Unit import *
from game_class_Equip import *
from game_class_Battle import *
from game_dialogs import *

from game_class_Unit import Unit
from game_class_Equip import Equip
from game_class_Battle import Battle


print ('')
print ('************************   WELCOME TO MYSTERYLAND   ************************')
print ('')


# Choose your character-----------------------------
unit_played = char_select()


# Choose your destination-----------------------------
# Get character assigned for battle (from characters existing in selected destination)
chars = list(destination_select(unit_played))
numb_char = random.randint(0,(len(chars)-1))
char_fighting = chars[numb_char]
print ('')
print (f'****{unit_played.name} meets {char_fighting.name}****')
print ('')
print ('')

# Start battle with character in selected place-----------------------------
battle_a = Battle(unit_played, char_fighting , 50)
winner = battle_a.fight()


# If battle won, winner gets new weapon or armour -----------------------------

numb_eqp = random.randint(0,len(eqp))
winner.eqp = eqp[numb_eqp]









