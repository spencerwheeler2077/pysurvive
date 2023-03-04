from random import randint
from bag import Bag


class Player:
    def __init__(self, name, difficulty):
        self.bag = Bag()
        self.name = name
        self.difficulty = difficulty
        self.water = 1000
        self.traveled = 0
        self.exhaustion = 0
        self.hasMap = False

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
            "b": self.bag,
            "f": self.forage,
            "e": self.explore,
            "i": self.info,
            "m": self.makeShelter,
            "n": self.sleep,
            "c": self.checkThing,
            "x": self.fire,
        }

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
        return [energyNeed, 0, 0, "placeHolder", True, 0, 0]
        # TODO calculate distance traveled
        # TODO create a new location

    def hunt(self):
        print("You Hunted")

    def bag(self):
        print("You opened your bag")

    def forage(self):
        print("You foraged")

    def explore(self):
        print("You explored")

    def info(self):
        # This should report all the things found out about the area
        print("You looked for info")

    def makeShelter(self):
        # TODO check if this is valid
        print("You made shelter")

    def sleep(self):
        # TODO check if this is valid
        self.exhaustion = 0
        print("You slept")

    def checkThing(self):
        print("You checked something")

    def fire(self):
        print("You made a fire")
