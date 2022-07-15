import random
list_of_num = [1,2,3,4,5,6,7,8,9,10]

class Character:
    def __init__(self, health, power):
        
        self.health = health
        self.power = power
        
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def attack(self,enemy):
        enemy.health -= self.power
        print(f'You did {self.power} damages to the {enemy.name}.')
        if enemy.health <= 0:
            print(f'{enemy.name} is dead.')
        
    def print_status(self, enemy):
        print(f'You have {self.health} health and {self.power} power.')
        print(f'The {enemy.name} has {enemy.health} and {enemy.power}.')

class Hero(Character):
    def __init__(self, health, power):
        self.name = "Hero"
        super(Hero, self).__init__(health, power)
        
    def attack_twice(self, enemy):
        self.enemy = enemy
        possibility = random.choice(list_of_num)  
        if possibility < 3:
            enemy.health -= self.power *2
            print(f'You gave {self.power *2} damage to the {enemy.name}')
            if enemy.health <= 0:
                print(f'The {enemy.name} is dead.')
                
        elif possibility > 2:
            enemy.health -= self.power
            print(f"You gave {self.power} damages to the {enemy.name}.")
            if enemy.health <= 0:
                print(f'The {enemy.name} is dead.')
        
        
        
        
        
class Goblin(Character):
    def __init__(self, health, power):
        self.name = "Goblin"
        super(Goblin, self).__init__(health, power)
        
class Medic(Character):
    def __init__(self, health, power):
        self.name = "Medic"
        super(Medic, self).__init__(health, power)
    def recovery(self):
        possibility = random.choice(list_of_num)
        if possibility <3:
            self.health += 2
            print(f'{self.name} just recovered by 2 health points.')

class Shadow(Character):
    def __init__(self, health, power):
        self.name = "Shadow"
        super(Shadow, self).__init__(health, power)
    def no_damage(self, enemy):
        
        possibility = random.choice(list_of_num)
        if possibility == 1:
            self.health -= enemy.power
            print(f'{enemy.name} gave {enemy.power} damage to {self.name}.')
        else:
            self.health = enemy.power
            print(f'{self.name} did not get health points taken away.')

class Zombie(Character):
    def __init__(self, health, power):
        self.name = "Zombie"
        super(Zombie, self).__init__(health, power)
    def never_die(self, enemy):
        self.health = self.health
        print(f'{self.name} never dies!')          

class Thor(Character):
    def __init__(self, health, power):
        super(Thor, self).__init__(health, power)
        self.name = "Thor" 
    def call_thor(self, friend):
        friend.health += self.health
        print(f'My friend {self.name} just gave me {self.health} health points.')
class Unicorn(Character):
    def __init__(self, health, power):
        super(Unicorn, self).__init__(health, power)
        self.name = "Unicorn"
    def steal_power(self, friend):
        friend.power += self.power
        print(f'My friend {self.name} just gave me {self.power} power points. Oh yea!') 
                   
hero= Hero(100, 20)
goblin= Goblin(150, 10)
medic= Medic(150, 10)
shadow= Shadow(1, 10)
zombie= Zombie(5,5)
thor= Thor(20, 20)
unicorn = Unicorn(10, 10)
def main():

   
    while goblin.alive() and hero.alive():
            print(f'{hero.name}, you have {hero.health} health and {hero.power} power.')
            print(f'{goblin.name}, you have {goblin.health} health and {goblin.power} power.')
            print()
            print("What do you want to do?")
            print("1. fight goblin")
            print("2. do nothing")
            print("3. flee")
            print("4. fight Medic")
            print("5. fight Shadow")
            print("6. fight Zombie")
            print("7. call Thor")
            print("8. call Unicorn")
            print("> ", end=' ')
            raw_input = input()
            if raw_input == "1":
                # Hero attacks goblin
                hero.attack_twice(goblin)
                
            elif raw_input == "2":
                pass
            elif raw_input == "3":
                print("Goodbye.")
                break
            elif raw_input == "4":
                hero.attack_twice(medic)
                medic.recovery()
            elif raw_input == "5":
                shadow.no_damage(hero)
            elif raw_input == "6":
                zombie.never_die(hero)
            elif raw_input == "7":
                thor.call_thor(hero)
            elif raw_input == "8":
                unicorn.steal_power(hero)
                
                
            else:
                print("Invalid input {}".format(raw_input))

            if goblin.health > 0:
                list_of_enemy = [1, 2, 3, 4]
                possibility = random.choice(list_of_enemy)
                
                # Goblin attacks hero
                if possibility == 1:
                    hero.health -= goblin.power
                    print(f"The goblin does {goblin.power} damage to you.")
                    if hero.health <= 0:
                        print("You are dead.")
                # Medic attacks hero
                if possibility == 2:
                    hero.health -= medic.power
                    print(f"The medic does {medic.power} damage to you.")
                    if hero.health <= 0:
                        print("You are dead.")
                 # Shadow attacks hero
                if possibility == 3:
                    hero.health -= shadow.power
                    print(f"The shadow does {shadow.power} damage to you.")
                    if hero.health <= 0:
                        print("You are dead.")
                # Zombie attacks hero
                if possibility == 4:
                    hero.health -= zombie.power
                    print(f"The zombie does {zombie.power} damage to you.")
                    if hero.health <= 0:
                        print("You are dead.")
main()
