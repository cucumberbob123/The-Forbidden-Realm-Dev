import time


class player:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.hunger = 100

    def decrease_health(self, amount):
        if self.health <= amount:
            print("Oh no {}! You died and lost the game!".format(self.name))
            time.sleep(20)
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
        if self.health < 100:
            self.health += amount
            self.hunger += amount
        else:
            self.hunger += amount
        if self.hunger > 100:
            print("{}, you are to bloated! You lose {} health!".format(
                self.name, amount))
            self.hunger = 100
            self.health -= amount

    def decrease_hunger(self, amount):
        self.hunger -= amount
        if self.hunger < 0:
            self.hunger = 0

    def turnly_decrease(self):
        self.decrease_hunger(3)
        print("{}, your hunger is now {}!".format(self.name, self.hunger))
        if self.hunger < 5:
            self.decrease_health(2)
            print("Oh no {}, you are hungry. Your health is now {}".format(
                self.name, self.health))
