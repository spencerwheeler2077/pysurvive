class Bag:
    def __init__(self):
        self.items = []

    def totalWeight(self):
        totalWeight = 0
        for item in self.items:
            totalWeight += item.getWeight()
        return totalWeight

    def useBag(self):
        print()
        count = 1
        for item in self.items:

            print(f"{count}. {item.name},", end="")

        print(f"\nTotal weight is {self.totalWeight()}")


