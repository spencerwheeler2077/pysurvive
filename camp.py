import structure
from random import randint


class Camp:

    def __init__(self, penalty, start=False):
        if start:
            self.__structure = structure.makeStructure(72)
        else:
            self.__structure = structure.makeStructure()
        self.__shelter = self.__structure.shelter
        self.__water = self.__structure.hasWater
        self.__animals = randint(5, 17)
        self.__plants = randint(25, 60)
        self.__shelterOdds = randint(25, 50)
        self.__fireOdds = randint(55, 70)
        self.__info = []
        self.__hasAnimalReport = False
        self.__hasPlantReport = False
        self.__foundAnimalCount = 0
        self.__foundPlantCount = 0

        if self.__water:
            self.__info.append("There is water here.")
        if self.__shelter:
            self.__shelterMessage = f"You can use the {str(self.__structure)} here as a shelter!"
        else:
            self.__shelterMessage = "You don't have shelter here"
        self.fire = False
        self.fireMessage = "You haven't started a fire here"
        print(self.__structure.message())

    def info(self):
        print("These are the notes you have taken about this location...\n")
        for i in self.__info:
            print("- " + i)
        print(f"- There is {self.__structure} here.")
        print("- " + self.__shelterMessage)
        print("- " + self.fireMessage)
        print(f"- You have hunted {self.__foundAnimalCount} animals here.")
        print(f"- You have foraged successfully {self.__foundPlantCount} times here.")
        print("\nMaybe you can explore this place more to find more out!")

    def findStructure(self):
        self.__structure = structure.makeStructure(64)
        if not self.__water and self.__structure.hasWater:
            self.__water = True
            print("You found water!")
            self.__info.append("You found water here!")
        if self.__structure.shelter:
            self.__shelter = True


    def explore(self):
        if randint(1, 100) >= 40:
            self.animalReport()
        if randint(1, 100) >= 30:
            self.plantReport()
        self.searchWater(25)

    def animalReport(self):
        if not self.__hasAnimalReport:
            self.__hasAnimalReport = True
            if self.__animals > 15:
                message = "There are a TON of animals here!"
            elif self.__animals > 10:
                message = "There are a good amount of animals here."
            else:
                message = "There doesn't seem to be much animal life here..."
            print(message)
            self.__info.append(message)

    def plantReport(self):
        if not self.__hasPlantReport:
            self.__hasPlantReport = True
            if self.__plants <= 35:
                message = "There aren't many plants around"
            elif self.__plants <= 50:
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

    def destroyShelter(self):
        self.__shelter = False
        self.__shelterMessage = "Your shelter was Destroyed!"

    def hunt(self, itemBonus):
        huntAttempt = randint(1, 100) - itemBonus
        self.searchWater(0)
        if huntAttempt <= self.__animals:

            self.__animals -= 1
            self.__foundAnimalCount += 1
            return True
        else:
            return False

    def forage(self, itemBonus):
        forageAttempt = randint(1, 100) - itemBonus
        self.searchWater(-5)
        if forageAttempt <= self.__plants:
            self.__plants -= 1
            self.__foundPlantCount += 1
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
            self.__shelterMessage = "You have made a shelter at this site."
            self.__shelter = True
            print("You successfully made a shelter here")
        else:
            print("Something went wrong and your shelter isn't that great. You will need to try again.")
            self.__shelterOdds += 30

    def makeFire(self, itemBonus):
        fireAttempt = randint(1, 100) - itemBonus
        if fireAttempt <= self.__fireOdds:
            self.fireMessage = "You have started a fire at this site."
            self.fire = True
            print("You successfully made a fire!")
        else:
            print("All the wood you gathered was wet and you weren't able to start a fire.")

    def itemHunt(self, itemBonus):
        print(f"You checked the {str(self.__structure)}")
        return self.__structure.takeItem(itemBonus)

