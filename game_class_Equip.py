class Equip:
    name = None
    type = None  # W = weapon, A = armour
    power = None

    def __init__(self, name, type, power):
        self.name = name
        self.type = type
        self.power = power


equip1 = Equip('knife', 'W', 1)
equip2 = Equip('axe', 'W', 3)
equip3 = Equip('sword', 'W', 5)
equip4 = Equip('helmet', 'A', 2)
equip5 = Equip('shield', 'A', 3)
equip6 = Equip('mail', 'A', 4)
eqp = (equip1, equip2, equip3, equip4, equip5, equip6)