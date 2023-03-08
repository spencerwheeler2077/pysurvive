import random


class Item:
    def __init__(self, weight):
        self.weight = weight
        self.name = "Item"

    def getWeight(self):
        return self.weight

    def use(self):
        print("No use right now")
        return 0

    def info(self):
        print("No use described")

    def __eq__(self, other):
        return type(self) == type(other)


class Map(Item):

    def __init__(self):
        super().__init__(10)
        self.name = "Map"

    def info(self):
        print(f"Map makes traveling more efficient, and lets you see how far you need to go until safety. Weighs {self.weight}")


class Knife(Item):

    def __init__(self):
        super().__init__(30)
        self.name = "Knife"

    def info(self):
        print(f"Having a knife makes hunting, foraging, and shelter making more effective. Weighs {self.weight}")


class WaterBottle(Item):

    def __init__(self):
        super().__init__(100)
        self.name = "WaterBottle"

    def info(self):
        print(f"Having a Water Bottle doubles you water limit. Weighs {self.weight}")


class Tarp(Item):

    def __init__(self):
        super().__init__(100)
        self.name = "Tarp"

    def info(self):
        print(f"A Tarp makes making a shelter significantly easier. Weighs {self.weight}")


class Match(Item):

    def __init__(self):
        super().__init__(1)
        self.name = "Matches"

    def info(self):
        print(f"Allows you to try to start a fire, more successful than a lighter but disappear after use. Weighs {self.weight}")


class Lighter(Item):
    def __init__(self):
        super().__init__(20)
        self.name = "Lighter"

    def info(self):
        print(f"Allows you to try to start a fire, less successful than matches but can be used multiple times. Weighs {self.weight}")


class FlashLight(Item):
    def __init__(self):
        super().__init__(30)
        self.name = "Flashlight"

    def info(self):
        print(f"Makes it easier to find items when searching structures. Weighs {self.weight}")


class Watch(Item):
    def __init__(self):
        super().__init__(10)
        self.name = "Watch"

    def info(self):
        print(f"You can keep track of time thanks to this! Weighs {self.weight}")


class Food(Item):
    def __init__(self, min=100, max=200):
        super().__init__(20)
        self.name = "Food"
        self.energyGiven = random.randint(min, max)
        # TODO give food a new name based on how much energy it gives

    def use(self):
        print(f"You ate the {self.name} and gained {self.energyGiven} energy")
        return self.energyGiven

    def info(self):
        print(f"Using this item, will give you {self.energyGiven} energy, weighs {self.weight}")
