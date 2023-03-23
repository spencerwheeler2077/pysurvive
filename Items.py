import random


def startItems(difficulty):
    items = [Map(), Lighter(), Knife(), Watch(), Food(100, 100), WaterBottle()]
    result = []
    for i in range(difficulty):
        result.append(items.pop(random.randint(0, len(items)-1)))
    return result


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
        self.name = "Water Bottle"

    def info(self):
        print(f"Having a Water Bottle doubles you water limit. Weighs {self.weight}")


class Tarp(Item):

    def __init__(self):
        super().__init__(100)
        self.name = "Tarp"

    def info(self):
        print(f"A Tarp makes making a shelter significantly easier. Weighs {self.weight}")


class Matches(Item):

    def __init__(self, count=1):
        super().__init__(1)
        self.name = "Matches"
        self._number = count

    def addMatch(self, num):
        self._number += num
    def useMatch(self):
        self._number -= 1

    def getCount(self):
        return self._number

    def getWeight(self):
        return self.weight*self._number

    def info(self):
        print(f"Allows you to try to start a fire, more successful than a lighter but disappear after use.\nYou have {self._number}. Weighs {self.weight}")


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


class Trap(Item):
    def __init__(self):
        super().__init__(50)
        self.name = "Trap"

    def info(self):
        print(f"This helps you be more effective while hunting. Weighs {self.weight}")


class Rope(Item):
    def __init__(self):
        super().__init__(30)
        self.name = "Rope"

    def info(self):
        print(f"This Rope will be useful when making a shelter! Weights {self.weight}")


class Food(Item):
    def __init__(self, min=100, max=200):
        super().__init__(20)
        self.energyGiven = random.randint(min, max)
        self.name = self.__giveName()

    def use(self):
        print(f"You ate the {self.name} and gained {self.energyGiven} energy")
        return self.energyGiven

    def info(self):
        print(f"Using this item, will give you {self.energyGiven} energy, weighs {self.weight}")

    def __giveName(self):
        if self.energyGiven < 40:
            return "Wild Greens"
        elif self.energyGiven < 60:
            return "Wild Berries"
        elif self.energyGiven < 75:
            return "Mushrooms"
        elif self.energyGiven <= 100:
            return "Nuts"
        # 150 - 250 unCooked
        elif self.energyGiven < 175:
            return "Raw Squirrel"
        elif self.energyGiven < 185:
            return "Raw Snake"
        elif self.energyGiven < 215:
            return "Raw Rabbit"
        elif self.energyGiven < 255:
            return "Raw Fish"
        elif self.energyGiven < 310:
            return "Cooked Squirrel"
        elif self.energyGiven < 340:
            return "Cooked Snake"
        elif self.energyGiven < 400:
            return "Cooked Fish"
        else:
            return "Cooked Rabbit"
