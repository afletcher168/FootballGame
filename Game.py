"""
Game.py

@author Andrew Fletcher
    Email: afletcher168@gmail.com
@since 08/16/2019
Sources of Help:
    TBD

File for launching the game. Takes optional command line arguments.
"""

import sys
import GameManager


DEFAULT_SAVE_FILE = "game_save.db"
DEFUALT_DIFFICULTY = "normal"

help_message = ("The program can be run with the following option arguements:"
                "\n-h: prints this help message\n"
                "-i: specifies a file to be loaded\n"
                "-o: specifies a file for the game to save to\n"
                "-d: specifies a difficulty\n"
                "The arguments should be given in the format '-flag argument'")


"""
Processes the optional command line arguments.
@param the command line arguments
"""
def process_args(args):
    if ((len(args) % 2 != 1) and (len(args) != 0)):
        print(help_message)
        sys.exit()

    global load_file, save_file, difficuly

    load_file = ""
    save_file = DEFAULT_SAVE_FILE
    difficuly = DEFUALT_DIFFICULTY

    for i in range(1, len(args)-1, 2):
        if args[i] == "-h":
            print(help_message)
        elif args[i] == "-i":
            load_file = args[i+1]
        elif args[i] == "-o":
            save_file = args[i+1]
        elif args[i] == "-d":
            difficuly = args[i+1]
        else:
            print(help_message)


#try:
process_args(sys.argv)

print("Welcome to the game.")
    
game = GameManager.GameManager(load_file, save_file, difficuly)
game.play()

#except:
    #print(help_message)