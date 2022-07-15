
import random

list_of_num = [1,2,3,4,5,6,7,8,9,10]

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
        print(f'You have {self.health} health and {self.power} power.')
        print(f'The {enemy.name} has {enemy.health} and {enemy.power}.')
        
        # if enemy.name == enemy:
        #     print(f'You have {self.health} health and {self.power} power.')
        #     print(f'The goblin has {enemy.health} and {enemy.power}.')
            
        # elif .name == enemy:
        #     print(f'You have {self.health} health and {self.power} power.')      
        #     print(f'The hero has {enemy.health} and {enemy.power}.')
            
class Hero(Character):
    def __init__(self, name, health, power):
        super(Hero,self).__init__(name, health, power)
        
        
    def attack1(self, enemy):
        self.enemy = enemy
        possibility = random.choice(list_of_num)
        print(possibility)
        if possibility < 3:
            # hero.power = hero.power * 2
            # print(hero.power)
             # Hero attacks goblin
            enemy.health -= self.power *2
            print(f"You did {self.power} damages to the {enemy.name}.")
            if enemy.health <= 0:
                print("The goblin is dead.") #change goblin into self.name after making class goblin
            
        elif possibility > 2:
             # Hero attacks goblin
            enemy.health -= self.power
            print(f"You did {self.power} damages to the {enemy.name}.")
            if enemy.health <= 0:
                print("The goblin is dead.")

class Goblin(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power
        
        
class Medic(Character):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power =power
    def attack(self, enemy):
        self.enemy = enemy
        possibility = random.choice(list_of_num)
        print(possibility)
        if possibility < 3:
            enemy.health -= self.power
            self.health += 2
            print(f"You did {self.power} damages to the {enemy.name}, and you now have {self.health} health.")
            if enemy.health <= 0:
                    print(f"The {enemy.name} is dead.")
            
        elif possibility > 2:
             # Hero attacks goblin
            enemy.health -= self.power
            print(f"You did {self.power} damages to the {enemy.name}. You did not recuperate any health points.")
            if enemy.health <= 0:
                print(f"The {enemy.name} is dead.")

class Shadow(Character):
    def __init__(self, health, power):   #how to default health = 1
        self. health = health
        self.power = power
        
        
    def attack(self, enemy):
        self.enemy = enemy
        possibility = random.choice(list_of_num)
        print(possibility)
        if possibility == 1:
            enemy.health -= self.power
            self.health -= enemy.power
            print(f"You did {self.power} damages to the {enemy.name}, but you got attacked. You now have {self.health} health.")
            if enemy.health <= 0:
                    print(f"The {enemy.name} is dead.")
        else:
            enemy.health -= self.power
            print(f"You did {self.power} damages to the {enemy.name}, and you now have {self.health} health.")
            if enemy.health <= 0:
                    print(f"The {enemy.name} is dead.")
        

class Zombie(Character):
    def __init__(self, name, health, power):
        super(Zombie, self).__init__(name, health, power)
    def attack(self, enemy):
        self.enemy = enemy
        #zombie attack any heros
        enemy.health -= self.power
        self.health -= enemy.power
        print(f'You did {self.power} damages to the {enemy.name}, but you never die!')        

class Barbie:
    pass

class Unicorn:
    pass

# # hero = Character("Good guy", 20, 5)
# # goblin = Character("Bad guy",15, 2)
# # hero= Hero(20, 2)
# # hero.attack(goblin)

# medic = Medic("medic guy", 20, 5)
# # medic.attack(goblin)

# # shadow=Shadow(1,2)
# # shadow.attack(goblin)

# zombie=Zombie("Zombie", 5,5)
# zombie.attack(medic)