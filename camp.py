import structure
from random import randint


class Camp:

    def __init__(self):
        self.__structure = structure.makeStructure()
        self.__shelter = self.__structure.shelter
        self.__water = self.__structure.hasWater
        self.__animals = randint(6, 15)
        self.__plants = randint(15, 56)
        self.__shelterOdds = randint(20, 35)
        self.__fireOdds = randint(55, 70)
        self.__info = [self.__structure.message()]
        self.__hasAnimalReport = False
        self.__hasPlantReport = False
        if self.__water:
            self.__info.append("There is water here.")
        if self.__shelter:
            self.__info.append(f"You can use the {str(self.__structure)} here as a shelter!")
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
        if randint(1, 100) >= 20:
            self.plantReport()
        self.searchWater(20)

    def animalReport(self):
        if not self.__hasAnimalReport:
            self.__hasAnimalReport = True
            if self.__animals > 10:
                message = "There are a good amount of animals here"
            else:
                message = "There arent a lot of animals here"
            print(message)
            self.__info.append(message)

    def plantReport(self):
        if not self.__hasPlantReport:
            self.__hasPlantReport = True
            if self.__plants < 25:
                message = "There aren't many plants around"
            elif self.__plants < 45:
                message = "There is a normal amount of plant life here"
            else:
                message = "There is a lot of edible plants here!"
            print(message)
            self.__info.append(message)

    def foundWater(self):
        return self.__water

    def hasShelter(self):
        return self.__shelter

    def hasFire(self):
        return self.fire

    def hasStructure(self):
        return self.__structure != structure.NoStructure()

    def hunt(self, itemBonus):
        huntAttempt = randint(1, 100) - itemBonus
        if huntAttempt <= self.__animals:
            self.searchWater(15)
            self.__animals -= 1
            return True
        else:
            return False

    def forage(self, itemBonus):
        forageAttempt = randint(1, 100) - itemBonus
        if forageAttempt <= self.__plants:
            self.searchWater(20)
            self.__plants -= 1
            return True
        return False

    def searchWater(self, num=0):
        if not self.__water:
            waterSearch = randint(1, 100)
            if waterSearch + num >= 75:
                self.__water = True
                print("You found a source of water!")
                self.__info.append("You have found a close source of fresh water at this location.")

    def makeShelter(self, itemBonus):
        shelterAttempt = randint(1, 100) - itemBonus
        if shelterAttempt <= self.__shelterOdds:
            self.__info.append("You have made a shelter at this site.")
            self.__shelter = True
            print("You successfully made a shelter here")
        else:
            print("Something went wrong and your shelter isn't that great. You will need to try again.")
            self.__shelterOdds += 25

    def makeFire(self, itemBonus):
        fireAttempt = randint(1, 100) - itemBonus
        if fireAttempt <= self.__fireOdds:
            self.__info.append("You have started a fire at this site.")
            self.fire = True
            print("You successfully made a fire!")
        else:
            print("All the wood you gathered was wet and you weren't able to start a fire.")

    def itemHunt(self):
        print(f"You checked the {str(self.__structure)}")
        return self.__structure.takeItem()
