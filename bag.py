class Bag:
    def __init__(self):
        self.items = []

    def totalWeight(self):
        totalWeight = 0
        for item in self.items:
            totalWeight += item.getWeight()
        return totalWeight

