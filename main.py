import random
from player import Player


class Game:
    def __init__(self):
        name = input('Player\'s name -> ')
        difficulty = ""
        while difficulty not in ['1', '2', '3']:
            difficulty = input("Enter 1 for easy, 2 for medium, 3 for hard -> ")
        difficulty = int(difficulty)
        self.player = Player(name, difficulty)
        #  TODO edit the distances to be a random thing

        # set up values for player

        self.play()

    def turn(self):
        print("---------------------------------")
        print(f"Name: {self.player.name}")
        #TODO add things to check if time and distance can be shown
        print("Day: ")
        print("Distance: [XXXXXXX       ]")
        print(f"Energy: {self.player.energy}")
        print(f"Water: {self.player.water}")
        print()
        print("Actions: \nTravel (t), Bag(b), Hunt (h) Forage (f), Explore (e), Info (i)")
        print("Make Shelter (m), Sleep (s), Check structure (c), Start Fire (x)")  # TODO make temporary actions appear/disapear
        print("---------------------------------")

        action = input("-> ")
        try:
            self.player.actionMap[action]()
        except KeyError:
            print("Invalid Action")


    def play(self):
        # TODO add a welcome message
        while self.player.traveled < self.player.distance:
            self.turn()


Game()
