from abc import ABC, abstractmethod
from Units import *


def return_unit(key):
    CreatorDict = {"Imp": CreateImp(), "Demon": CreateDemon(), "Cerberus": CreateCerberus(),
                   "Pit_fiend": CreatePit_fiend(),
                   "Devil": CreateDevil(), "Skeleton_warrior": CreateSkeleton_warrior(),
                   "Ghost": CreateGhost(), "Vampire": CreateVampire(), "Lich": CreateLich(),
                   "Death_knight": CreateDeath_knight(), "Footman": CreateFootman(), "Archer": CreateArcher(),
                   "Berserker": CreateBerserker(), "Lands_knecht": CreateLands_knecht(),
                   "Paladin": CreatePaladin()}
    return CreatorDict[key]


class CreateObject(ABC):
    @abstractmethod
    def create(self, player_numb_, type_, gold_increment_, relation_, units_pool_,
               stack_):
        pass

    def __init__(self):
        pass


class CreateTown(CreateObject):
    def create(self, player_numb_, type_, gold_increment_, relation_, units_pool_,
               stack_):
        return town(player_numb_, type_, gold_increment_, relation_, units_pool_,
                    stack_)


class CreateHero(CreateObject):
    def create(self, player_numb_, type_, gold_increment_, relation_, units_pool_,
               stack_):
        return hero(player_numb_, type_, gold_increment_, relation_, units_pool_,
                    stack_)


class CreateUnit(ABC):

    @abstractmethod
    def create(self):
        pass

    def __init__(self):
        pass


class CreateImp(CreateUnit):
    def create(self):
        return unit("Imp")


class CreateDemon(CreateUnit):
    def create(self):
        return unit("Demon")


class CreateCerberus(CreateUnit):
    def create(self):
        return unit("Cerberus")


class CreatePit_fiend(CreateUnit):
    def create(self):
        return unit("Pit_fiend")


class CreateDevil(CreateUnit):
    def create(self):
        return unit("Devil")


class CreateFootman(CreateUnit):
    def create(self):
        return unit("Footman")


class CreateArcher(CreateUnit):
    def create(self):
        return unit("Archer")


class CreateBerserker(CreateUnit):
    def create(self):
        return unit("Berserker")


class CreateLands_knecht(CreateUnit):
    def create(self):
        return unit("Lands_knecht")


class Create(CreateUnit):
    def create(self):
        return unit("Imp")


class CreatePaladin(CreateUnit):
    def create(self):
        return unit("Paladin")


class CreateSkeleton_warrior(CreateUnit):
    def create(self):
        return unit("Skeleton_warrior")


class CreateGhost(CreateUnit):
    def create(self):
        return unit("Ghost")


class CreateVampire(CreateUnit):
    def create(self):
        return unit("Vampire")


class CreateDeath_knight(CreateUnit):
    def create(self):
        return unit("Death_knight")


class CreateLich(CreateUnit):
    def create(self):
        return unit("Lich")
