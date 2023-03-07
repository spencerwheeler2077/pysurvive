import Items


class Bag:
    def __init__(self):
        self.items = [Items.Knife(), Items.Watch()]

    def totalWeight(self):
        totalWeight = 0
        for item in self.items:
            totalWeight += item.getWeight()
        return totalWeight

    def useBag(self):
        print()
        if len(self.items) == 0:
            print("You have no items in your bag.")
            return 0

        checkingBag = True
        while True:
            self.__printItems()
            print("Enter a number to check an item. If you want to exit the bag enter exit")
            userInput = input("-> ")
            if userInput == "exit":
                return 0
            try:
                userIndex = int(userInput) - 1
                self.items[userIndex].info()
                if input("Do you want to use this item? Enter y for yes, anything else for no. -> ") == "y":
                    return self.items[userIndex].use()
            except ValueError:
                print("That was not a number try again.")
            except IndexError:
                print("That number isn't one for an item in your bag.")



    def __printItems(self):
        count = 0
        for item in self.items:
            count += 1
            print(f"{count}. {item.name},", end=" ")

        print(f"\nTotal weight is {self.totalWeight()}")
