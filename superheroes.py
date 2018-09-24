import random

class Ability:
    def __init__(self, name, attack_strength):
        #Initiate starting values
        self.name = name
        self.attack_strength = attack_strength
    def attack(self):
        #Return attack value

        #Calculate lowest attack value as an integer
        lowest_attack_value = self.attack_strength // 2
        #Use random.randint(a, b) to select a random attack value
        random_attack_value = random.randint(lowest_attack_value, self.attack_strength)
        #Return attack value between 0 and the full attack
        return random_attack_value

    def update_attack(self, attack_strength):
        #Update attack value
        self.attack_strength = attack_strength

class Armor:
    def __init__(self, name, defense):
        """Instantiate name and defense strength."""
        self.name = name
        self.defense = defense

    def defend(self):
        """Return a random value between 0 and initialized defend strength."""
        random_defense_value = random.randint(0, self.defense)
        return random_defense_value

class Weapon(Ability):
    def attack(self):
        lowest_attack_value = 0
        random_attack_value = random.randint(lowest_attack_value, self.attack_strength)
        return random_attack_value

class Hero:
    def __init__(self, name, health=100):

        self.abilities = list()
        self.name = name
        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    def defend(self):
        """
        This method should run the defense method on each piece of armor and calculate the total defense

        If the hero's health is 0, the hero is out of play and should return 0 defense points.
        """
        if self.health == 0:
            return 0
        else:
            total_defense = 0
            for armor in self.armors:
                total_defense += armor.defend()
            return total_defense

    def take_damage(self, damage_amt):
        """
        This method should subtract the damage amount from the hero's health.
        If the hero dies, update the number of deaths
        """
        self.health = self.health - damage_amt
        if self.health <= 0:
            self.deaths += 1

    def add_kill(self, num_kills):
        """
        This method should add the number of kills to self.kills
        """

        self.kills += num_kills

    def add_armor(self, armor):
        self.armors.append(armor)

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        # Call the attack method on every ability in our ability list
        # Add up and return the total of all attacks
        total_attack = 0
        if self.abilities is not None:
            for ability in self.abilities:
                total_attack = total_attack + ability.attack()
        return total_attack

class Team:
    def __init__(self, team_name):
        """Instantiate resources."""
        self.name = team_name
        self.heroes = list()
        self.team_kills = 0

    def add_hero(self, Hero):
        """Add Hero object to heroes list."""
        self.heroes.append(Hero)

    def remove_hero(self, name):
        """
        Remove hero from heroes list.
        If Hero isn't found return 0.
        """
        if self.heroes != []:
            for hero in self.heroes:
                if name in hero.name:
                    self.heroes.remove(hero)
                else:
                    return 0
        else:
            return 0

    def find_hero(self, name):
        """
        Find and return hero from heroes list.
        If Hero isn't found return 0.
        """
        if self.heroes != []:
            for hero in self.heroes:
                if name == hero.name:
                    return hero
                else:
                    return 0
        else:
            return 0

    def view_all_heroes(self):
        """Print out all heroes to the console."""
        for hero in self.heroes:
            name = hero.name
            print(name)

    def attack(self, other_team):
        total_attack_strength = 0
        for hero in self.heroes:
            attack_strength = hero.attack()
            total_attack_strength += attack_strength

        other_team.defend(total_attack_strength)

    def update_kills(self):
        for hero in self.heroes:
            # print("ANNNNNWWWAAARRR")
            # hero.kills += 1
            hero.add_kill(1)
            # print("Hero kills" + str(hero.kills))
            # print("WTF")

    def defend(self, damage_amt):
        total_defense_strength = 0
        for hero in self.heroes:
            total_defense = hero.defend()
            total_defense_strength += total_defense

        excess = 0
        print("total_defense_strength=" + str(total_defense_strength))
        print("damage_amt=" + str(damage_amt))
        if total_defense_strength < damage_amt:
            print("something has been killed")
            self.update_kills()
            excess = damage_amt - total_defense_strength

        return self.deal_damage(excess)

    def deal_damage(self, damage):
        damage_per_hero = damage/len(self.heroes)
        total_deaths = 0
        for hero in self.heroes:
            hero.take_damage(damage_per_hero)
        for hero in self.heroes:
            total_deaths += hero.deaths
        return total_deaths

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.health = health

    def stats(self):
        for hero in self.heroes:
            value = hero.kills/hero.deaths
            f'The stats of {hero.name} is {value}'

if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())

# <----------- TEST FOR TEAM CLASS ------------->
    team_one = Team("One")
    jodie = Hero("Jodie Foster")
    aliens = Ability("Alien Friends", 10000)
    jodie.add_ability(aliens)
    team_one.add_hero(jodie)
    team_two = Team("Two")
    athena = Hero("Athena")
    socks = Armor("Socks", 10)
    athena.add_armor(socks)
    team_two.add_hero(athena)
    assert team_one.heroes[0].kills == 0
    team_one.attack(team_two)
    assert team_one.heroes[0].kills == 1
