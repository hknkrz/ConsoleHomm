import math
from Unit_stats import *
import random
from Units_pool import *


class Object:
    def __init__(self, player_numb_, type_, gold_increment_=0, relation_="Empty", units_pool_="HeroPool",
                 stack_=None):
        self.type = type_
        self.gold_increment = gold_increment_
        self.player_numb = player_numb_
        self.units_pool = Units_pool[units_pool_]
        self.obj_stack = stack_
        self.relation = relation_


class town(Object):
    def __init__(self, player_numb_, type_, gold_increment_=0, relation_="Empty", units_pool_="HeroPool",
                 stack_=None):
        super().__init__(player_numb_, type_, gold_increment_, relation_, units_pool_, stack_)


class hero(Object):
    def __init__(self, player_numb_, type_, gold_increment_=0, relation_="Empty", units_pool_="HeroPool",
                 stack_=None):
        super().__init__(player_numb_, type_, gold_increment_, relation_, units_pool_, stack_)


class unit:
    def __init__(self, key):
        arr = Unit_stats[key]
        self.hitpoint = arr[0]
        self.current_hitpoint = arr[0]
        self.speed = arr[1]
        self.damage = arr[2]
        self.quantity = 1
        self.price = arr[3]
        self.player_numb = -1
        self.name = arr[4]
        self.type = arr[5]

    def deal_damage(self):
        pass

    def take_damage(self, damage: int):
        if self.hitpoint * (self.quantity - 1) + self.current_hitpoint <= damage:
            print(self.name, "perish")
            return True
        else:
            cur_hp = self.hitpoint * (self.quantity - 1) + self.current_hitpoint \
                     - damage
            self.current_hitpoint -= damage % self.hitpoint
            self.quantity -= damage // self.hitpoint
            print(self.name, " takes ", damage, " damage")
            return False


class Imp(unit):
    def __init__(self):
        super().__init__("Imp")

    def deal_damage(self):
        return math.ceil(self.damage * self.quantity * (1 + (random.randrange(100) - 50) / 100))


class Demon(unit):
    def __init__(self):
        super().__init__("Demon")

    def deal_damage(self):
        return math.ceil(self.damage * self.quantity * (1 + (random.randrange(40) - 20) / 100))


class Cerberus(unit):
    def __init__(self):
        super().__init__("Cerberus")

    def deal_damage(self):
        return math.ceil(self.damage * self.quantity * (1 + (random.randrange(30) - 15) / 100))


class Pit_fiend(unit):
    def __init__(self):
        super().__init__("Pit_fiend")

    def deal_damage(self):
        return math.ceil(self.damage * self.quantity * (1 + (random.randrange(50) - 25) / 100))


class Devil(unit):
    def __init__(self):
        super().__init__("Devil")

    def deal_damage(self):
        return math.ceil(self.damage * self.quantity * (1 + (random.randrange(10) - 5) / 100))


class Skeleton_warrior(unit):
    def __init__(self):
        super().__init__("Skeleton_warrior")

    def deal_damage(self):
        return math.ceil(self.damage * self.quantity * (1 + (random.randrange(80) - 40) / 100))


class Ghost(unit):
    def __init__(self):
        super().__init__("Ghost")

    def deal_damage(self):
        return math.ceil(self.damage * self.quantity * (1 + (random.randrange(20) - 10) / 100))

    def take_damage(self, damage: int):
        if random.randrange(100) < 20:
            print("Ghosts evade hit!")
        else:
            super().take_damage(damage)


class Vampire(unit):
    def __init__(self):
        super().__init__("Vampire")

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
        super().__init__("Lich")

    def deal_damage(self):
        return math.ceil(self.damage * self.quantity * (1 + (random.randrange(100) - 50) / 100))


class Death_knight(unit):
    def __init__(self):
        super().__init__("Death_knight")

    def deal_damage(self):
        return math.ceil(self.damage * self.quantity * (1 + (random.randrange(100) - 50) / 100))


class Footman(unit):
    def __init__(self):
        super().__init__("Footman")

    def deal_damage(self):
        return math.ceil(self.damage * self.quantity * (1 + (random.randrange(100) - 50) / 100))


class Archer(unit):
    def __init__(self):
        super().__init__("Archer")

    def deal_damage(self):
        return math.ceil(self.damage * self.quantity * (1 + (random.randrange(100) - 50) / 100))


class Berserker(unit):
    def __init__(self):
        super().__init__("Berserker")

    def deal_damage(self):
        return math.ceil(self.damage * self.quantity * (1 + (random.randrange(100) - 50) / 100))


class Lands_knecht(unit):
    def __init__(self):
        super().__init__("Lands_knecht")

    def deal_damage(self):
        return math.ceil(self.damage * self.quantity * (1 + (random.randrange(100) - 50) / 100))


class Paladin(unit):
    def __init__(self):
        super().__init__("Paladin")

    def deal_damage(self):
        return math.ceil(self.damage * self.quantity)
