class region():
    def __init__(self, place):
        self.place = place

    def describe(self):
        if self.place == "forest":
            print("THE FOREST:\nFull of trees.\n\nResources:")
        if self.place == "river":
            print("THE RIVER:\nA steady stream of water.\n\nResources:")
        if self.place == "mountains":
            print("THE MOUNTAINS:\nA giant hunk of rock.\n\nResources:")
        if self.place == "plains":
            print("THE PLAINS:\nA whole load of nothing but grass.\n\nResources:")
        self.show_resources()
        print("\nAnimals:")
        self.show_animals()
        

    def show_animals(self):
        if self.place == "forest":
            animals = (['Deer', 'Bird', 'Fox'])
        if self.place == "river":
            animals = (['Salmon', 'Cod'])
        if self.place == "mountain":
            animals = (['Mountain Goat', 'Bird'])
        if self.place == "plains":
            animals = (['Bird', 'Sheep'])
        for animal in animals:
            print(animal)

    def show_resources(self):
        if self.place == "forest":
            resources = (['Wood', 'Wild Berry', 'Stick'])
        if self.place == "river":
            resources = (['Water', 'Clay', 'Reeds'])
        if self.place == "mountains":
            resources = (['Rock', 'Flint', 'Spring Water'])
        if self.place == "plains":
            resources = (['Twine', 'Corn', 'Dried Leaves'])
        for resource in resources:
            print(resource)

class forest2(region):
    def __init__(self, place):
        region.__init__(self, place)
        self.resources = (['Wood', 'Wild Berry', 'Stick'])
    
    def show_resources(self):
        print("Boo!")
        for resource in self.resources:
            print(resource)

            
forest = region("forest")
river = region("river")
mountains = region("mountains")
plains = region("plains")
# forest.describe()

forest_new = forest2("forest")
forest_new.describe()
plains.describe()
