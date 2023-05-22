import random

total_rounds = 0

class GameEntity:
    def __init__(self, name, health, damage) -> None:
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name
    
    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value
    
    def __str__(self) -> str:
       return f"{self.name}\nHealth: {self.health}\nDamage: {self.damage}\n"
    


class Boss(GameEntity):
    def __init__(self, name, health, damage) -> None:
        super().__init__(name, health, damage)
    
    def hit(self, heroes: list):
        for hero in heroes:
            if hero.health > 0 and self.health > 0:
                hero.health -= self.damage

    def __str__(self) -> str:
        return "BOSS " + super().__str__()


class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability) -> None:
        super().__init__(name, health, damage)
        self.__super_ability = super_ability

    @property
    def super_ability(self):
        return self.__super_ability

    @super_ability.setter
    def super_ability(self, value):
        self.__super_ability = value
    
    def hit(self, boss: Boss):
        if boss.health > 0 and self.health > 0:
            boss.health -= self.damage

    def apply_super_power(self, boss: Boss, heroes: list):
        pass 

class Berserk(Hero):
    def __init__(self, name, health, damage) -> None:
        super().__init__(name, health, damage, "PART DAMAGE")
    
    def apply_super_power(self, boss: Boss, heroes: list):
        coef = random.randint(0, 100)
        boss.health -= boss.damage - coef
        print(f"Berserk {self.name} hits part damage : {boss.damage - coef}\n")


class Warior(Hero):
    def __init__(self, name, health, damage) -> None:
        super().__init__(name, health, damage, "CRITICAL DAMAGE")

    def apply_super_power(self, boss: Boss, heroes: list):
        coef = random.randint(0, 5)
        boss.health -= self.damage * coef
        print(f"Warrior {self.name} hits criticaly: {self.damage * coef}")


class Medic(Hero):
    def __init__(self, name, health, damage, heal_point) -> None:
        super().__init__(name, health, damage, "HEAL")
        self.__heal_point = heal_point

    def apply_super_power(self, boss: Boss, heroes: list):
        print(f"Medic: {self.name} heal {self.__heal_point}")
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.health += self.__heal_point


class Mag(Hero):
    def __init__(self, name, health, damage) -> None:
        super().__init__(name, health, damage, "BOOST")

    def apply_super_power(self, boss: Boss, heroes: list):
        boost_point = random.choice([5, 10, 15])
        print(f"Mag: {self.name} boost {boost_point}")
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.damage += boost_point



def is_game_finished(boss: Boss, heroes):
    if boss.health <= 0:
        print("Heroes WON!")
        return True

    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
    
    if all_heroes_dead:
        print("Boss WON!")

    return all_heroes_dead
    

def print_statistic(boss: Boss, heroes):
    print(f"___________{total_rounds} Round___________\n")
    print(boss)
    for hero in heroes:
        print(hero)


def heroes_power(boss: Boss, heroes: list):
    boss_ability = random.choice(["CRITICAL DAMAGE", "HEAL", "BOOST","PART DAMAGE","Size Manipulation","Relive"])
    print(f"Boss {boss.name} blocked {boss_ability}")
    for hero in heroes:
        if boss_ability != hero.super_ability and boss.health > 0 and hero.health > 0:
            hero.apply_super_power(boss, heroes)



def play_round(boss: Boss, heroes: list):
    print_statistic(boss, heroes)
    global total_rounds
    total_rounds += 1

    boss.hit(heroes)

    for hero in heroes:
        hero.hit(boss)
    heroes_power(boss, heroes)



def main():
    boss = Boss("Nurbolot", 15000, 500)

    warrior = Warior("Ashat", 2600, 100)
    warrior_2 = Warior("Kurmanbek", 2900, 200)
    medic = Medic("Islam", 2202, 5, 150)
    medic_assistent = Medic("Janysh", 2400, 10, 50)
    magic = Mag("Magomed", 2900, 200)
    berserk = Berserk("Kaveh", 2300, 250)

    heroes = [warrior, medic, medic_assistent, magic, warrior_2, berserk]

    while not is_game_finished(boss, heroes):
        play_round(boss, heroes)
main()


# class Witcher(Hero):
#     def __init__(self, name, health, damage) -> None:
#         super().__init__(name, health, damage,"Relive")

#     def apply_super_power(self, boss: Boss, heroes: list):
#         relive_coef = random.choice(heroes)
#         print(f"Witcher {self.name}, relived {relive_coef}")
#         for hero in heroes:
#             if self.health <= 0 and hero != self:
#                 self.health *= hero.health

#     def __str__(self) -> str:
#         return super().__str__()
