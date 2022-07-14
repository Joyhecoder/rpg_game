# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

import characters






        
hero = characters.Character("Good guy", 20, 5)
goblin = characters.Character("Bad guy",15, 2)




def main():

   
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

