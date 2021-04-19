from Objects import CreateTownObj, CreateHero, CreateTown, CreateHeroObj, player, Stacks, Player_list, \
    Town_list, Number_of_players
for i in range(Number_of_players, 3 * Number_of_players):
    Town_list[i].obj_stack = Stacks[i]
for i in range(Number_of_players):
    print("player ", i + 1, " - choose fraction")
    fraction = str(input())
    if fraction == "Castle":
        Town_list[i] = CreateTown.create(CreateHeroObj, i, "Castle", 500, "Empty", "Castle", Stacks[2 * i + 1])
        Warrior = CreateHero.create(CreateHeroObj, i, "Warrior", 0, Town_list[i], "HeroPool", Stacks[2 * i])
        Warrior.obj_stack.castle_stack(i)
        Town_list[i].relation = Warrior
        Player_list[i].reinit("Warrior", Warrior, Town_list[i], 2, 2, "Castle", i)

    elif fraction == "Necropolis":
        Town_list[i] = CreateTown.create(CreateTownObj, i, "Necropolis", 450, "Empty", "Necropolis", Stacks[2 * i + 1])
        Necromancer = CreateHero.create(CreateHeroObj, i, "Necromancer", 0, Town_list[i], "HeroPool", Stacks[2 * i])
        Necromancer.obj_stack.necro_stack(i)
        Town_list[i].relation = Necromancer
        Player_list[i].reinit("Necromancer", Necromancer, Town_list[i], 2, 2, "Necropolis", i)

    elif fraction == "Demonpolis":
        Town_list[i] = CreateTown.create(CreateTownObj, i, "Demonpolis", 400, "Empty", "Demonpolis", Stacks[2 * i + 1])
        Warlock = CreateHero.create(CreateHeroObj, i, "Warlock", 0, Town_list[i], "HeroPool", Stacks[2 * i])
        Warlock.obj_stack.demon_stack(i)
        Town_list[i].relation = Warlock
        Player_list[i].reinit("Warlock", Warlock, Town_list[i], 3, 3, "Demonpolis", i)

    else:
        i -= 1
        print("Wrong fraction name, repeat please")
for q in range(Number_of_players, 3 * Number_of_players + 1):
    if q % 3 == 0:
        Town_list[q] = CreateTown.create(CreateTownObj, "Neutral", "Demonpolis", 400, "Empty", "Demonpolis",
                                         Stacks[q + Number_of_players])
    elif q % 3 == 1:
        Town_list[q] = CreateTown.create(CreateTownObj, "Neutral", "Necropolis", 450, "Empty", "Necropolis",
                                         Stacks[q + Number_of_players])
    else:
        Town_list[q] = CreateTown.create(CreateTownObj, "Neutral", "Castle", 500, "Empty", "Castle",
                                         Stacks[q + Number_of_players])
for player_numb in range(Number_of_players):
    current_player = Player_list[player_numb // Number_of_players]
    while current_player.current_movepoints > 0:
        command = list(input().split())
        player.funcs(current_player, command[0], command[1:])
    current_player.current_movepoints = current_player.movepoints
    for town in current_player.towns:
        current_player.gold += town.gold_increment
    print("Player ", player_numb // Number_of_players, " -your turn is over")
