from random import randint

import Items


class Bag:
    def __init__(self):
        self.__limit = 10
        self.items = [Items.Knife(), Items.Food(25, 100), Items.Watch(), Items.Lighter()]
        self.__length = len(self.items)
        self.matches = None

    def totalWeight(self):
        totalWeight = 0
        for item in self.items:
            totalWeight += item.getWeight()
        if self.matches is not None:
            return totalWeight + self.matches.getWeight()
        return totalWeight

    def numItems(self):
        if self.matches is not None:
            self.__length = 1 + len(self.items)

        else:
            self.__length = len(self.items)

    def addItem(self, item):

        if self.__length >= self.__limit:
            print("You can't put any more items so you have to toss this instead.")
            return
        if self.__length >= self.__limit - 3:
            print(f"Warning, you have {self.__length} items, you can only have 10 in your bag")


        print(f"{item.name} was added to your bag")
        if item == Items.Matches():
            if self.matches is not None:
                self.matches.addMatch(item.getCount())
            else:
                self.matches = item

        else:
            self.items.append(item)
        self.numItems()

    def removeRandomItem(self):
        lostItem = self.items.pop(randint(0, len(self.items)-1))
        print(f"You lost a {lostItem.name}")

    # Since You shouldn't have expect to have more than 10 items these searches shouldn't matter too much even though
    # They are inefficient. This could be improved.
    def huntBonus(self):
        if Items.Knife() in self.items:
            return 12
        else:
            return 0

    def hasMap(self):
        return Items.Map() in self.items

    def hasWatch(self):
        return Items.Watch() in self.items

    def canMakeFire(self):
        if len(self.items) != 0:
            return Items.Matches() is not None or Items.Lighter() in self.items

    def hasWaterBottle(self):
        return Items.WaterBottle() in self.items

    def shelterBonus(self):
        total = 0
        if Items.Knife() in self.items:
            total += 10
        if Items.Tarp() in self.items:
            total += 10
        return total

    def hasFlashLight(self):
        return Items.FlashLight() in self.items

    def useMatch(self):
        if self.matches is not None:
            if self.matches.getCount() == 1:
                self.matches = None
            else:
                self.matches.useMatch()

            return 10
        # This returns the bonus that should be used to make fire 10 for a match, 0 without (lighter)
        return 0

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
                use = input("Do you want to use this item? Enter y for yes, t to toss it, anything else for no. -> ")
                if use == "y":
                    totalEnergy += self.items[userIndex].use()
                    self.items.pop(userIndex)
                elif use == "t":
                    if input("Are you sure you want to toss this? enter y if yes -> ") == "y":
                        print(f"You tossed the {self.items.pop(userIndex).name}")
                self.numItems()  # reset the count of items in bag
            except ValueError:
                print("That was not a number try again.")
            except IndexError:
                print("That number isn't one for an item in your bag.")
            print()

    def __printItems(self):
        count = 0
        if self.matches is not None:
            count += 1
            print(f"{count}. {self.matches.name} x{self.matches.getCount()}", end=" ")
        for item in self.items:
            count += 1
            print(f"{count}. {item.name} ", end=" ")
            if count % 5 == 0:
                print()


        print(f"\nTotal weight is {self.totalWeight()}")
