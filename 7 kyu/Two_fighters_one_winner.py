import math

def declare_winner(fighter1, fighter2, first_attacker):
    f1 = math.ceil(fighter1.health/fighter2.damage_per_attack)
    f2 = math.ceil(fighter2.health/fighter1.damage_per_attack)
    print(f1, f2)
    if f1 == f2 and first_attacker == fighter1.name:
        return fighter1.name
    else:
        if f1 > f2:
            return fighter1.name
        else:
            return fighter2.name