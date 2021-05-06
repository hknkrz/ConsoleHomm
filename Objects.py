from Units import Army
import copy
from Units_pool import Units_pool
from Creator import *

CASTLE_GOLD_INCREMENT = 500
NECROPOLIS_GOLD_INCREMENT = 450
DEMONPOLIS_GOLD_INCREMENT = 400
START_PLAYER_GOLD = 2000
MAX_ARMY_SIZE = 5
START_MOVEPOINTS = 2
CORRECT_FRACTIONS = ["Castle", "Necropolis", "Demonpolis"]


class Map:
    def __init__(self, player_numb):
        self.objects = object_container()
        self.players = []
        self.TownCreatorObj = TownCreator()
        self.HeroCreatorObj = HeroCreator()
        for i in range(player_numb):
            print("player ", i + 1, " - choose fraction")
            while True:
                fraction = str(input())
                if fraction not in CORRECT_FRACTIONS:
                    print("Invalid fraction name -", fraction)
                    continue
                else:
                    break

            if fraction == "Castle":
                town_obj = TownCreator.create(self.TownCreatorObj, i, "Castle" + str(i), CASTLE_GOLD_INCREMENT, "Empty",
                                              "Castle",
                                              Army())
                hero_obj = HeroCreator.create(self.HeroCreatorObj, i, "Warrior" + str(i), 0, town_obj, "empty_pool",
                                              Army())
                hero_obj.army.castle_stack(i)
                town_obj.relation = hero_obj
                player_obj = player("Castle", i, object_container(), self)
                player_obj.objects.add_object(hero_obj)
                player_obj.objects.add_object(town_obj)

            elif fraction == "Necropolis":
                town_obj = TownCreator.create(self.TownCreatorObj, i, "Necropolis" + str(i), NECROPOLIS_GOLD_INCREMENT,
                                              "Empty",
                                              "Necropolis",
                                              Army())
                hero_obj = HeroCreator.create(self.HeroCreatorObj, i, "Necromancer" + str(i), 0, town_obj,
                                              "empty_pool",
                                              Army())
                hero_obj.army.necro_stack(i)
                town_obj.relation = hero_obj
                player_obj = player("Necropolis", i, object_container(), self)
                player_obj.objects.add_object(hero_obj)
                player_obj.objects.add_object(town_obj)

            else:
                town_obj = TownCreator.create(self.TownCreatorObj, i, "Demonpolis" + str(i), DEMONPOLIS_GOLD_INCREMENT,
                                              "Empty",
                                              "Demonpolis",
                                              Army())
                hero_obj = HeroCreator.create(self.HeroCreatorObj, i, "Barbarian" + str(i), 0, town_obj,
                                              "empty_pool",
                                              Army())
                hero_obj.army.demon_stack(i)
                town_obj.relation = hero_obj
                player_obj = player("Demonpolis", i, object_container(), self)
                player_obj.objects.add_object(hero_obj)
                player_obj.objects.add_object(town_obj)
            self.objects.add_object(town_obj)
            self.add_player(player_obj)

        for i in range(number_of_players, 3 * number_of_players + 1):
            if i % 3 == 0:
                town_obj = TownCreator.create(self.TownCreatorObj, "Neutal", "Necropolis" + str(i),
                                              NECROPOLIS_GOLD_INCREMENT,
                                              "Empty",
                                              "Necropolis",
                                              Army())
            elif i % 3 == 1:
                town_obj = TownCreator.create(self.TownCreatorObj, "Neutal", "Demonpolis" + str(i),
                                              DEMONPOLIS_GOLD_INCREMENT,
                                              "Empty",
                                              "Demonpolis",
                                              Army())
            else:
                town_obj = TownCreator.create(self.TownCreatorObj, "Neutal", "Castle" + str(i),
                                              CASTLE_GOLD_INCREMENT,
                                              "Empty",
                                              "Castle",
                                              Army())
            self.objects.add_object(town_obj)

    def add_player(self, object_tmp):
        self.players.append(object_tmp)
        return True

    def print_map(self):
        for object_tmp in self.objects.get_values():
            print(object_tmp.name, " player - ", object_tmp.player_number, " gold increment - ",
                  object_tmp.gold_increment,
                  " hero - ", object_tmp.relation if object_tmp.relation == "Empty" else object_tmp.relation.name)


