import pickle
import os

# Code inspired by https://java2blog.com/save-object-to-file-python/


def save(player):
    if os.path.isfile("playerFiles/" + player.name + "_Player_File.pkl"):
        print("There is a save file for this player already.")
        check = input("Do you still want to save? (enter y) -> ")
        if check != "y":
            print("The game wasn't saved.")
            return

    fileName = "playerFiles/" + player.name + "_Player_File.pkl"
    with open(fileName, 'wb') as file:
        pickle.dump(player, file)
        print(f"Game was saved! To start playing this game again, run python main.py {player.name}")
        print("Into your command line.")
        print(f"To delete this file you can run python main.py delete {player.name} into the command line.")
        exit(1)


def load(name):
    if os.path.isfile("playerFiles/" + name + "_Player_File.pkl"):
        return pickle.load(open("playerFiles/" + name + "_Player_File.pkl", "rb"))
    print("A player file with that name doesn't exist. Unable to start game.")
    exit(0)


def delete(name):
    fileName = "playerFiles/" + name + "_Player_File.pkl"
    if os.path.isfile(fileName):
        os.remove(fileName)
    else:
        print("The file does not exist, so nothing was deleted")

