

import random
from game_class_Equip import Equip

class Unit:
    name = None
    hp = None # Health points
    att = None # Attack strength
    df = None # Defence points
    eqp = None # Equipment

    def __init__(self, name = None, hp = 0, att = 0, df = 0, code = None, place = None):
        self.name = name
        self.hp = hp
        self.att = att
        self.df = df
        self.code = code
        self.place = place

    @ property
    def eqp(self):
        return self._eqp

    @eqp.setter
    def eqp(self, a):
        if not isinstance(a, Equip):
            raise Exception('Equipment should be an object of Equip type')
        else:
            self._eqp = a
            print ('')
            print(f'Equipment available for {self.name}:  {self.eqp.name}')
            if self.eqp.type == 'W':
                self.att += self.eqp.power
                print(f'{self.name} now has weapon: {self.eqp.name}, +{self.eqp.power} attack points')
            elif self.eqp.type == 'A':
                self.df += self.eqp.power
                print(f'{self.name} now has armour:  {self.eqp.name}, +{self.eqp.power} defence points')
            print('-----------------------------------')
            return self.att, self.df

    def attack(self, other):
        """Attacking character has attack points and chance of double-strength attack.
        Attacked character has defence points and chance of escaping from attack.
        Attacked character losses in health points = attack points minus defence points.
        If randomly assigned to escape an attack, attacked character does not lose any health points"""
        live = (self.hp > 0 and other.hp > 0)
        sametype = (type(self) == type (other))

        if live and sametype:
            self.double_att = random.randint(1, 15)
            other.escape_att = random.randrange(1, 5)
            print(f'{other.name} attacked by {self.name}')
            if other.escape_att != 1:
                if self.double_att == 1:
                    self.att = self.att * 2
                other.hp -= self.att
                other.hp += other.df
                print (f'{self.name} attack strength: {self.att}, {other.name} defence: {other.df}')
                print (f' minus {self.att-other.df} health points from {other.name}')
            else:
                print(f'{other.name} escaped from {self.name} attack')
            print (f'{other.name} now has {other.hp} health points')
            if self.hp <= 0:
                print('')
                print (f'*******************  {self.name} killed, {other.name} wins!!!!!!!!!!')
            if other.hp <= 0:
                print('')
                print(f'*******************  {other.name} killed, {self.name} wins!!!!!!!!!!')
            print ('--------------')
        return other.hp


# players
Unit1 = Unit('Knight', 100, 12, 2, 'K')
Unit2 = Unit('Dark Queen', 100, 5, 10, 'Q')
players = (Unit1, Unit2)

# Forest characters
Unit3 = Unit('Magician', 200, 3, 2, 'Forest')
Unit4 = Unit('Vampire', 200, 3, 2, 'Forest')
fr_chars = (Unit3, Unit4)

# Mountain characters
Unit5 = Unit('Dragon', 100, 15, 4, 'Mountain')
Unit6 = Unit('Orc', 50, 20, 10, 'Mountain')
mt_chars = (Unit5, Unit6)