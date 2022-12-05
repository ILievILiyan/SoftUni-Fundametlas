def castspell(heroes_dictionary, hero_name_, mp_, mp_needed_, spell_name_):
    if mp_ >= mp_needed_:
        mp_ -= mp_needed_
        print(f'{hero_name_} has successfully cast {spell_name_} and now has {mp_} MP!')
    else:
        print(f'{hero_name_} does not have enough MP to cast {spell_name_}!')
    heroes[hero_name_]['mp'] = mp_
    return heroes_dictionary


def takedamage(heroes_dictionary, hero_name_, hp_, damage_, attacker_):
    if hp_ > damage_:
        hp_ -= damage_
        print(f'{hero_name_} was hit for {damage_} HP by {attacker_} and now has {hp_} HP left!')
        heroes[hero_name_]['hp'] = hp_
    else:
        print(f'{hero_name_} has been killed by {attacker_}!')
        del heroes[hero_name_]
    return heroes_dictionary


def recharge(heroes_dictionary, hero_name_, mp_, amount_recovered_):
    if mp_ + amount_recovered_ > 200:
        result_recovered = 200 - mp_
        mp_ = 200
    else:
        mp_ += amount_recovered
        result_recovered = amount_recovered_
    heroes_dictionary[hero_name_]['mp'] = mp_
    print(f'{hero_name_} recharged for {result_recovered} MP!')

    return heroes_dictionary


def healed(heroes_dictionary, hero_name_, hp_, amount_recovered_):
    if hp_ + amount_recovered_ > 100:
        result_recovered = 100 - hp_
        hp_ = 100
    else:
        hp_ += amount_recovered_
        result_recovered = amount_recovered_
    heroes_dictionary[hero_name_]['hp'] = hp_
    print(f'{hero_name_} healed for {result_recovered} HP!')
    return heroes_dictionary


num_of_heroes = int(input())
heroes = {}

for _ in range(num_of_heroes):
    hero = input().split()
    hero_name, hp,  mp = hero[0], int(hero[1]), int(hero[2])
    if hero_name not in heroes.keys():
        heroes[hero_name] = {}
    heroes[hero_name]['hp'] = hp
    heroes[hero_name]['mp'] = mp

while True:
    command = input()
    if command == "End":
        if len(heroes) > 0:
            for name, hp_mp in heroes.items():
                print(name)
                print(f'HP: {hp_mp["hp"]}')
                print(f'MP: {hp_mp["mp"]}')
        break

    cmd = command.split(" - ")
    hero = cmd[1]
    hp = heroes[hero]['hp']
    mp = heroes[hero]['mp']

    if cmd[0] == "CastSpell":
        mp_needed, spell_name = int(cmd[2]), cmd[3]
        castspell(heroes, hero, mp, mp_needed, spell_name)

    elif cmd[0] == "TakeDamage":
        damage, attacker = int(cmd[2]), cmd[3]
        takedamage(heroes, hero, hp, damage, attacker)

    elif cmd[0] == "Recharge":
        amount_recovered = int(cmd[2])
        recharge(heroes, hero, mp, amount_recovered)

    elif cmd[0] == "Heal":
        amount_recovered = int(cmd[2])
        healed(heroes, hero, hp, amount_recovered)
