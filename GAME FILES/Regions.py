class region():
    def __init__(self, place):
        self.place = place

class forest(region):
    def __init__(self, place):
        region.__init__(self, place)
        self.resources = (['Wood', 'Wild Berry', 'Stick'])
        self.animals = (['Deer', 'Bird', 'Fox'])

    def show_resources(self):
        for resource in self.resources:
            print(resource)
            
    def show_animals(self):
        for animal in self.animals:
            print(animal)

    def description(self):
        print("THE FOREST:\nFull of trees.\n\nResources:")
        self.show_resources()
        print("Animals:")
        self.show_animals()

class river(region):
    def __init__(self, place):
        region.__init__(self, place)
        self.resources = (['Water', 'Clay', 'Reeds'])
        self.animals = (['Salmon', 'Cod'])

    def show_resources(self):
        for resource in self.resources:
            print(resource)
            
    def show_animals(self):
        for animal in self.animals:
            print(animal)

    def description(self):
        print("THE RIVER:\nA steady steam of water.\n\nResources:")
        self.show_resources()
        print("Animals:")
        self.show_animals()

class mountain(region):
    def __init__(self, place):
        region.__init__(self, place)
        self.resources = (['Rock', 'Flint', 'Spring Water'])
        self.animals = (['Mountain Goat', 'Bird'])

    def show_resources(self):
        for resource in self.resources:
            print(resource)
            
    def show_animals(self):
        for animal in self.animals:
            print(animal)

    def description(self):
        print("THE MOUNTAINS:\nA giant hunk of rock.\n\nResources:")
        self.show_resources()
        print("Animals:")
        self.show_animals()

class plains(region):
    def __init__(self, place):
        region.__init__(self, place)
        self.resources = (['Twine', 'Corn', 'Dried Leaves'])
        self.animals = (['Bird', 'Sheep'])

    def show_resources(self):
        for resource in self.resources:
            print(resource)
            
    def show_animals(self):
        for animal in self.animals:
            print(animal)

    def description(self):
        print("THE PLAINS:\nA whole load of nothing but grass.\n\nResources:")
        self.show_resources()
        print("Animals:")
        self.show_animals()
# regions           
forest = forest("forest")
river = river("river")
mountain = mountain("mountains")
plains = plains("plains")
