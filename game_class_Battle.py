
import random
import time

class Battle:
    def __init__(self, ch1, ch2, attacks):
        self.ch1 = ch1
        self.ch2 = ch2
        self.attacks = attacks

    def fight(self):
        sametype = (type(self.ch1) == type (self.ch2))
        print('')
        print (f'-----------------------BATTLE BETWEEN {self.ch1.name} and {self.ch2.name} -----------------------')
        time.sleep(1)
        live = (self.ch1.hp > 0 and self.ch2.hp > 0)
        if live and sametype:
            while self.attacks > 0:
                units = [self.ch1, self.ch2]
                starting = random.randint(0,1)
                first = units[starting]
                del(units[starting])
                second = units[0]
                first.attack(second)
                time.sleep(0.3)
                self.attacks -=1
        if self.ch1.hp > 0:
            winner = self.ch1
        else:
            winner = self.ch2
        return winner
