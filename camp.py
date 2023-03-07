import structure
from random import randint


class Camp:

    def __init__(self):
        self.__structure = structure.makeStructure()
        self.__shelter = self.__structure.shelter
        self.__water = self.__structure.hasWater
        self.__animals = randint(6, 15)
        self.__plants = randint(10, 50)
        self.__info = [self.__structure.message()]
        print(self.__structure.message())

    def foundWater(self):
        return self.__water()

    def hunt(self, itemBonus):
        huntAttempt = randint(1, 100) - itemBonus
        if huntAttempt < self.__animals:
            self.searchWater()
            return True
        else:
            return False

    def forage(self, itemBonus):
        forageAttempt = randint(1, 100) - itemBonus
        if forageAttempt < self.__plants:
            self.searchWater(10)
            return True
        return False

    def searchWater(self, num=0):
        if not self.__water:
            waterSearch = randint(1, 100)
            if waterSearch + num > 90:
                self.__water = True
                print("You found a source of water!")
