"""
PlayCalling.py

@author Andrew Fletcher
    Email: afletcher168@gmail.com
@since 08/18/2019

File that contains and handles the playcalls for offense and defense
"""

import sys

# {play call : [QB,RB,WR1,WR2,WR3,TE1,OL1,OL2,OL3,OL4,OL5,WR4,TE2,TE3,FB]}

# 0 = do nothing, not counted towards rating

# QBR = qb run
# SP = short pass
# MP = medium pass
# DP = deep pass

# SR = speed run
# PR = power run
# OZR = outside zone run
# IZR = inside zone run

# SRR = speed route running
# QRR = quick route running
# PRR = possession route running

# PAB = pass block
# POB = power block
# PUB = pull block

offensive_playbook = {
    "SR" : [[0, "SR", "POB", "POB", 0, "POB", "POB", "POB", "POB", "POB", 0, 0, "POB", "POB", "POB"],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
    "PR" : [[0, "PR", 0, 0, 0, "POB", "POB", "POB", "POB", "POB", "POB", 0, "POB", "POB", "POB"],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
    "OZR": [[0, "OZR", "PUB", "PUB", 0, "PUB", "PUB", "PUB", "PUB", 0, "PUB", 0, "PUB", "PUB", "PUB"],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
    "IZR": [[0, "IZR", 0, 0, 0, "PUB", "PUB", "PUB", "PUB", "PUB", "PUB", 0, "PUB", "PUB", "PUB"],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
    "slants-flats":[["SP","PAB","QRR","SRR","SRR","PRR","PAB","PAB","PAB","PAB","PAB","SRR","PRR","PRR","SRR"],
                    [ 0  ,  0  , "M" , "M" , "S" , "S" ,  0  ,  0  ,  0  ,  0  ,  0  , "S" , "S" , "S" , "S"]],
    "curls":[["SP","PAB","BRR","BRR","BRR","BRR","PAB","PAB","PAB","PAB","PAB","BRR","BRR","PAB","PAB"],
             [ 0  ,  0  , "M" , "M" , "M" , "M" ,  0  ,  0  ,  0  ,  0  ,  0  , "M" , "M" ,  0  ,  0]],
    "verticals":[["DP","PAB","SRR","SRR","SRR","SRR","PAB","PAB","PAB","PAB","PAB","SRR","SRR","SRR","PAB"],
                 [ 0  ,  0  , "D" , "D" , "D" , "D" ,  0  ,  0  ,  0  ,  0  ,  0  , "D" , "D" , "D" ,  0]],
}


"""
The function for playcalling for the offense
@param roster the roster of the team that is calling the play
@return [play, rating]
"""
def call_offensive_play(roster):
    actives = [1]*15
    while True:
        print("What personnel would you like to use?")
        user_input = input()
        if((user_input.lower() == 'q') or (user_input.lower() == "quit")):
            #save and exit
            sys.exit()
        elif ((user_input.lower() == 'h') or (user_input.lower() == "help")):
            print("Please input personnel in the numbering system.")
            print("For instance:\n")
            print("1RB/1TE/(3WR) = 11 personnel")
            print("2RB/1TE/(2WR) = 21")
            print("1RB/2TE/(2WR) = 12")
            print("Max number of RBs is 2, max number of TE is 3, max WR is 4")
            print("press 'q' or 'quit' to quit.")
        elif(user_input == "11"):
            actives[11] = 0
            actives[12] = 0
            actives[13] = 0
            actives[14] = 0
            while True:
                print("Run or Pass?")
                user_input = input()
                if((user_input.lower() == 'q')or(user_input.lower()=="quit")):
                    #save and exit()
                    sys.exit()
                elif((user_input.lower()=='b')or(user_input.lower()=="back")):
                    actives[11] = 1
                    actives[12] = 1
                    actives[13] = 1
                    actives[14] = 1
                    break
                elif((user_input.lower()=='r')or(user_input.lower()=="run")):
                    play = call_run_play(roster, actives)
                    if play == "back":
                        continue
                    else:
                        return play
                elif((user_input.lower()=='p')or(user_input.lower()=="pass")):
                    play = call_pass_play(roster, actives)
                    if play == "back":
                        continue
                    else:
                        return play
                else:
                    print("Input 'r' or 'run' to select run plays.")
                    print("Input 'p' or 'pass' to select pass plays.")
                    print("Input 'q' or 'quit' to quit.")
                    print("Input 'b' or 'back' to go back.")
        elif(user_input == "03"):
            pass
        elif(user_input == "13"):
            pass
        elif(user_input == "23"):
            pass
        elif(user_input == "02"):
            pass
        elif(user_input == "12"):
            pass
        elif(user_input == "22"):
            pass
        elif(user_input == "01"):
            pass
        elif(user_input == "21"):
            pass
        elif(user_input == "10"):
            pass
        elif(user_input == "20"):
            pass
        else:
            print("Please input a proper personnel grouping.")
            print("input 'h' or 'help' for more information.")


"""
The function for calling a run play.
"""
def call_run_play(roster, actives):
    roster.play_type = "RUN"
    actives[0] = 0
    while True:
        print("Zone or traditional blocking?")
        user_input = input()
        if((user_input.lower() == 'q') or (user_input.lower() == "quit")):
            #save and exit()
            sys.exit()
        elif((user_input.lower() == 'b') or (user_input.lower() == "back")):
            return "back"
        elif((user_input.lower() == 'z') or (user_input.lower() == "zone")):
            while True:
                print("Select a play:")
                print("Outside Zone Run: (%.2f)"
                    % (roster.calculate_offensive_rating(
                        offensive_playbook["OZR"], actives)))
                print("Inside Zone Run: (%.2f)"
                    % (roster.calculate_offensive_rating(
                        offensive_playbook["IZR"], actives)))
                user_input = input()
                if((user_input.lower()=='q')or(user_input.lower()=="quit")):
                    #save and exit()
                    sys.exit()
                elif((user_input.lower()=='b')or(user_input.lower()=="back")):
                        break
                elif(user_input.lower() == 'ozr' or
                    (user_input.lower() == 'outside zone run')):
                    return 'OZR'
                elif(user_input.lower() == 'izr' or
                    (user_input.lower() == 'inside zone run')):
                    return 'IZR'
                else:
                    print("Please select one of the plays.")
                    print("To go back or quit, 'b' or 'q'.")
        elif((user_input.lower()=='t')or(user_input.lower()=="traditional")):
            while True:
                print("Select a play:")
                print("Speed Run: (%.2f)" % (roster.calculate_offensive_rating(
                          offensive_playbook["SR"], actives)))
                print("Power Run: (%.2f)" % (roster.calculate_offensive_rating(
                          offensive_playbook["PR"], actives)))
                user_input = input()
                if((user_input.lower()=='q')or(user_input.lower()=="quit")):
                    #save and exit()
                    sys.exit()
                elif((user_input.lower() == 'b') or
                      (user_input.lower() == "back")):
                    break
                elif(user_input.lower() == 's' or
                      (user_input.lower() == 'speed run')):
                    return 'SR'
                elif(user_input.lower() == 'p' or
                         (user_input.lower() == 'power run')):
                    return 'PR'
                else:
                    print("Please select one of the plays.")
                    print("To go back or quit, 'b' or 'q'.")
        else:
            print("Zone blocking relies more on agility/intel")
            print("Traditional relies more on strength/size.")


"""
The function for calling a pass play.
@param roster the offense's roster
@param actives the personnel that are active on the play
@return the playcall
"""
def call_pass_play(roster, actives):
    roster.play_type = "PASS"
    while True:
        print("Would you like to call a preset play?")
        user_input = input()
        if((user_input.lower() == 'q') or (user_input.lower() == "quit")):
            #save and exit()
            sys.exit()
        elif((user_input.lower() == 'b') or (user_input.lower() == "back")):
            return "back"
        elif((user_input.lower() == 'y') or (user_input.lower() == "yes")):
            while True:
                print("Select a play:")
                print("Slants-Flats: (%.2f)" % 
                          (roster.calculate_offensive_rating(
                          offensive_playbook["slants-flats"], actives)))
                print("Curls: (%.2f)" % (roster.calculate_offensive_rating(
                          offensive_playbook["curls"], actives)))
                print("Verticals: (%.2f)"%(roster.calculate_offensive_rating(
                          offensive_playbook["verticals"], actives)))
                user_input = input()
                if((user_input.lower()=='q')or(user_input.lower()=="quit")):
                    #save and exit()
                    sys.exit()
                elif((user_input.lower() == 'b') or
                      (user_input.lower() == "back")):
                    break
                elif(user_input.lower() == 'sf' or
                      (user_input.lower() == 'slants-flats')):
                    roster.calculate_offensive_rating(
                        offensive_playbook["slants-flats"], actives)
                    return 'slants-flats'
                elif(user_input.lower() == 'c' or
                         (user_input.lower() == 'curls')):
                    roster.calculate_offensive_rating(
                        offensive_playbook["curls"], actives)
                    return 'curls'
                elif(user_input.lower() == 'v' or
                         (user_input.lower() == 'verticals')):
                    roster.calculate_offensive_rating(
                        offensive_playbook["verticals"], actives)
                    return 'verticals'
                else:
                    print("Please select one of the plays.")
                    print("To go back or quit, 'b' or 'q'.")
        elif((user_input.lower() == 'n') or (user_input.lower() == "no")):
            create_offensive_play(roster, actives)


"""
Player manually creates an offensive play to be added to the offensive playbook
@param roster the offense's roster
@param actives the active players on the roster
@return the playcall
"""
def create_offensive_play(roster, actives):
    pass


# {play call : [DL1,DL2,DL3,DL4,LB1,LB2,LB3,CB1,CB2,SS,FS,LB4,DB5]}

# 0 = do nothing, not counted towards rating

# PR = pass rush
# 1G = one gap responsibility
# 2G = two gap responsibility
# SR = stuff run

# MC = man coverage
# SZ = short zone
# MZ = mid zone
# DZ = deep zone

defensive_playbook = {
    "COV1" : ["PR","PR","PR","PR","MZ","MC","MC","MC","MC","MC","DZ","PR","MC"],
    "COV2M": ["PR","PR","PR","PR","MC","MC","MC","MC","MC","DZ","DZ","PR","MC"],
    "COV2Z": ["PR","PR","PR","PR","MZ","MZ","MZ","SZ","SZ","DZ","DZ","PR","MZ"],
    "COV3" : ["PR","PR","PR","PR","MZ","MZ","MZ","DZ","DZ","MZ","DZ","PR","MZ"],
}


"""
The function for playcalling for the defense
@param roster the roster that includes the defensive players
@param offense the roster that includes the opposing offense's players
"""
def call_defensive_play(roster, offense):
    actives = [1]*13
    while True:
        print("What personnel would you like to use?")
        user_input = input()
        if((user_input.lower() == 'q') or (user_input.lower() == "quit")):
            #save and exit
            sys.exit()
        elif ((user_input.lower() == 'h') or (user_input.lower() == "help")):
            print("Please input the personnel name that is most common.")
            print("For instance:\n")
            print("3DL/4LB/(4DB) = 3-4 personnel")
            print("4DL/3LB/(4DB) = 4-3")
            print("4DL/2LB/(5DB) = nickel")
            print("Max number of DL is 4, max number of LB is 4, max DB is 5")
            print("press 'q' or 'quit' to quit.")
        elif(user_input == "4-3"):
            actives[11] = 0
            actives[12] = 0
            gap_roles = ["1G","1G","1G","1G","SR","SR","SR",0,0,0,0,0,0]
            while True:
                print("would you like to call a preset play?")
                user_input = input()
                if((user_input.lower() == 'q')or(user_input.lower()=="quit")):
                    #save and exit()
                    sys.exit()
                elif((user_input.lower()=='b')or(user_input.lower()=="back")):
                    actives[11] = 1
                    actives[12] = 1
                    break
                elif((user_input.lower()=='y')or(user_input.lower()=="yes")):
                    return pick_defensive_play(roster, gap_roles, actives,
                                                                    offense)
                elif((user_input.lower()=='n')or(user_input.lower()=="no")):
                    return create_defensive_play(roster, actives)
                else:
                    print("Input 'q' or 'quit' to quit.")
                    print("Input 'b' or 'back' to go back.")
        elif(user_input == "3-4"):
            actives[3] = 0
            actives[12] = 0
            gap_roles = ["2G","2G","2G",0,0,0,0,0,0,0,0,0,0]
            while True:
                print("would you like to call a preset play?")
                user_input = input()
                if((user_input.lower() == 'q')or(user_input.lower()=="quit")):
                    #save and exit()
                    sys.exit()
                elif((user_input.lower()=='b')or(user_input.lower()=="back")):
                    actives[3] = 1
                    actives[12] = 1
                    break
                elif((user_input.lower()=='y')or(user_input.lower()=="yes")):
                    return pick_defensive_play(roster, gap_roles, actives,
                                                                    offense)
                elif((user_input.lower()=='n')or(user_input.lower()=="no")):
                    return create_defensive_play(roster, actives)
                else:
                    print("Input 'q' or 'quit' to quit.")
                    print("Input 'b' or 'back' to go back.")
        elif(user_input == "nickel"):
            actives[3] = 0
            actives[11] = 0
            gap_roles = ["1G","1G","1G","1G","SR","SR","SR",0,0,0,0,0,0]
            while True:
                print("would you like to call a preset play?")
                user_input = input()
                if((user_input.lower() == 'q')or(user_input.lower()=="quit")):
                    #save and exit()
                    sys.exit()
                elif((user_input.lower()=='b')or(user_input.lower()=="back")):
                    actives[3] = 1
                    actives[12] = 1
                    break
                elif((user_input.lower()=='y')or(user_input.lower()=="yes")):
                    return pick_defensive_play(roster, gap_roles, actives, 
                                                                    offense)
                elif((user_input.lower()=='n')or(user_input.lower()=="no")):
                    return create_defensive_play(roster, actives)
                else:
                    print("Input 'q' or 'quit' to quit.")
                    print("Input 'b' or 'back' to go back.")
        else:
            print("Please input a proper personnel grouping.")
            print("input 'h' or 'help' for more information.")


"""
Function to pick a defensive play from a preset playbook
"""
def pick_defensive_play(roster, gap_roles, actives, offense):
    while True:
        roles = [[],[]]
        print("Select a play:")
        roles[1] = gap_roles
        roles[0] = defensive_playbook["COV1"]
        print("cover 1: (%.2f)" % 
                (roster.calculate_defensive_rating(roles, actives, offense)))
        roles[0] = defensive_playbook["COV2M"]
        print("cover 2-man: (%.2f)" %
                (roster.calculate_defensive_rating(roles, actives, offense)))
        roles[0] = defensive_playbook["COV2Z"]
        print("cover 2-zone: (%.2f)" %
                (roster.calculate_defensive_rating(roles, actives, offense)))
        roles[0] = defensive_playbook["COV3"]
        print("cover 3: (%.2f)" %
                (roster.calculate_defensive_rating(roles, actives, offense)))
        user_input = input()
        if((user_input.lower()=='q')or(user_input.lower()=="quit")):
            #save and exit()
            sys.exit()
        elif((user_input.lower() == 'b') or (user_input.lower() == "back")):
            break
        elif((user_input.lower()=='cov1') or (user_input.lower()=='cover 1')
              or user_input.lower()=='1'):
            roles[0] = defensive_playbook["COV1"]
            roster.calculate_defensive_rating(roles, actives, offense)
            return 'COV1'
        elif((user_input.lower()=='cov2m') or
            (user_input.lower()=='cover 2-man')or(user_input.lower()=="2m")):
            roles[0] = defensive_playbook["COV2M"]
            roster.calculate_defensive_rating(roles, actives, offense)
            return 'COV2M'
        elif((user_input.lower()=='cov2z') or
            (user_input.lower()=='cover 2-zone')or(user_input.lower()=="2z")):
            roles[0] = defensive_playbook["COV2Z"]
            roster.calculate_defensive_rating(roles, actives, offense)
            return 'COV2Z'
        elif((user_input.lower()=='cov3')or(user_input.lower()=='cover 3')
            or(user_input.lower() == "3")):
            roles[0] = defensive_playbook["COV3"]
            roster.calculate_defensive_rating(roles, actives, offense)
            return 'COV3'
        else:
            print("Please select one of the plays.")
            print("To go back or quit, 'b' or 'q'.")


"""
Create a defensive play
"""
def create_defensive_play(roster, actives):
    pass