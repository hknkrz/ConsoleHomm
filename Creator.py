from abc import ABC, abstractmethod
from Units import *
from Units_pool import Units_pool


def return_unit(key):
    CreatorDict = {"Imp": ImpCreator(), "Demon": DemonCreator(), "Cerberus": CerberusCreator(),
                   "Pit_fiend": Pit_fiendCreator(),
                   "Devil": DevilCreator(), "Skeleton_warrior": Skeleton_warriorCreator(),
                   "Ghost": GhostCreator(), "Vampire": VampireCreator(), "Lich": LichCreator(),
                   "Death_knight": Death_knightCreator(), "Footman": FootmanCreator(), "Archer": ArcherCreator(),
                   "Berserker": BerserkerCreator(), "Lands_knecht": Lands_knechtCreator(),
                   "Paladin": PaladinCreator()}
    return CreatorDict[key]


class ObjectCreator(ABC):
    @abstractmethod
    def create(self, player_numb, name, gold_increment, relation, units_pool,
               army):
        pass

    def __init__(self):
        pass


class TownCreator(ObjectCreator):
    def create(self, player_numb, obj_type, gold_increment, relation, units_pool,
               stack):
        return town(player_numb, obj_type, gold_increment, relation, units_pool,
                    stack)


class HeroCreator(ObjectCreator):
    def create(self, player_numb, obj_type, gold_increment, relation, units_pool,
               stack):
        return hero(player_numb, obj_type, gold_increment, relation, units_pool,
                    stack)


class Object:
    def __init__(self, player_numb, name, gold_increment, relation, units_pool,
                 army):
        self.player_number = player_numb
        self.name = name
        self.gold_increment = gold_increment
        self.relation = relation
        self.units_pool = Units_pool[units_pool]
        self.army = army


class town(Object):
    def __init__(self, player_numb, name, gold_increment, relation="Empty", units_pool="empty_pool",
                 army=None):
        super().__init__(player_numb, name, gold_increment, relation, units_pool, army)


class hero(Object):
    def __init__(self, player_numb, name, gold_increment, relation="Empty", units_pool="empty_pool",
                 army=None):
        super().__init__(player_numb, name, gold_increment, relation, units_pool, army)


class object_container:

    def __init__(self):
        self.objects = dict()

    def get_values(self):
        return self.objects.values()

    def get_keys(self):
        return self.objects.keys()

    def get_by_key(self, key):
        return self.objects[key]

    def add_object(self, object_tmp):
        self.objects[object_tmp.name] = object_tmp
        return True

    def remove_object(self, object_tmp):
        if object_tmp.name in self.objects.keys():
            self.objects.pop(object_tmp.name)
            return True
        else:
            print("Object ", object_tmp.name, " doesn't exist")
            return False

    def print_objects(self):
        for element in self.objects:
            print("Object - ", element.name, "under control - ", element.player_number)


class UnitCreator(ABC):

    @abstractmethod
    def create(self):
        pass

    def __init__(self):
        pass


class ImpCreator(UnitCreator):
    def create(self):
        return Imp()


class DemonCreator(UnitCreator):
    def create(self):
        return Demon()


class CerberusCreator(UnitCreator):
    def create(self):
        return Cerberus()


class Pit_fiendCreator(UnitCreator):
    def create(self):
        return Pit_fiend()


class DevilCreator(UnitCreator):
    def create(self):
        return Devil()


class FootmanCreator(UnitCreator):
    def create(self):
        return Footman()


class ArcherCreator(UnitCreator):
    def create(self):
        return Archer()


class BerserkerCreator(UnitCreator):
    def create(self):
        return Berserker()


class Lands_knechtCreator(UnitCreator):
    def create(self):
        return Lands_knecht()


class PaladinCreator(UnitCreator):
    def create(self):
        return Paladin()


class Skeleton_warriorCreator(UnitCreator):
    def create(self):
        return Skeleton_warrior()


class GhostCreator(UnitCreator):
    def create(self):
        return Ghost()


class VampireCreator(UnitCreator):
    def create(self):
        return Vampire()


class Death_knightCreator(UnitCreator):
    def create(self):
        return Death_knight()


class LichCreator(UnitCreator):
    def create(self):
        return Lich()
