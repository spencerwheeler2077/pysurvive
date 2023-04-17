import pickle
import os

# Code inspired by https://java2blog.com/save-object-to-file-python/

def save(player):
    if os.path.isfile("playerFiles/" + player.name + "_Player_File.pkl"):
        print("There is a save file for this player already. Unable to save")
    # TODO Make it so that a save with the same name just overwrites old file. (after checking that's okay to do so)

    fileName = "playerFiles/" + player.name + "_Player_File.pkl"
    with open(fileName, 'wb') as file:
        pickle.dump(player, file)
        print(f"Game was saved! To start playing this game again, run python main.py {player.name}")
        print("Into your command line.")
        exit(1)


def load(name):
    if os.path.isfile("playerFiles/" + name + "_Player_File.pkl"):
        return pickle.load(open("playerFiles/" + name + "_Player_File.pkl", "rb"))
    print("A player file with that name doesn't exist. Unable to start game.")
    exit(0)

