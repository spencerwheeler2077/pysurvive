import structure
from random import randint


class Camp:

    def __init__(self):
        self.__structure = structure.makeStructure()
        self.__shelter = self.__structure.shelter
        self.__water = self.__structure.hasWater
        self.__animals = randint(6, 15)
        self.__plants = randint(15, 56)
        self.__info = [self.__structure.message()]
        self.__hasAnimalReport = False
        self.__hasPlantReport = False
        if self.__water:
            self.__info.append("There is water here.")
        self.fire = False
        print(self.__structure.message())

    def info(self):
        print("These are the notes you have taken about this location...\n")
        for i in self.__info:
            print("- " + i)
        print("\nMaybe you can explore this place more to find more out!")

    def explore(self):
        if randint(1, 100) >= 40:
            self.animalReport()
        if randint(1, 100) > 20:
            self.plantReport()
        self.searchWater(20)

    def animalReport(self):
        if not self.__hasAnimalReport:
            self.__hasAnimalReport = True
            if self.__animals > 10:
                self.__info.append("There are an good amount of animals here")
            else:
                self.__info.append("There arent a lot of animals here")

    def plantReport(self):
        if not self.__hasPlantReport:
            self.__hasPlantReport = True
            if self.__plants < 25:
                self.__info.append("There isn't many plants around")
            elif self.__plants < 45:
                self.__info.append("There is an normal amount of plant life here")
            else:
                self.__info.append("There is a lot of edible plants here!")

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
            self.searchWater(14)
            return True
        return False

    def searchWater(self, num=0):
        if not self.__water:
            waterSearch = randint(1, 100)
            if waterSearch + num > 80:
                self.__water = True
                print("You found a source of water!")
                self.__info.append("You have found a close source of fresh water at this location.")
