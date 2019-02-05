class Region():
    def __init__(self, place, resources, animals, description):
        # i know you had description as a function name before, feel free to
        # rename this and change it back if you'd like
        self.place = place
        self.description = description
        self.resources = resources
        self.animals = animals

    def show_resources(self):
        for resource in self.resources:
            print(resource)

    def show_animals(self):
        for animal in self.animals:
            print(animal)

    def show_description(self):
        print(f"THE {self.place.upper()}:\n{self.description}\n\nResources:")
        self.show_resources()
        print("Animals:")
        self.show_animals()


class Forest(Region):
    def __init__(self, place):
        self.place = place
        self.resources = (["Wood", "Wild Berry", "Stick"])
        self.animals = (["Deer", "Bird", "Fox"])

        self.description = "Full of trees."

        super().__init__(self.place, self.resources, self.animals, self.description)


class River(Region):
    def __init__(self, place):
        self.place = place
        self.resources = (["Water", "Clay", "Reeds"])
        self.animals = (["Salmon", "Cod"])
        self.description = "A steady steam of water."

        super().__init__(self.place, self.resources, self.animals, self.description)


class Mountain(Region):
    def __init__(self, place):
        self.place = place
        self.resources = (["Rock", "Flint", "Spring Water"])
        self.animals = (["Mountain Goat", "Bird"])
        self.description = "A giant hunk of rock."
        super().__init__(self.place, self.resources, self.animals, self.description)


class Plains(Region):
    def __init__(self, place):
        self.place = place
        self.resources = (["Twine", "Corn", "Dried Leaves"])
        self.animals = (["Bird", "Sheep"])
        self.description = "A whole load of nothing but grass."
        super().__init__(self.place, self.resources, self.animals, self.description)


class World():
    def __init__(self):
        self.forest = Forest("forest")
        self.river = River("river")
        self.mountain = Mountain("mountain")
        self.plains = Plains("plains")
