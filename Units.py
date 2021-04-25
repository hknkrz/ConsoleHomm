import math
import random


class unit:
    def __init__(self):
        self.hitpoint = 0
        self.current_hitpoint = 0
        self.speed = 0
        self.damage = 0
        self.quantity = 0
        self.price = 0
        self.player_number = -1
        self.name = "Empty"
        self.type = "Empty"

    def deal_damage(self):
        pass

    def take_damage(self, damage: int):
        if self.hitpoint * (self.quantity - 1) + self.current_hitpoint <= damage:
            print(self.name, "perish")
            return True
        else:
            self.current_hitpoint -= damage % self.hitpoint
            self.quantity -= damage // self.hitpoint
            print(self.name, " takes ", damage, " damage")
            return False


class Imp(unit):
    def __init__(self):
        super().__init__()
        self.hitpoint = 8
        self.current_hitpoint = 8
        self.speed = 4
        self.damage = 2
        self.quantity = 1
        self.price = 40
        self.player_number = -1
        self.name = "Imp"
        self.type = "Melee"

    def deal_damage(self):
        return math.ceil(self.damage * self.quantity * (1 + (random.randrange(100) - 50) / 100))


class Demon(unit):
    def __init__(self):
        super().__init__()
        self.hitpoint = 25
        self.current_hitpoint = 25
        self.speed = 5
        self.damage = 4
        self.quantity = 1
        self.price = 160
        self.player_number = -1
        self.name = "Demon"
        self.type = "Melee"

    def deal_damage(self):
        return math.ceil(self.damage * self.quantity * (1 + (random.randrange(40) - 20) / 100))


class Cerberus(unit):
    def __init__(self):
        super().__init__()
        self.hitpoint = 35
        self.current_hitpoint = 35
        self.speed = 8
        self.damage = 10
        self.quantity = 1
        self.price = 270
        self.player_number = -1
        self.name = "Cerberus"
        self.type = "Melee"

    def deal_damage(self):
        return math.ceil(self.damage * self.quantity * (1 + (random.randrange(30) - 15) / 100))


class Pit_fiend(unit):
    def __init__(self):
        super().__init__()
        self.hitpoint = 65
        self.current_hitpoint = 65
        self.speed = 6
        self.damage = 20
        self.quantity = 1
        self.price = 550
        self.player_number = -1
        self.name = "Pit_fiend"
        self.type = "Melee"

    def deal_damage(self):
        return math.ceil(self.damage * self.quantity * (1 + (random.randrange(50) - 25) / 100))


class Devil(unit):
    def __init__(self):
        super().__init__()
        self.hitpoint = 150
        self.current_hitpoint = 150
        self.speed = 18
        self.damage = 35
        self.quantity = 1
        self.price = 1300
        self.player_number = -1
        self.name = "Devil"
        self.type = "Melee"

    def deal_damage(self):
        return math.ceil(self.damage * self.quantity * (1 + (random.randrange(10) - 5) / 100))


class Skeleton_warrior(unit):
    def __init__(self):
        super().__init__()
        self.hitpoint = 13
        self.current_hitpoint = 13
        self.speed = 3
        self.damage = 3
        self.quantity = 1
        self.price = 70
        self.player_number = -1
        self.name = "Skeleton_warrior"
        self.type = "Melee"

    def deal_damage(self):
        return math.ceil(self.damage * self.quantity * (1 + (random.randrange(80) - 40) / 100))


class Ghost(unit):
    def __init__(self):
        super().__init__()
        self.hitpoint = 22
        self.current_hitpoint = 22
        self.speed = 7
        self.damage = 5
        self.quantity = 1
        self.price = 140
        self.player_number = -1
        self.name = "Ghost"
        self.type = "Melee"

    def deal_damage(self):
        return math.ceil(self.damage * self.quantity * (1 + (random.randrange(20) - 10) / 100))

    def take_damage(self, damage: int):
        if random.randrange(100) < 20:
            print("Ghosts evade hit!")
            return False
        else:
            return super().take_damage(damage)


class Vampire(unit):
    def __init__(self):
        super().__init__()
        self.hitpoint = 40
        self.current_hitpoint = 40
        self.speed = 9
        self.damage = 10
        self.quantity = 1
        self.price = 400
        self.player_number = -1
        self.name = "Vampire"
        self.type = "Melee"

    def deal_damage(self):
        damage = math.ceil(self.damage * self.quantity * (1 + (random.randrange(10) - 5) / 100))
        hp_restore_parameter = math.ceil(damage / 10)
        self.quantity += hp_restore_parameter // self.hitpoint
        if self.current_hitpoint + hp_restore_parameter % self.hitpoint >= self.hitpoint:
            self.current_hitpoint = self.hitpoint
        else:
            self.current_hitpoint += hp_restore_parameter % self.hitpoint

        return damage


