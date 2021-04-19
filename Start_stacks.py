from Units import *


class Unit_stacks:
    def __init__(self):
        self.stack = []

    def castle_stack(self, player_numb_):
        unit1 = Footman()
        unit1.quantity = 25
        unit1.player_numb = player_numb_
        unit2 = Archer()
        unit2.quantity = 20
        unit2.player_numb = player_numb_

        unit3 = Berserker()
        unit3.quantity = 7
        unit3.player_numb = player_numb_

        self.stack.append(unit1)
        #self.stack.append(unit2)
        #self.stack.append(unit3)

    def demon_stack(self, player_numb_):
        unit1 = Imp()
        unit1.quantity = 45
        unit1.player_numb = player_numb_
        unit2 = Demon()
        unit2.quantity = 15
        unit2.player_numb = player_numb_

        unit3 = Cerberus()
        unit3.quantity = 4
        unit3.player_numb = player_numb_

        self.stack.append(unit1)
        self.stack.append(unit2)
        self.stack.append(unit3)

    def necro_stack(self, player_numb_):
        unit1 = Skeleton_warrior()
        unit1.quantity = 35
        unit1.player_numb = player_numb_

        unit2 = Ghost()
        unit2.quantity = 16
        unit2.player_numb = player_numb_

        unit3 = Vampire()
        unit3.quantity = 4
        unit3.player_numb = player_numb_

        #self.stack.append(unit1)
        self.stack.append(unit2)
        #self.stack.append(unit3)
