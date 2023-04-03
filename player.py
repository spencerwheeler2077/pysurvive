from random import randint
from random import uniform as ranFloat
from bag import Bag
from camp import Camp
import Items
from Time import Time


class Player:
    def __init__(self, name, difficulty):
        self.actionCount = 0
        self.bag = Bag(difficulty)
        self.name = name
        self.water = 1000
        self.exhaustionLimit = 15
        self.traveled = 0
        self.exhaustion = 0
        self.time = Time()


        if difficulty == 1:
            self.distance = randint(950, 1150)
            self.penalty = 0
            self.energy = 1000
        if difficulty == 2:
            self.distance = randint(1150, 1350)
            self.penalty = 3
            self.energy = 900
        if difficulty == 3:
            self.distance = randint(1350, 1600)
            self.penalty = 6
            self.energy = 850

        self.location = Camp(self.penalty)
        self.actionMap = {
            "t": self.travel,
            "h": self.hunt,
            "b": self.useBag,
            "f": self.forage,
            "e": self.explore,
            "i": self.info,
            "m": self.makeShelter,
            "s": self.sleep,
            "c": self.checkStructure,
            "x": self.fire,
            "w": self.wait,
            "q": self.quit,
        }

    def printActions(self):
        if self.exhaustion > self.exhaustionLimit:
            print("Sleep (s), Wait (w), Bag (b), Info (i), Quit (q)")
        else:
            print("Actions: \nTravel (t), Bag (b), Hunt (h) Forage (f), Explore (e), Info (i), wait (w), ")
            if not self.location.hasShelter():
                print("Make Shelter (m),", end=" ")
            if self.time.canSleep():
                print("Sleep (s),", end=" ")
            if self.location.hasStructure():
                print("Check structure (c),", end=" ")
            if (not self.location.hasFire()) and self.bag.canMakeFire():
                print("Start Fire (x)", end=" ")
            print("Quit (q)")

    def printInfo(self):
        print(f"Name: {self.name}")
        if self.bag.hasWatch():
            print(self.time)
        else:
            print(self.time.getLight())

        if self.bag.hasMap():
            print("[", end="")
            percentDistance = int(self.traveled / self.distance * 10)
            for i in range(percentDistance):
                print("X", end="")
            for i in range((10 - percentDistance)):
                print(end=" ")
            print("]")

        print(f"Energy: {self.energy}")
        print(f"Water: {self.water}")
        print()

    def doAction(self, action):
        try:
            if self.exhaustion > self.exhaustionLimit:
                if action != "s" and action != "w" and action != "b" and action != "i":
                    print("You are too exhausted to do anything but sleep, wait, Bag, or Info!")
                    return
            self.actionMap[action]()
            self.actionCount += 1

        except KeyError:
            print("Invalid Action")

    def __addExhaustion(self, num):
        self.exhaustion += num
        if self.exhaustion == 7:
            print("Starting to get tired...")
        elif self.exhaustion == 10:
            print("You are really tired now.")
        elif self.exhaustion == 14:
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
        if self.water < 1:
            self.__death("You have run out of water.")

    def __useEnergy(self, least, most):

        self.__useWater(least * 2, most * 2)
        energySpent = randint(least, most)
        print(f"You spent {energySpent} energy")
        self.energy = self.energy - energySpent
        if self.energy < 1:
            self.__death("You have run out of energy, maybe next time eat more food.")

    def __death(self, message):
        print("You have died.")
        print(message)
        self.__gameReport()
        exit(0)

    def winMessage(self):
        print("You have reached civilization!")
        print("You have won the game!")
        self.__gameReport()
        exit(0)

    def __gameReport(self):
        print(f"- You traveled {self.traveled} out of the {self.distance} needed.")
        print(f"- You found {self.bag.getNumItems()} items")
        print(f"- You survived for {self.time.getDay()} in game Days.")
        print(f"- It took you {self.time.realTimeElapsed()} minutes.")
        print(f"- You did {self.actionCount} actions")
        print("\nThanks for playing!")

    def __addEnergy(self, amount):
        self.energy += amount
        if self.energy > 1200:
            self.energy = 1200

    def travel(self):
        if self.exhaustion >= 6:
            print("You are too tired to travel, you need to sleep first.")
            return
        if self.energy < 300:
            print("You need at least 300 energy to travel")
            return
        if self.water < 600:
            print("You need at least 600 water to travel")
            return

        print('''You need at least 300 energy to travel, do you still wish to travel?\n''' +
              '''Type y to continue, anything else to quit. ''', end="")
        if input("-> ") != 'y':
            print("You did not travel")
            return
        energyNeed = randint(150, 250)
        travelCount = 1
        while self.energy - energyNeed > 150 and self.water - energyNeed * 2 > 300:
            print(f"You've spent about {energyNeed} energy traveling, and do you wish to continue?")
            if input("y to continue, anything else to stop -> ") == "y":
                energyNeed += randint(25, 100)
                travelCount += 1
            else:
                break
        print()
        self.location = Camp(self.penalty)
        print()
        self.__useEnergy(energyNeed, energyNeed + 5 + self.penalty)
        self.__addExhaustion(travelCount + 2)
        self.time.travel(travelCount + 1)
        print()

        self.traveled += self.__findTravelDistance(energyNeed, self.bag.hasMap())

        return

    def __findTravelDistance(self, energyUsed, hasMap):
        if hasMap:
            return int((4 * energyUsed) // 5 - self.penalty * 5 - self.bag.totalWeight() // 2)
        else:
            return int(((4 * energyUsed) // 5 - self.penalty * 5 - self.bag.totalWeight() // 2) * ranFloat(.6, 1))

    def hunt(self):
        maxEnergy = 35 + self.penalty
        if self.energy < maxEnergy:
            print("You don't have enough energy to go hunting!")
            return
        print("You started hunting")

        success = self.location.hunt(self.bag.huntBonus() - self.penalty)
        if success:
            print("You were successful!")
            if self.location.fire:
                self.bag.addItem(Items.Food(250, 525))
            else:
                print("You don't have a fire so the food won't be that great to eat...")
                self.bag.addItem(Items.Food(150, 275))
        else:
            print("You didn't find any food on your hunt.")

        self.__addExhaustion(1)
        self.__useEnergy(20, maxEnergy)
        self.time.action()
        print()

    def forage(self):
        minEnergy = 15
        maxEnergy = 30 + self.penalty
        if self.energy < maxEnergy:
            print("You don't have enough energy!")
            return

        print("You started looking for food")
        success = self.location.forage(self.bag.forageBonus() - self.penalty)
        if success:
            print("You were successful!")
            self.bag.addItem(Items.Food(35, 100))
        else:
            print("You didn't find any food.")
        self.__addExhaustion(1)
        self.__useEnergy(minEnergy, maxEnergy)
        self.time.action()
        print()

    def useBag(self):

        energy = self.bag.useBag()
        if self.energy != 0:
            self.__addEnergy(energy)
        print()

    def explore(self):
        print("You started exploring")
        self.location.explore()
        self.__addExhaustion(1)
        self.time.action()
        self.__useEnergy(10+self.penalty, 20+self.penalty)
        print()

    def info(self):
        # This should report all the things found out about the area
        self.location.info()

    def makeShelter(self):
        if self.location.hasShelter():
            print("You already have a shelter")
            return

        self.location.makeShelter(self.bag.shelterBonus() - self.penalty)
        self.__addExhaustion(1)
        self.__useEnergy(25, 35)
        self.time.action()

    def sleep(self):
        if self.time.canSleep():
            self.exhaustion = 0
            self.time.sleep()
            print("You slept")
            EnergyLoss = 0
            if self.location.hasShelter():
                self.__addEnergy(randint(30-self.penalty, 45))
                print("The Shelter helped you sleep")
            else:
                EnergyLoss += randint(50+self.penalty, 80)
                print("It would have been nice to sleep in a shelter.")

            if self.location.hasFire():  # This runs if there is no shelter and no fire
                self.__addEnergy(randint(-5, 15-self.penalty))
                print("The fire helped you sleep")
            else:
                EnergyLoss += randint(10+self.penalty, 25)
                print("It would have been nice to sleep, with a fire...")
            if EnergyLoss > 0:
                self.__useEnergy(EnergyLoss, EnergyLoss+self.penalty)
        else:
            print("You cannot sleep right now. It is not late enough")

        print()

    def wait(self):
        self.time.action()
        print("You waited around relaxing for an hour")
        self.__useEnergy(-1, 4+self.penalty)

    def quit(self):
        intentionCheck = input("Are you sure you want to exit? enter y to quit \n-> ")
        if intentionCheck == "y":
            print("You quit the game")
            exit()

    def checkStructure(self):
        if self.location.hasStructure():
            foundItem = self.location.itemHunt(self.bag.searchBonus())
            if foundItem is not None:
                self.bag.addItem(foundItem)
            self.__addExhaustion(1)
            self.__useEnergy(15, 30+self.penalty)
            self.time.action()

    def fire(self):
        if self.bag.canMakeFire():
            self.location.makeFire(self.bag.fireBonus())
            self.__addExhaustion(1)
            self.__useEnergy(25, 50 + self.penalty)
            self.time.action()