class Lich(unit):
    def __init__(self):
        super().__init__()
        self.hitpoint = 50
        self.current_hitpoint = 50
        self.speed = 6
        self.damage = 15
        self.quantity = 1
        self.price = 520
        self.player_number = -1
        self.name = "Lich"
        self.type = "Range"

    def deal_damage(self):
        return math.ceil(self.damage * self.quantity * (1 + (random.randrange(100) - 50) / 100))


class Death_knight(unit):
    def __init__(self):
        super().__init__()
        self.hitpoint = 180
        self.current_hitpoint = 180
        self.speed = 15
        self.damage = 40
        self.quantity = 1
        self.price = 1500
        self.player_number = -1
        self.name = "Death_knight"
        self.type = "Melee"

    def deal_damage(self):
        return math.ceil(self.damage * self.quantity * (1 + (random.randrange(100) - 50) / 100))


class Footman(unit):
    def __init__(self):
        super().__init__()
        self.hitpoint = 15
        self.current_hitpoint = 15
        self.speed = 4
        self.damage = 4
        self.quantity = 1
        self.price = 110
        self.player_number = -1
        self.name = "Footman"
        self.type = "Melee"

    def deal_damage(self):
        return math.ceil(self.damage * self.quantity * (1 + (random.randrange(100) - 50) / 100))


class Archer(unit):
    def __init__(self):
        super().__init__()
        self.hitpoint = 18
        self.current_hitpoint = 18
        self.speed = 7
        self.damage = 6
        self.quantity = 1
        self.price = 220
        self.player_number = -1
        self.name = "Archer"
        self.type = "Range"

    def deal_damage(self):
        return math.ceil(self.damage * self.quantity * (1 + (random.randrange(100) - 50) / 100))


class Berserker(unit):
    def __init__(self):
        super().__init__()
        self.hitpoint = 30
        self.current_hitpoint = 30
        self.speed = 9
        self.damage = 12
        self.quantity = 1
        self.price = 350
        self.player_number = -1
        self.name = "Berserker"
        self.type = "Melee"

    def deal_damage(self):
        return math.ceil(self.damage * self.quantity * (1 + (random.randrange(100) - 50) / 100))


class Lands_knecht(unit):
    def __init__(self):
        super().__init__()
        self.hitpoint = 85
        self.current_hitpoint = 85
        self.speed = 6
        self.damage = 15
        self.quantity = 1
        self.price = 490
        self.player_number = -1
        self.name = "Lands_knecht"
        self.type = "Melee"

    def deal_damage(self):
        return math.ceil(self.damage * self.quantity * (1 + (random.randrange(100) - 50) / 100))


class Paladin(unit):
    def __init__(self):
        super().__init__()
        self.hitpoint = 230
        self.current_hitpoint = 230
        self.speed = 10
        self.damage = 45
        self.quantity = 1
        self.price = 2250
        self.player_number = -1
        self.name = "Paladin"
        self.type = "Melee"

    def deal_damage(self):
        return math.ceil(self.damage * self.quantity)


class Army:

    def __init__(self):
        self.stack = []

    def get_by_index(self, index):
        return self.stack[index]

    def get(self):
        return self.stack

    def get_values(self):
        return self.stack

    def print_army(self):
        for unit_name in self.stack:
            print(unit_name.quantity, " ", unit_name.name)

    def add_unit(self, unit_name):
        if len(self.stack) == 5:
            print("Your army contains too much units")
            return False
        else:
            self.stack.append(unit_name)
            return True

    def remove_unit(self, unit_name):
        if unit_name in self.stack:
            self.stack.remove(unit_name)
            return True
        else:
            print("This unit doesn't exist")
            return False

    def unit_quantity(self):
        return len(self.stack)

    def is_empty(self):
        if self.unit_quantity() == 0:
            return True
        else:
            return False

    def castle_stack(self, player_numb):
        unit1 = Footman()
        unit1.quantity = 25
        unit1.player_number = player_numb
        unit2 = Archer()
        unit2.quantity = 20
        unit2.player_number = player_numb

        unit3 = Berserker()
        unit3.quantity = 7
        unit3.player_number = player_numb

        self.stack.append(unit1)
        self.stack.append(unit2)
        self.stack.append(unit3)

    def demon_stack(self, player_numb):
        unit1 = Imp()
        unit1.quantity = 45
        unit1.player_number = player_numb
        unit2 = Demon()
        unit2.quantity = 15
        unit2.player_number = player_numb

        unit3 = Cerberus()
        unit3.quantity = 4
        unit3.player_number = player_numb

        self.stack.append(unit1)
        self.stack.append(unit2)
        self.stack.append(unit3)

    def necro_stack(self, player_numb):
        unit1 = Skeleton_warrior()
        unit1.quantity = 35
        unit1.player_number = player_numb

        unit2 = Ghost()
        unit2.quantity = 16
        unit2.player_number = player_numb

        unit3 = Vampire()
        unit3.quantity = 4
        unit3.player_number = player_numb

        self.stack.append(unit1)
        self.stack.append(unit2)
        self.stack.append(unit3)
