from Start_stacks import Unit_stacks
from Creator import *
import copy


class player:
    def __init__(self, hero_, town_, movepoint, cur_movepoint, fract):
        self.heros = {}
        self.towns = [town_]
        self.movepoints = movepoint
        self.fraction = fract
        self.current_movepoints = cur_movepoint
        self.gold = 0
        self.number = 0

    def reinit(self, hero_name, hero_, town_, movepoint, cur_movepoint, fract, numb):
        self.heros = {hero_name: hero_}
        self.towns = [town_]
        self.movepoints = movepoint
        self.fraction = fract
        self.current_movepoints = cur_movepoint
        self.gold = 2000
        self.number = numb

    def funcs(self, key, arr):
        func_dict = {"move": player.move_to, "attack": player.attack_town,
                     "replace": player.replace_unit,
                     "buy": player.buy_unit, "statistic": player.print_towns, "army": player.print_army}
        if key not in func_dict.keys():
            print("Wrong command")
            return

        return func_dict[key](self, arr)

    def print_towns(self, arr):
        print("Current gold - ", self.gold)
        print("Current heros - ", self.heros.keys())
        print("Current movepoints - ", self.current_movepoints)
        for town_ in range(len(Town_list) - 1):
            print(town_, " ", Town_list[town_].type, " Player - ", Town_list[town_].player_numb,
                  " Hero in town - ",
                  "Empty" if Town_list[town_].relation == {} else Town_list[town_].relation, " gold increment - ",
                  Town_list[town_].gold_increment)

    def attack_town(self, arr):
        if int(arr[1]) >= len(Town_list):
            print("Wrong town number")
            return
        town_ = Town_list[int(arr[1])]
        hero_ = self.heros[arr[0]]

        if town_.player_numb == self.number:
            print("This town is under your control")
            return
        hero_.relation.relation = "Empty"
        hero_.relation = "Empty"
        self.current_movepoints -= 1
        if town_.relation == "Empty":
            if player.attack_object(self, town_, hero_):
                town_.relation = hero_
                hero_.relation = town_
                town_.player_numb = self.number
                return
        else:
            if player.attack_object(self, town_.relation, hero_):
                if player.attack_object(self, town_, hero_):
                    town_.relation = hero_
                    hero_.relation = town_
                    town_.player_numb = self.number
                    return
        return

    def attack_object(self, obj, hero_):
        if len(obj.obj_stack.stack) == 0:
            print("Player ", self.number, " win!")
            return True
        opponents = {obj.player_numb: hero_, hero_.player_numb: obj}
        print("Enter attacked stack")
        while True:
            A = sorted(obj.obj_stack.stack + hero_.obj_stack.stack, key=lambda x: x.speed, reverse=True)
            for units in A:
                print("Player ", units.player_numb, " ", units.name, " turn")
                print("Defender army:")
                for units_ in obj.obj_stack.stack:
                    print(units_.name, " - ", units_.quantity)
                print("Attacker army:")
                for units_ in hero_.obj_stack.stack:
                    print(units_.name, " - ", units_.quantity)
                while True:
                    data = int(input())
                    if data >= len(opponents[units.player_numb].obj_stack.stack):
                        print("Wrong stack number")
                    else:
                        break
                attacked_stack = opponents[units.player_numb].obj_stack.stack[data]
                if attacked_stack.take_damage(units.deal_damage()):
                    opponents[units.player_numb].obj_stack.stack.remove(attacked_stack)
                if len(obj.obj_stack.stack) == 0:
                    print("Player ", self.number, " win!")
                    return True
                if len(hero_.obj_stack.stack) == 0:
                    print("Player ", obj.player_numb, " win!")
                    return False

    def move_to(self, arr):
        hero_ = self.heros[arr[0]]
        town_ = int(arr[1])
        if Town_list[town_].player_numb == self.number:
            self.current_movepoints -= 1
            Town_list[town_].relation = hero
            hero_.relation.relation = "Empty"
            print(hero_, " Moved to ", town_, ". Move points left - ", self.current_movepoints)

            return
        else:
            print("This town isn't under your control")
            return

    def print_army(self, arr):
        for hero_ in self.heros.keys():
            print(hero_, " army:", )
            for units in self.heros[hero_].obj_stack.stack:
                print(units.name, " - ", units.quantity)

    def buy_unit(self, arr):
        town_ = int(arr[2])
        quantity_ = int(arr[0])
        if arr[1] in Units_pool[Town_list[town_].type]:
            unit_ = return_unit(arr[1]).create()
        else:
            print(Town_list[town_].type, " has no unit ", arr[1])
            return

        if unit_.price * quantity_ > self.gold:
            print("Need more gold")
            return
        else:
            tmp_town = CreateTown.create(CreateTownObj, "Neutral", "TmpTown", 400, "Empty", "HeroPool",
                                         Stacks[3 * Number_of_players])

            unit_ = unit(arr[1])
            unit_.quantity = quantity_
            tmp_town.obj_stack.stack.append(unit_)

            Town_list[3 * Number_of_players].obj_stack.stack.append(unit_)
            if player.replace_unit(self, [len(Town_list) - 1, town_, arr[1], quantity_]):
                self.gold -= unit_.price * quantity_
                return
            else:
                print("Buying failed")

    def replace_unit(self, arr):  # replace from obj1 to obj2
        if str(arr[0]).isnumeric() and not str(arr[1]).isnumeric():
            obj2 = self.heros[arr[1]]
            obj1 = Town_list[int(arr[0])]
        elif str(arr[1]).isnumeric() and not str(arr[0]).isnumeric():
            obj2 = Town_list[int(arr[1])]
            obj1 = self.heros[arr[0]]
        elif str(arr[0]).isnumeric() and str(arr[1]).isnumeric():
            obj2 = Town_list[int(arr[1])]
            obj1 = Town_list[int(arr[0])]
        else:
            obj2 = self.heros[arr[1]]
            obj1 = self.heros[arr[0]]
        unit_ = False
        for units in obj1.obj_stack.stack:
            if units.name == arr[2]:
                unit_ = units
                break
        if not unit_:
            print("Wrong unit name")
            return
        quantity_ = int(arr[3])
        if (unit_.quantity < quantity_) or (quantity_ <= 0):
            print("Wrong unit quantity")
            return False
        index = -1
        for units_ind in range(len(obj2.obj_stack.stack)):
            if unit_.name == obj2.obj_stack.stack[units_ind].name:
                index = units_ind
        if len(obj2.obj_stack.stack) == 5:
            if index == -1:
                print("Your army currently have 5 unit stacks, you don't can replace ", quantity_, " ", arr[3])
                return False
        unit_.quantity -= quantity_

        if index == -1:
            obj2.obj_stack.stack.append(copy.deepcopy(unit_))
            obj2.obj_stack.stack[len(obj2.obj_stack.stack) - 1].quantity = quantity_
            obj2.obj_stack.stack[len(obj2.obj_stack.stack) - 1].player_numb = self.number
            print(quantity_, " ", unit_.name, " Replaced from ", obj1, " to ", obj2)
        else:
            obj2.obj_stack.stack[index].quantity += quantity_
            print(quantity_, " ", unit_.name, " Replaced from ", obj1, " to ", obj2)

        if unit_.quantity == 0:
            obj1.obj_stack.stack.remove(unit_)
        return True


CreateTownObj = CreateTown()
CreateHeroObj = CreateHero()
print("Select the number of players")
Number_of_players = int(input())
Stacks = [Unit_stacks() for _ in range(6 * Number_of_players)]
Player_list = [player(None, None, None, None, None) for _ in range(Number_of_players)]
Town_list = [CreateTown.create(CreateTownObj, None, None, 0, "Empty", "HeroPool", Unit_stacks()) for _ in
             range(3 * Number_of_players + 1)]
