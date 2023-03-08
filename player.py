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
            "c": self.checkStructure,
            "x": self.fire,
            "w": self.wait,
        }

    def doAction(self, action):
        if self.exhaustion > 13:
            if action != "s" or "w":
                print("You are too exhausted to do anything but sleep or wait!")
                return
        self.actionMap[action]()

        # else: TODO make it so water is taken away after doing an action

    def addExhaustion(self, num):
        self.exhaustion += num
        if self.exhaustion >= 6:
            print("Starting to get tired...")
        elif self.exhaustion >= 9:
            print("You are really tired now.")
        elif self.exhaustion >= 12:
            print("You will need to sleep soon you can barely do anything you're so tired.")

    def __useWater(self, small, most):
        if self.location.foundWater():
            if self.bag.hasWaterBottle():
                self.water = 2000
            else:
                self.water = 1000
            return
        waterSpent = randint(small, most)
        print(f"You used {waterSpent} water")
        self.water = self.water - waterSpent
        self.time.action()

    def __useEnergy(self, small, most):
        self.__useWater(small*2, most*2)
        energySpent = randint(small, most)
        print(f"You spent {energySpent} energy")
        self.energy = self.energy - energySpent
        self.time.action()

    def __addEnergy(self, amount):
        self.energy += amount
        if self.energy > 1200:
            self.energy = 1200

    def travel(self):
        # TODO rework this!
        if self.exhaustion >= 6:
            print("You are too tired to travel, you need to sleep first.")
            return
        if self.energy < 300:
            print("You need at least 300 energy to travel")
            return
        if self.water < 600:
            print("You need at least 600 water to travel")

        print('''You need at least 300 energy to travel, do you still wish to travel?\n''' +
              '''Type y to continue, anything else to quit. ''', end="")
        if input() != 'y':
            print("You did not travel")
            return
        energyNeed = randint(150, 250)
        travelCount = 1
        while self.energy - energyNeed > 150 and self.water - energyNeed*2 > 300:
            print(f"You've spent {energyNeed} energy traveling, and do you wish to continue?")
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
        if self.energy != 0:
            self.__addEnergy(energy)

    def explore(self):
        print("You started exploring")
        self.location.explore()
        self.time.action()
        self.__useEnergy(15, 30)

    def info(self):
        # This should report all the things found out about the area
        self.location.info()

    def makeShelter(self):
        if self.location.hasShelter():
            print("You already have a shelter")
        else:
            self.location.makeShelter(self.bag.shelterBonus()-self.penalty)

    def sleep(self):
        if self.time.canSleep():
            self.exhaustion = 0
            self.time.sleep()
            print("You slept")
            if self.location.hasShelter():
                self.__addEnergy(randint(10, 20))
            elif not self.location.hasFire():  # This runs if there is no shelter and no fire
                self.__useEnergy(0, randint(15, 30))
                print("You didn't sleep well it was hard without a shelter and no fire")
            else:  # This runs if there is a fire but no shelter
                self.__addEnergy(randint(10, 20))

        else:
            print("You cannot sleep right now. It is not late enough")

    def wait(self):
        self.time.action()
        print("You waited around relaxing for an hour")

    def checkStructure(self):
        print("You checked area")

    def fire(self):
        print("You made a fire")
