import random
from player import Player


class Game:
    def __init__(self, test=False, strength=1):
        if not test:
            self.welcome()
            name = input('Player\'s name -> ')
            difficulty = ""
            while difficulty not in ['1', '2', '3']:
                difficulty = input("Enter 1 for easy, 2 for medium, 3 for hard -> ")
            difficulty = int(difficulty)
        else:
            name = "TestPlayer"
            difficulty = strength
        print()
        self.player = Player(name, difficulty)

        self.play()

    def turn(self):
        print("---------------------------------")
        self.player.printInfo()
        self.player.printActions()
        print("---------------------------------")

        action = input("-> ")
        self.player.doAction(action)

    def play(self):

        while self.player.traveled < self.player.distance:
            self.turn()

        self.player.winMessage()

    def welcome(self):
        print("\n---------------------------------\nWelcome to pySurvive!")
        print('''\nYou are lost in a forest, and must try to escape with your life.
There are many actions available to you that will help you accomplish this
task. Each of these tasks can be done by typing in the correlating key into
the console, and then pressing enter. Try your best to do it in the best
time, taking the least number of in game days. (very correlated with number
of actions you take.) Good Luck!\n---------------------------------\n''')


if __name__ == "__main__":
    Game()
