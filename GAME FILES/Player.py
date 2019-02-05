import time


class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.hunger = 100

    def decrease_health(self, amount):
        if self.health <= amount:
            print(f"Oh no {self.name}! You died and lost the game!")
            time.sleep(20)
            exit()
        self.health = self.health - amount
        print(f"{self.name}, your health is now {self.health}!")

    def increase_health(self, amount):
        self.health += amount
        print(f"{self.name}, your health is now {self.health}!")
        if self.health > 100:
            self.health = 100
            print(f"{self.name}, you are at full health!")

    def increase_hunger(self, amount):
        if self.health < 100:
            self.health += amount
            self.hunger += amount
        else:
            self.hunger += amount
        if self.hunger > 100:
            print("{self.name}, you are too bloated! You lose {amount} health!")
            self.hunger = 100
            self.health -= amount

    def decrease_hunger(self, amount):
        self.hunger -= amount
        if self.hunger < 0:
            self.hunger = 0

    def turnly_decrease(self):
        self.decrease_hunger(3)
        print(f"{self.name}, your hunger is now {self.hunger}!")
        if self.hunger < 5:
            self.decrease_health(2)
            print(f"Oh no {self.name}, you are hungry. Your health is now {self.health}")
