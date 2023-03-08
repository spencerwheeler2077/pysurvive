from random import randint

import Items


class Bag:
    def __init__(self):
        self.items = [Items.Knife(), Items.Watch(), Items.Food(25, 100)]

    def totalWeight(self):
        totalWeight = 0
        for item in self.items:
            totalWeight += item.getWeight()
        return totalWeight

    def addItem(self, item):
        print(f"{item.name} was added to your bag")
        self.items.append(item)

    def removeRandomItem(self):
        lostItem = self.items.pop(randint(0, len(self.items)-1))
        print(f"You lost a {lostItem.name}")

    # Since You shouldn't have expect to have more than 10 items these searches shouldn't matter too much even though
    # They are inefficient. This could be improved.
    def huntBonus(self):
        if Items.Knife in self.items:
            return 12
        else:
            return 0

    def hasMap(self):
        return Items.Map in self.items

    def hasWatch(self):
        return Items.Watch in self.items

    def canMakeFire(self):
        return Items.Match in self.items or Items.Lighter in self.items

    def hasWaterBottle(self):
        return Items.WaterBottle in self.items

    def shelterBonus(self):
        total = 0
        if Items.Knife in self.items:
            total += 10
        if Items.Tarp in self.items:
            total += 10

    def hasFlashLight(self):
        return Items.FlashLight in self.items

    def useBag(self):

        print()
        if len(self.items) == 0:
            print("You have no items in your bag.")
            return 0

        totalEnergy = 0
        while True:
            self.__printItems()
            print("Enter a number to check an item. If you want to exit the bag enter exit")
            userInput = input("-> ")
            if userInput == "exit":
                return totalEnergy
            try:
                userIndex = int(userInput) - 1
                self.items[userIndex].info()
                if input("Do you want to use this item? Enter y for yes, anything else for no. -> ") == "y":
                    totalEnergy += self.items[userIndex].use()
                    self.items.pop(userIndex)
            except ValueError:
                print("That was not a number try again.")
            except IndexError:
                print("That number isn't one for an item in your bag.")

            print()

    def __printItems(self):
        count = 0
        for item in self.items:
            count += 1
            print(f"{count}. {item.name} ", end=" ")
            if count > 5:
                print()

        print(f"\nTotal weight is {self.totalWeight()}")
