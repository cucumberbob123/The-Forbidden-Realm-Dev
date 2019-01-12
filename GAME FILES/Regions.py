class region():
    def __init__(self, place):
        self.place = place
    def describe(self):
        if self.place == "forest":
            print("THE FOREST:\nFull of trees.\n\nResources:\nWood,\nWild "
                  "Berry,\nStick,\nGrass\n\nAnimals:")
        if self.place == "river":
            print("THE RIVER:\nA steady stream of water.\n\nResources:\n"
                  "Water,\nClay,\nReeds\n\nAnimals:\nSalmon,\nCod")
        if self.place == "mountains":
            print("THE MOUNTAINS:\nA giant hunk of rock.\n\nResources:\n"
                  "Rock,\nFlint,\nSpring Water\n\nAnimals:\nEagle,\nMountain Goat")
        if self.place == "plains":
            print("THE PLAINS:\nA whole load of nothing but grass.\n\nResources:\n"
                  "Twine\n\nAnimals:\nBird,\nSheep")
        self.show_animals()
    def show_animals(self):
        if self.place == "forest":
            animals = (['Deer', 'Bird', 'Fox'])
        if self.place == "river":
            animals = (['Salmon', 'Cod'])
        for animal in animals:
            print(animal)

forest = region("forest")
river = region("river")
mountains = region("mountains")
plains = region("plains")

