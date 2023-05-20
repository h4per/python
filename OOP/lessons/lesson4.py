
import random

total_rounds = 0

class GameEntity:
    def __init__(self, name, health, damage):
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
    def health(self, new_health):
        if new_health < 0:
            self.__health = 0
        else:
            self.__health = new_health

    @property
    def damage(self):
        return self.__damage
    
    @damage.setter
    def damage(self, new_damage):
        self.__damage = new_damage

    def __str__(self) -> str:
        return f"Name: {self.name}\nHealth: {self.health}\nDamage: {self.damage}\n"
    

class Boss(GameEntity):
    def __init__(self, name, health, damage):
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


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "Critical Damage ")

    def apply_super_power(self, boss: Boss, heroes: list):
        coef = random.randint(0, 4)
        boss.health -= self.damage * coef
        print(f"Warrior {self.name} hits criticaly: {self.damage * coef}\n")


def print_stat(boss: Boss, heroes):
    print(f"______{total_rounds} Round______\n")
    print(boss)

    for hero in heroes:
        print(hero)


def is_game_finished(boss: Boss, heroes):
    if boss.health == 0:
        print("Heroes WON!")
        return True

    all_heroes_dead = True
    
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
    
    if all_heroes_dead:
        print("Boss WON!")

    return all_heroes_dead


def heroes_power(boss: Boss, heroes: list):
    boss_ability =(["CRITICAL DAMAGE"])
    print(f"Boss {boss.name} blocked {boss_ability}")
    for hero in heroes:
        if boss_ability != hero.super_ability and boss.health > 0 and hero.health > 0:
            hero.apply_super_power(boss, heroes)


def play_round(boss: Boss, heroes: list):
    global total_rounds
    total_rounds += 1

    boss.hit(heroes)

    for hero in heroes:
        hero.hit(boss)
    heroes_power(boss, heroes)



def main():
    boss = Boss("Paimon", 9090, 200)
    warior = Warrior("Kaveh", 5579, 150)
    heroes = [warior]
    

    while not is_game_finished(boss, heroes):
        play_round(boss, heroes)
        print_stat(boss, heroes)
main()