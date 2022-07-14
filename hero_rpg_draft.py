# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
        
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
        
    def attack(self,enemy):
        if goblin.name == enemy:
            # Hero attacks goblin
            goblin.health -= hero.power
            print(f"You did {self.power} damages to the {enemy}.")
            if goblin.health <= 0:
                print("The goblin is dead.")
                
        elif hero.name == enemy:
            # Goblin attacks hero
            hero.health -= goblin.power
            print(f"You did {self.power} damages to the {enemy}.")
            if hero.health <= 0:
                print("You are dead.")

    def print_status(self, enemy):
        if goblin.name == enemy:
            print(f'You have {self.health} health and {self.power} power.')
            print(f'The goblin has {enemy.health} and {enemy.power}.')
            
        elif hero.name == enemy:
            print(f'You have {self.health} health and {self.power} power.')      
            print(f'The hero has {enemy.health} and {enemy.power}.')

# class Zombie():
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power
#     def attack(self, enemy):
#         hero.name == enemy
#         hero.health -= zombie.power
#         print(f'{self.name} did {self.power} damages to the {enemy}')
                
# class Hero(Character):
    # def __init__(self):
       
    # def attack(self,enemy):
    #     goblin.name = enemy
    #     # Hero attacks goblin
    #     goblin.health -= hero.power
    #     print(f"You did {self.power} damages to the {enemy}.")
    #     if goblin.health <= 0:
    #         print("The goblin is dead.")
    # def alive(self):
    #     if self.health > 0:
    #         return True
    #     else:
    #         return False
        
    # def print_status(self, enemy):
    #     goblin.name = enemy
    #     print(f'You have {self.health} health and {self.power} power.')
    #     print(f'The goblin has {enemy.health} and {enemy.power}.')
        # print("You have {} health and {} power.".format(hero_health, hero_power))
        # print("The goblin has {} health and {} power.".format(goblin_health, goblin_power))
    
# class Goblin(Character):
    # def __init__(self, name, health, power):
    #     self.name = name
    #     self.health = health
    #     self.power = power
    # def attack(self,enemy):
    #     hero.name = enemy
    #     # Goblin attacks hero
    #     hero.health -= goblin.power
    #     print(f"You did {self.power} damages to the {enemy}.")
    #     if hero.health <= 0:
    #         print("You are dead.")
    # def alive(self):
    #     if self.health > 0:
    #         return True
    #     else:
    #         return False
        
    # def print_status():
    #     print(f'You have {self.health} health and {self.power} power.')      
    #     print(f'The hero has {enemy.health} and {enemy.power}.')
        
hero = Character("goodguy", 20, 5)
goblin = Character("badguy",15, 2)
# zombie=Zombie("Veggie", 5)

# hero.attack(goblin)
# hero.alive()
# goblin.alive()



def main():
#     hero.health = 10
#     hero.power = 5
#     goblin.health = 6
#     goblin.power = 2

   
    while goblin.alive() and hero.alive():
            print(f'{hero.name}, you have {hero.health} health and {hero.power} power.')
            print(f'{goblin.name}, you have {goblin.health} health and {goblin.power} power.')
            print()
            print("What do you want to do?")
            print("1. fight goblin")
            print("2. do nothing")
            print("3. flee")
            print("> ", end=' ')
            raw_input = input()
            if raw_input == "1":
                # Hero attacks goblin
                goblin.health -= hero.power
                print(f"You do {hero.power} damage to the goblin.")
                if goblin.health <= 0:
                    print("The goblin is dead.")
            elif raw_input == "2":
                pass
            elif raw_input == "3":
                print("Goodbye.")
                break
            else:
                print("Invalid input {}".format(raw_input))

            if goblin.health > 0:
                # Goblin attacks hero
                hero.health -= goblin.power
                print(f"The goblin does {goblin.power} damage to you.")
                if hero.health <= 0:
                    print("You are dead.")

main()