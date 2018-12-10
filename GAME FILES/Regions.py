class region():
    def __init__(self, place):
        self.place = place
    def describe(self):
        if self.place == "forest":
            print("THE FOREST:\nFull of trees.\n\nResources:\nWood,\nWild"
                  "Berry,\nStick,\nGrass\n\nAnimals:\nDeer,\nBird,\nFox")
forest = region()
forest.describe("forest")
