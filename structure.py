from random import randint
import Items


def makeStructure():
    randNum = randint(1, 100)
    if randNum < 66:
        return Structure()
    if randNum < 70:
        return Car()
    if randNum < 74:
        return Cabin()
    if randNum < 80:
        return BigTree()
    if randNum < 86:
        return Cave()
    if randNum < 92:
        return River()
    else:
        return Structure()



class Structure:
    def __init__(self):
        self.shelter = True
        self.hasWater = False
        self.__itemChance = 0
        self.__maxItems = 0
        self.takenItems = 0
        self.__items = []

    def takeItem(self):
        if self.__maxItems == self.takenItems:
            print("There are no more items here")
            return None
        elif randint(1, 100) <= self.__itemChance:
            self.takenItems += 1
            return self.__items[randint(0, len(self.__items)-1)]
        else:
            print("Couldn't find anything in the structure. Maybe you should try again.")
            return None

    def message(self):
        print("There isn't a structure here")


class Car(Structure):
    def __init__(self):
        super().__init__()
        self.__maxItems = randint(2, 4)
        self.__itemChance = randint(75, 95)
        self.__items = [Items.Map(), Items.Knife(), Items.WaterBottle(), Items.Tarp(), Items.Lighter(), Items.Match(),
                        Items.Match(), Items.Match()]

    def message(self):
        print("There is a abandoned car here!")


class Cabin(Structure):
    def __init__(self):
        super().__init__()
        self.__maxItems = randint(2, 6)
        self.__itemChance = randint(65, 85)
        self.__items = [Items.Map(), Items.Map(), Items.Knife(), Items.Knife(), Items.Tarp(), Items.Match(),
                        Items.Match(), Items.Match(), Items.Match(), Items.Food()]

    def message(self):
        print("There is a abandoned cabin here!")


class Cave(Structure):
    def __init__(self):
        super().__init__()
        self.__maxItems = randint(1, 2)
        self.__itemChance = randint(40, 65)
        self.__items = [Items.Knife(), Items.WaterBottle(), Items.Lighter(), Items.Match(),
                        Items.Match(), Items.Food(), Items.Food()]

    def message(self):
        print("There is a cave here!")


class BigTree(Structure):
    def __init__(self):
        super().__init__()
        self.shelter = False
        self.__maxItems = [0, 0, 1, 2][randint(0, 3)]
        self.__itemChance = randint(85, 99)
        self.__items = [Items.Knife(), Items.WaterBottle(), Items.Tarp(), Items.Lighter(),
                        Items.Food(), Items.Food(), Items.Food()]

    def message(self):
        print("There is a Big Tree here!")


class River(Structure):
    def __init__(self):
        super().__init__()
        self.shelter = False
        self.hasWater = True
        self.__maxItems = [0, 0, 0, 1, 1, 2, 2, 3][randint(0, 7)]
        self.__itemChance = randint(40, 60)
        self.__items = [Items.WaterBottle(), Items.WaterBottle(), Items.WaterBottle(), Items.Tarp(), Items.Lighter(),
                        Items.Lighter(), Items.Food(), Items.Food(), Items.Food()]

    def message(self):
        print("There is a river here!")

