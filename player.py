from random import randint
from bag import Bag
from camp import Camp
import Items
from Time import Time


class Player:
    def __init__(self, name, difficulty):
        self.bag = Bag()
        self.name = name
        self.difficulty = difficulty
        self.water = 1000
        self.traveled = 0
        self.exhaustion = 0
        self.hasMap = False
        self.time = Time()
        self.location = Camp()

        if difficulty == 1:
            self.distance = 1000
            self.penalty = 0
            self.energy = 1000
        if difficulty == 2:
            self.distance = 1500
            self.penalty = 2
            self.energy = 900
        if difficulty == 3:
            self.distance = 2200
            self.penalty = 5
            self.energy = 800

        self.actionMap = {
            "t": self.travel,
            "h": self.hunt,
            "b": self.useBag,
            "f": self.forage,
            "e": self.explore,
            "i": self.info,
            "m": self.makeShelter,
            "n": self.sleep,
            "c": self.checkThing,
            "x": self.fire,
        }

    def doAction(self, action):
        self.actionMap[action]()
        if self.location.foundWater():
            if self.bag.hasWaterBottle():
                self.water = 2000
            else:
                self.water = 1000

    def __useEnergy(self, small, most):
        energySpent = randint(small, most)
        print(f"You spent {energySpent} energy")
        self.energy = self.energy - energySpent
        self.time.action()


    def travel(self):
        # TODO rework this!
        if self.exhaustion >= 6:
            print("You are too tired to travel, you need to sleep first.")
            return
        if self.energy < 300:
            print("You need at least 300 energy to travel")
            return
        print('''You need at least 300 energy to travel, do you still wish to travel?\n''' +
              '''Type y to continue, anything else to quit. ''', end="")
        if input() != 'y':
            print("You did not travel")
            # TODO add time system here
            return
        energyNeed = randint(150, 250)
        travelCount = 1
        while self.energy - energyNeed > 150:
            print(f"You've spent {energyNeed} energy traveling, do you wish to continue?")
            if input("y to continue, anything else to stop ->") == "y":
                energyNeed += randint(25, 100)
                travelCount += 1
            else:
                break
        print(f"total energy spent {energyNeed}")
        self.location = Camp()
        # TODO calculate distance traveled
        return

    def hunt(self):
        maxEnergy = 40
        if self.energy < maxEnergy:
            print("You don't have enough energy to go hunting!")
            return
        print("You started hunting")

        success = self.location.hunt(self.bag.huntBonus()-self.penalty)
        if success:
            print("You were successful!")
            if self.location.fire:
                self.bag.addItem(Items.Food(200, 500))
            else:
                print("You don't have a fire so the food won't be that great to eat...")
                self.bag.addItem(Items.Food(125, 250))
        else:
            print("You didn't find any food on your hunt.")

        self.__useEnergy(20, maxEnergy)

    def forage(self):
        minEnergy = 20
        maxEnergy = 40
        if self.energy < maxEnergy:
            print("You don't have enough energy!")

        print("You started looking for food")
        success = self.location.forage(self.bag.huntBonus()-self.penalty)
        if success:
            print("You were successful!")
            self.bag.addItem(Items.Food(35, 100))
        else:
            print("You didn't find any food.")
        self.__useEnergy(minEnergy, maxEnergy)


    def useBag(self):
        energy = self.bag.useBag()
        if energy != 0:
            self.energy += energy
            if self.energy > 1200:
                self.energy = 1200

    def explore(self):
        print("You started exploring")
        self.location.explore()
        self.time.action()
        self.__useEnergy(15, 30)

    def info(self):
        # This should report all the things found out about the area
        self.location.info()

    def makeShelter(self):
        # TODO check if this is valid
        print("You made shelter")

    def sleep(self):
        # TODO check if this is valid
        self.exhaustion = 0
        self.time.sleep()
        print("You slept")

    def checkThing(self):
        print("You checked something")

    def fire(self):
        print("You made a fire")
