"""
GameManager.py

@author Andrew Fletcher
    Email: afletcher168@gmail.com
@since 08/16/2019

File that runs the game
"""

"""
The object for the game
"""

import Field
import Roster
import PlayCalling

class GameManager(object):

    """
    Constructor for the game manager
    @param load_file the file to try to load a game from
    @param save_file a file to save to
    @param diff the difficulty of the game
    """
    def __init__(self, load_file, save_file, diff):
        global field, player1_roster, player2_roster, save_file_name,difficulty
        field = Field.Field(load_file, save_file)
        player1_roster = Roster.Roster(load_file, "player1")
        player2_roster = Roster.Roster(load_file, "player2")
        save_file_name = save_file
        difficulty = diff


    """
    A help message for the user.
    """
    def help(self):
        print("This game is a type of play calling game.\n")
        print("The better the roster is suited for a play,\n")
        print("and the better the play matchup, the better the results.")

    
    """
    The method that plays (carries out) the game.
    """
    def play(self):
        print("Welcome to the game!")
        print(field)


        while True:   #add real conditions here
            if field.possession == "player1":
                print("PLAYER 1 calling OFFENSE:")
                print(field)
                PlayCalling.call_offensive_play(player1_roster)
                print("PLAYER 2 calling DEFENSE:")
                print(field)
                PlayCalling.call_defensive_play(player2_roster, player1_roster)
                print(field.snap(player1_roster,player2_roster))
            elif field.possession == "player2":
                print("PLAYER 2 calling OFFENSE:")
                print(field)
                PlayCalling.call_offensive_play(player2_roster)
                print("PLAYER 1 calling DEFENSE:")
                print(field)
                PlayCalling.call_defensive_play(player1_roster, player2_roster)
                print(field.snap(player2_roster,player1_roster))

