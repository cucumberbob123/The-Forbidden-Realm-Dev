import time
class player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.hunger = 100

    def decrease_health(self, amount):
        if self.health <= amount:
            print("Oh no {}! You died and lost the game!".format(self.name)) # finish that
            time.sleep(10)
            exit()
        self.health = self.health - amount
        print("{}, your health is now {}!".format(self.name, self.health))

    def increase_health(self, amount):
        self.health += amount
        print("{}, your health is now {}!".format(self.name, self.health))
        if self.health > 100:
            self.health = 100
            print("{}, you are full health!".format(self.name))

    def increase_hunger(self, amount):
        self.hunger += amount
        if self.hunger > 100:
            print("{}, you are to bloated! You lose {} health!".format(self.name, amount))
            self.hunger = 100
            self.health -= amount
            
    def 
