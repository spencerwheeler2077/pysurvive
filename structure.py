from random import randint
import Items


def makeStructure():
    randNum = randint(1, 100)
    if randNum < 66:
        return Cabin()
    if randNum < 70:
        return Car()
    if randNum < 72:
        return Cabin()
    if randNum < 78:
        return BigTree()
    if randNum < 82:
        return Cave()
    if randNum < 90:
        return River()
    else:
        return NoStructure()


class Structure:
    def __init__(self):
        self.shelter = True
        self.hasWater = False
        self._itemChance = 0
        self._maxItems = 0
        self._items = []

    def takeItem(self):
        if self._maxItems == 0:
            print("There are no more items here")
            return None
        elif randint(1, 100) <= self._itemChance:
            self._maxItems -= 1
            print("You found an item!")
            return self._items[randint(0, len(self._items)-1)]
        else:
            print("Couldn't find anything in the structure. Maybe you should try again.")
            return None

    def message(self):
        return "There isn't a structure here"

    def __eq__(self, other):
        return type(other) == type(self)

    def __str__(self):
        return "Wasn't given a name"


class NoStructure(Structure):
    # This is a structure, place holder, basically there isn't anything here
    def __init__(self):
        super().__init__()
        self.shelter = False

    def __str__(self):
        return "Nothing is here"



class Car(Structure):
    def __init__(self):
        super().__init__()
        self._maxItems = randint(1, 4)
        self._itemChance = randint(75, 95)
        self._items = [Items.Map(), Items.Knife(), Items.WaterBottle(), Items.Tarp(), Items.Lighter(), Items.Match(),
                        Items.Watch(), Items.Match(), Items.Match()]

    def message(self):
        return "There is a abandoned car here!"

    def __str__(self):
        return "Car"


class Cabin(Structure):
    def __init__(self):
        super().__init__()
        self._maxItems = randint(2, 6)
        self._itemChance = randint(65, 85)
        self._items = [Items.Map(), Items.Map(), Items.Knife(), Items.Knife(), Items.Tarp(), Items.Match(),
                        Items.Match(), Items.FlashLight, Items.Match(), Items.Match(), Items.Food(100, 150)]

    def message(self):
        return "There is a abandoned cabin here!"

    def __str__(self):
        return "Cabin"


class Cave(Structure):
    def __init__(self):
        super().__init__()
        self._maxItems = randint(1, 2)
        self._itemChance = randint(40, 65)
        self._items = [Items.Knife(), Items.WaterBottle(), Items.Lighter(), Items.Match(),
                        Items.Match(),Items.FlashLight(), Items.Food(50, 200), Items.Food(70, 220)]

    def message(self):
        return "There is a cave here!"

    def __str__(self):
        return "Cave"


class BigTree(Structure):
    def __init__(self):
        super().__init__()
        self.shelter = False
        self._maxItems = [0, 0, 0, 1, 1, 2][randint(0, 5)]
        self._itemChance = randint(85, 97)
        self._items = [Items.Knife(), Items.WaterBottle(), Items.Tarp(), Items.Lighter(),
                        Items.Food(30, 100), Items.Food(50, 150), Items.Food(75, 250)]

    def message(self):
        return "There is a big tree here!"

    def __str__(self):
        return "Big Tree"

# TODO add campsite

# TODO add airplane

# TODO add cliff


class River(Structure):
    def __init__(self):
        super().__init__()
        self.shelter = False
        self.hasWater = True
        self._maxItems = [0, 0, 0, 1, 1, 2, 2, 3][randint(0, 7)]
        self._itemChance = randint(40, 60)
        self._items = [Items.WaterBottle(), Items.WaterBottle(), Items.WaterBottle(), Items.Tarp(), Items.Lighter(),
                        Items.Lighter(), Items.Food(30, 60), Items.Food(50, 100), Items.Food(100, 200)]

    def message(self):
        return "There is a river here!"

    def __str__(self):
        return "River"

