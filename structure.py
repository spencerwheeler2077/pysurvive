from random import randint
import Items


def makeStructure(minimum=1):
    rareStructures = [Car(), Cabin()]
    commonStructures = [BigTree(), Cave(), River(), Cliff(), Campsite(), Lake()]
    randNum = randint(minimum, 100)
    if randNum < 63:
        return NoStructure()
    if randNum < 71:
        return rareStructures[randint(0, len(rareStructures)-1)]
    else:
        return commonStructures[randint(0, len(commonStructures)-1)]


class Structure:
    def __init__(self):
        self.shelter = True
        self.hasWater = False
        self._itemChance = 0
        self._maxItems = 0
        self._items = []

    def takeItem(self, itemBonus):
        if self._maxItems == 0:
            print("There are no more items here")
            return None
        elif (randint(1, 100) + itemBonus) <= self._itemChance:
            self._maxItems -= 1
            print("You found an item!")
            return self._items.pop(randint(0, len(self._items) - 1))
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
        return "nothing"


class Car(Structure):
    def __init__(self):
        super().__init__()
        self._maxItems = randint(1, 4)
        self._itemChance = randint(75, 95)
        self._items = [Items.Map(), Items.Map(), Items.WaterBottle(), Items.Lighter(), Items.Matches(3), Items.Watch(),
                       Items.FlashLight(), Items.Matches(2)]

    def message(self):
        return "There is a abandoned car here!"

    def __str__(self):
        return "a car"


class Cabin(Structure):
    def __init__(self):
        super().__init__()
        self._maxItems = randint(2, 5)
        self._itemChance = randint(65, 85)
        self._items = [Items.Map(), Items.Map(), Items.Knife(), Items.Knife(), Items.Tarp(), Items.Rope(), Items.Matches(3),
                       Items.Matches(2), Items.Matches(1), Items.FlashLight(), Items.FlashLight(), Items.Trap()]

    def message(self):
        return "There is a abandoned cabin here!"

    def __str__(self):
        return "a cabin"


class Cave(Structure):
    def __init__(self):
        super().__init__()
        self._maxItems = randint(1, 2)
        self._itemChance = randint(40, 65)
        self._items = [Items.Knife(), Items.WaterBottle(), Items.Lighter(), Items.Matches(2), Items.Trap(),
                       Items.FlashLight(), Items.Food(50, 200), Items.Food(70, 220)]

    def message(self):
        return "There is a cave here!"

    def __str__(self):
        return "a cave"


class BigTree(Structure):
    def __init__(self):
        super().__init__()
        self.shelter = False
        self._maxItems = [0, 0, 1, 1, 1, 2][randint(0, 5)]
        self._itemChance = randint(85, 97)
        self._items = [Items.Knife(), Items.Trap(), Items.WaterBottle(), Items.Tarp(), Items.Lighter(),
                       Items.Food(30, 100), Items.Food(50, 150), Items.Food(75, 250)]

    def message(self):
        return "There is a big tree here!"

    def __str__(self):
        return "a big tree"


class Campsite(Structure):
    def __init__(self):
        super().__init__()
        self.shelter = False
        self._maxItems = randint(1, 2)
        self._itemChance = randint(85, 90)
        self._items = [Items.Map(), Items.Knife(), Items.WaterBottle(), Items.Tarp(), Items.Matches(3),
                       Items.Matches(2), Items.FlashLight(), Items.FlashLight(), Items.Trap()]

    def message(self):
        return "There is a abandoned campsite here!"

    def __str__(self):
        return "an abandoned campsite"


# TODO add airplane

class Cliff(Structure):
    def __init__(self):
        super().__init__()
        self.shelter = False
        self._maxItems = randint(0, 1)
        self._itemChance = randint(75, 85)
        self._items = [Items.Rope(), Items.Rope(), Items.Knife(), Items.WaterBottle(), Items.FlashLight(), Items.Trap(),
                       Items.WaterBottle()]

    def message(self):
        return "You found a cliff!"

    def __str__(self):
        return "a base of a cliff"


class River(Structure):
    def __init__(self):
        super().__init__()
        self.shelter = False
        self.hasWater = True
        self._maxItems = [0, 0, 1, 1, 2, 2, 3][randint(0, 6)]
        self._itemChance = randint(40, 60)
        self._items = [Items.WaterBottle(), Items.WaterBottle(), Items.Rope(), Items.Tarp(), Items.Lighter(),
                       Items.Matches(2), Items.Food(30, 60), Items.Food(50, 100), Items.Food(100, 200), Items.Trap()]

    def message(self):
        return "There is a river here!"

    def __str__(self):
        return "a river"


class Lake(Structure):
    def __init__(self):
        super().__init__()
        self.shelter = False
        self.hasWater = True
        self._maxItems = [0, 0, 1, 1, 1, 2, 2][randint(0, 6)]
        self._itemChance = randint(30, 45)
        self._items = [Items.WaterBottle(), Items.Knife(), Items.Matches(), Items.Food(30, 60), Items.Food(50, 100),
                       Items.Food(75, 120), Items.Trap(), Items.Rope(), Items.Rope(), Items.Trap()]

    def message(self):
        return "There is a lake here!"

    def __str__(self):
        return "a lake"