class player:

    def __init__(self, fraction, player_number, object_cont, map_tmp):

        self.movepoints = START_MOVEPOINTS
        self.current_movepoints = START_MOVEPOINTS
        self.gold = START_PLAYER_GOLD
        self.fraction = fraction
        self.player_number = player_number
        self.objects = object_cont
        self.TownCreatorObj = TownCreator()
        self.current_map = map_tmp
        # методы вызываются по ключу, каждому ключу соответствует кортеж из метода и кол-ва аргументов
        self.func_dict = {"move": (self.move_to, 2), "attack": (self.attack_town, 2),
                          "replace": (self.replace_unit, 4),
                          "buy": (self.buy_unit, 3), "info": (self.print_info, 0), "army": (self.print_army, 1),
                          "map": (self.current_map.print_map, 0)}

    def funcs(self, *args):
        if len(args) == 0:
            print("Empty input line")
            return False
        if args[0] not in self.func_dict.keys():
            print("This command doesn't exist - ", args[0])
            return False
        if len(args) - 1 != self.func_dict[args[0]][1]:
            print("Wrong argument quantity for command ", args[0])
            return False
        new_args = []
        if len(args) > 1:
            new_args += args[1:]
        return self.func_dict[args[0]][0](*new_args)

    def print_info(self):
        print("Current gold - ", self.gold)
        print("Current movepoints - ", self.current_movepoints)
        for object_tmp in self.objects.get_values():
            if isinstance(object_tmp, town):
                print(object_tmp.name, " gold increment - ", object_tmp.gold_increment, " hero - ", object_tmp.relation)

    def correct_name(self, hero_name, town_name):
        if town_name not in current_map.objects.get_keys():
            print("Town ", town_name, " doesn't exist")
            return False

        if hero_name not in self.objects.get_keys():
            print("Hero ", hero_name, " doesn't exist")
            return False
        hero_obj = self.objects.get_by_key(hero_name)
        if not isinstance(hero_obj, hero):
            print(hero_name, " is a name of town")
            return False
        return True

    def attack_town(self, hero_name, town_name):
        if not self.correct_name(hero_name, town_name):
            return False
        town_obj = current_map.objects.get_by_key(town_name)
        if town_obj.player_number == self.player_number:
            print("This town is under your control")
            return False

        hero_obj = self.objects.get_by_key(hero_name)
        hero_obj.relation.relation = "Empty"
        hero_obj.relation = "Empty"
        self.current_movepoints -= 1
        if town_obj.relation == "Empty":
            if self.attack_object(town_obj, hero_obj):
                town_obj.relation = hero_obj
                hero_obj.relation = town_obj
                town_obj.player_number = self.player_number
                return
        else:
            if self.attack_object(town_obj.relation, hero_obj):
                if self.attack_object(town_obj, town_obj):
                    town_obj.relation = hero_obj
                    hero_obj.relation = town_obj
                    town_obj.player_number = self.player_number
                    return
        return

    def attack_object(self, town_obj, hero_obj):
        if town_obj.army.is_empty():
            print("Player ", self.player_number, " win!")
            return True
        opponents = {town_obj.player_number: hero_obj, hero_obj.player_number: town_obj}
        print("Enter attacked unit")
        while True:
            Unit_queue = sorted(town_obj.army.get() + hero_obj.army.get(), key=lambda x: x.speed, reverse=True)
            for units in Unit_queue:
                print("Player ", units.player_number, " ", units.name, " turn")
                print("Defender army:")
                town_obj.army.print_army()
                print("Attacker army:")
                hero_obj.army.print_army()
                while True:
                    input_val = input()
                    data = 0
                    try:
                        data = int(input_val)
                    except Exception:
                        print("Incorrect value for number of unit")
                        continue
                    if data >= opponents[units.player_number].army.unit_quantity():
                        print("Wrong unit number")
                    else:
                        break
                attacked_stack = opponents[units.player_number].army.get_by_index(data)
                if attacked_stack.take_damage(units.deal_damage()):
                    opponents[units.player_number].army.remove_unit(attacked_stack)
                if town_obj.army.is_empty():
                    print("Player ", self.player_number, " win!")
                    return True
                if hero_obj.army.is_empty():
                    print("Player ", town_obj.player_number, " win!")
                    return False

    def move_to(self, hero_name, town_name):

        if not self.correct_name(hero_name, town_name):
            return False

        town_obj = current_map.objects.get_by_key(town_name)
        hero_obj = self.objects.get_by_key(hero_name)
        if town_obj.player_number == self.player_number:
            self.current_movepoints -= 1
            town_obj.relation = hero_obj
            hero_obj.relation.relation = "Empty"
            print(hero_name, "Moved to", town_name, ". Move points left -", self.current_movepoints)

            return True
        else:
            print("This town isn't under your control")
            return False

    def print_army(self, obj_name):
        if obj_name not in self.objects.get_keys():
            print("Obj ", obj_name, " doesn't exist")
            return False
        obj = self.objects.get_by_key(obj_name)
        print(obj_name, " army:")
        obj.army.print_army()
        return True

    def buy_unit(self, quantity, unit_name, town_name):
        quantity = int(quantity)
        if town_name not in self.objects.get_keys():
            print("Town ", town_name, " doesn't exist")
            return False
        town_obj = self.objects.get_by_key(town_name)
        if not isinstance(town_obj, town):
            print(town_name, " is a name of hero")
            return False
        if unit_name in town_obj.units_pool:
            tmp_unit = return_unit(unit_name).create()
        else:
            print(town_name, " pool has no unit ", unit_name)
            return False

        if tmp_unit.price * quantity > self.gold:
            print("Need more gold")
            return False
        tmp_town = TownCreator.create(self.TownCreatorObj, -1, "Noname", 0,
                                      "Empty",
                                      "empty_pool",
                                      Army())
        tmp_unit.quantity = quantity
        tmp_town.army.add_unit(tmp_unit)
        if self.replace_unit(tmp_town, town_name, unit_name, quantity):
            self.gold -= tmp_unit.price * quantity
            return True
        else:
            print("Buying failed")
            return False

    def replace_unit(self, object1_name, object2_name, unit_name, quantity):  # replace from obj1 to obj2
        quantity = int(quantity)
        if object2_name not in self.objects.get_keys():
            print("Object ", object2_name, " doesn't exist")
            return False
        object2 = self.objects.get_by_key(object2_name)
        # Проверка, вызвана ли функция из ф-ции покупки
        if not isinstance(object1_name, town):
            if object1_name not in self.objects.get_keys():
                print("Object ", object1_name, " doesn't exist")
                return False
            object1 = self.objects.get_by_key(object1_name)
        else:
            object1 = object1_name

        tmp_unit = False
        for units in object1.army.get():
            if units.name == unit_name:
                tmp_unit = units
                break
        if not tmp_unit:
            print("Wrong unit name")
            return False
        if (tmp_unit.quantity < quantity) or (quantity <= 0):
            print("Wrong unit quantity")
            return False
        for units in object2.army.get():
            if units.name == tmp_unit.name:
                units.quantity += quantity
                tmp_unit.quantity -= quantity
                if tmp_unit.quantity == 0:
                    object1.army.remove_unit(tmp_unit)
                return True
        copy_unit = copy.deepcopy(tmp_unit)
        copy_unit.quantity = quantity
        if object2.army.add_unit(copy_unit):
            tmp_unit.quantity -= quantity
            if tmp_unit.quantity == 0:
                object1.army.remove_unit(tmp_unit)
            return True
        return False


print("Select the number of players")
number_of_players = int(input())
current_map = Map(number_of_players)
while (True):
    for current_player in current_map.players:
        while current_player.current_movepoints > 0:
            command = list(input().split())
            player.funcs(current_player, *command)
        current_player.current_movepoints = current_player.movepoints
        for objects in current_player.objects.get_values():
            current_player.gold += objects.gold_increment
        print("Player ", current_player.player_number, " -your turn is over")
    break
