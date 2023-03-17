import random
from player import Player


class Game:
    def __init__(self, test=False, strength=1):
        if not test:
            name = input('Player\'s name -> ')
            difficulty = ""
            while difficulty not in ['1', '2', '3']:
                difficulty = input("Enter 1 for easy, 2 for medium, 3 for hard -> ")
            difficulty = int(difficulty)
        else:
            name = "TestPlayer"
            difficulty = strength
        self.player = Player(name, difficulty)
        #  TODO edit the distances to be a random thing

        # set up values for player

        self.play()

    def turn(self):
        print("---------------------------------")
        self.player.printInfo()
        self.player.printActions()
        print("---------------------------------")

        action = input("-> ")
        try:
            self.player.doAction(action)
        except KeyError:
            print("Invalid Action")

    def play(self):
        # TODO add a welcome message
        while self.player.traveled < self.player.distance:
            self.turn()

if __name__ == "__main__":
    Game()
