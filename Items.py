import random


class Item:
    def __init__(self, weight):
        self.weight = weight

    def getWeight(self):
        return self.weight

    def use(self):
        print("No use right now")
        return 0

    def info(self):
        print("No use described")


class Map(Item):

    def __init__(self):
        super().__init__(10)

    def info(self):
        print(f"Map makes traveling more efficient, and lets you see who far you need to go until safety. Weighs {self.weight}")


class Knife(Item):

    def __init__(self):
        super().__init__(30)

    def info(self):
        print(f"Having a knife makes hunting, foraging, and shelter making more effective. Weighs {self.weight}")


class WaterBottle(Item):

    def __init__(self):
        super().__init__(100)

    def info(self):
        print(f"Having a Water Bottle doubles you water limit. Weighs {self.weight}")


class Tarp(Item):

    def __init__(self):
        super().__init__(100)

    def info(self):
        print(f"A Tarp makes making a shelter significantly easier. Weighs {self.weight}")


class Match(Item):

    def __init__(self):
        super().__init__(1)

    def info(self):
        print(f"Allows you to try to start a fire, more successful than a lighter but disappear after use. Weighs {self.weight}")


class Lighter(Item):
    def __init__(self):
        super().__init__(20)

    def info(self):
        print(f"Allows you to try to start a fire, less successful than matches but can be used multiple times. Weighs {self.weight}")


class Food(Item):
    def __init__(self):
        super().__init__(20)
        self.energyGiven = random.randint(100, 400)

    def use(self):
        print(f"You ate the food and gained {self.energyGiven} energy")
        return self.energyGiven

    def info(self):
        print(f"You can eat this and gain {self.energyGiven} energy, weighs {self.weight}")
