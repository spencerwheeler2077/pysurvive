from random import randint

import Items


class Bag:
    def __init__(self, difficulty):
        startItemsNum = 4-difficulty  # Hard gets 1, medium gets 2, easy gets 3
        self.__limit = 10
        self.items = Items.startItems(startItemsNum)
        self.matches = Items.Matches(startItemsNum + 1)
        self.__length = 0  # This is here to initialize self.__length and nothing else
        self.__countNumItems()

    def totalWeight(self):
        totalWeight = 0
        for item in self.items:
            totalWeight += item.getWeight()
        if self.matches is not None:
            return totalWeight + self.matches.getWeight()
        return totalWeight

    def getNumItems(self):
        return self.__length

    def isEmpty(self):
        return self.__length == 0

    def __countNumItems(self):
        if self.matches is not None:
            self.__length = 1 + len(self.items)

        else:
            self.__length = len(self.items)

    def addItem(self, item):

        if self.__length >= self.__limit:
            print("You can't put any more items so you have to toss this instead.")
            return
        if self.__length >= self.__limit - 3:
            print(f"Warning, you have {self.__length + 1} items, you can only have 10 in your bag")


        print(f"{item.name} was added to your bag")
        if item == Items.Matches():
            if self.matches is not None:
                self.matches.addMatch(item.getCount())
            else:
                self.matches = item

        else:
            self.items.append(item)
        self.__countNumItems()

    def removeRandomItem(self):
        itemIndex = randint(0, self.__length-1)

        if self.matches is not None:
            if itemIndex == 0:
                self.matches.useMatch(2)
                print(f"You lost 2 Matches!")
                if self.matches.getCount() <= 0:
                    self.matches = None
                self.__countNumItems()
                return Items.Matches(1)
            itemIndex -= 1

        itemIndex
        lostItem = self.items.pop(itemIndex)
        self.__countNumItems()
        return lostItem

    def hasMap(self):
        return Items.Map() in self.items

    def hasWatch(self):
        return Items.Watch() in self.items

    def canMakeFire(self):
        if len(self.items) != 0:
            return (self.matches is not None) or (Items.Lighter() in self.items)

    def hasWaterBottle(self):
        return Items.WaterBottle() in self.items

    def huntBonus(self):
        total = 0
        for i in self.items:
            total += i.huntBonus
        return total

    def forageBonus(self):
        total = 0
        for i in self.items:
            total += i.forageBonus
        return total

    def shelterBonus(self):
        total = 0
        for i in self.items:
            total += i.shelterBonus
        return total

    def searchBonus(self):
        total = 0
        for i in self.items:
            total += i.searchBonus
        return total

    def fireBonus(self):
        bonus = 0
        if self.matches is not None:
            if self.matches.getCount() == 1:
                self.matches = None
            else:
                self.matches.useMatch()

            bonus += 12
        # This returns the bonus that should be used to make fire 10 for a match, 0 without (lighter)
        for i in self.items:
            bonus += i.fireBonus
        return bonus

    def useBag(self):

        print()
        if len(self.items) == 0:
            print("You have no items in your bag.")
            return 0

        totalEnergy = 0
        while True:
            self.__printItems()
            print("Enter a number to check an item. If you want to exit the bag, enter n ")
            userInput = input("-> ")
            if userInput == "n" or userInput == "exit":
                return totalEnergy
            try:
                if self.matches is not None:
                    userIndex = int(userInput) - 2
                    if userIndex == -1:
                        self.matches.info()
                    else:
                        self.items[userIndex].info()
                else:
                    userIndex = int(userInput)-1
                    self.items[userIndex].info()
                use = input("Do you want to use this item? Enter y for yes, t to toss it, anything else for no. -> ")
                if use == "y":
                    item = self.items[userIndex]
                    totalEnergy += item.use()
                    if item.dispose:
                        self.items.pop(userIndex)
                elif use == "t":
                    if input("Are you sure you want to toss this? enter y if yes -> ") == "y":
                        print(f"You tossed the {self.items.pop(userIndex).name}")
                self.__countNumItems()  # reset the count of items in bag
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
