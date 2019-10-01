"""
Field.py

@author Andrew Fletcher
    Email: afletcher168@gmail.com
@since 09/05/2019

File for the field object that keeps track of down, distance, and possession,
in addition to running the play once the plays are called.
"""

import random
import copy
import sys

class Field(object):

    """
    Constructor for the field object. If no valid load file is given,
    defaults are assigned.
    @param load_file the file to load the save data from
    """
    def __init__(self, load_file, save_file):
        try:
            f = open(load_file)
            lines = f.readlines()
            self.possession = lines[0]
            self.time = int(lines[1])
            self.yard_line = int(lines[2])
            self.down = int(lines[3])
            self.distance = int(lines[4])
            self.player1_score = int(lines[5])
            self.player2_score = int(lines[6])
            f.close()
        except:
            self.possession = "player1"
            self.time = 3600
            self.yard_line = 25
            self.down = 1
            self.distance = 10
            self.player1_score = 0
            self.player2_score = 0
    
    def __repr__(self):
        if self.yard_line > 50:
            print("{} has the ball on their opponent's {:.1f} yard line."
                .format(self.possession, 100-self.yard_line))
        elif self.yard_line < 50:
            print("{} has the ball on their {:.1f} yard line.".format(
                self.possession, self.yard_line))
        else:
            print("{} has the ball at the 50 yard line.".format(
                self.possession))
        print("There is {:.0f}:{:.0f} left on the clock.".format(
            self.time//60, self.time%60))
        print("The score is player1: {} to player2: {}."
                .format(self.player1_score, self.player2_score))
        return("It is {} down, and {:.1f}".format(self.down, self.distance))

    """
    Runs the simulation for the play.
    @param offense the offense's roster
    @param defense the defense's roster
    """
    def snap(self, offense, defense):
        result = "snap"
        QB = copy.copy(offense.QB)
        risk_v_rewards = []
        if offense.play_type == "RUN":
            #check to see if RB makes it through line
            run_stop_multiplier = defense.vs_run/offense.RBlock
            print("RSM: {}".format(run_stop_multiplier))
            stop_value = run_stop_multiplier*random.random()*100
            print("STOP VALUE: {}".format(stop_value))
            if stop_value >= 80:
                yards = -2 + 4*random.random()
                self.update_field(yards)
                result = ("Run is stopped for {:.1f} yards.".format(yards))
                return result
            #check to see if RB makes it through second level
            run_stop_multiplier=defense.vs_run_second_level/offense.RB.speed/2
            print("RSM: {}".format(run_stop_multiplier))
            stop_value = run_stop_multiplier*random.random()*100
            print("STOP VALUE: {}".format(stop_value))
            if (stop_value >= 50):
                yards = 3 + 3*random.random()
                self.update_field(yards)
                result= ("Run is stopped in the second level for {:.1f} yards."
                        .format(yards))
                return result
            elif (stop_value >= 10):
                yards = 7 + 18*random.random()
                self.update_field(yards)
                result = ("Run breaks to third level for {:.1f} yards"
                        .format(yards))
                return result
            else:
                yards = 100-self.yard_line
                self.update_field(yards)
                result = ("Run breaks for a {:.1f} yard touchdown!"
                        .format(yards))
                return result

        elif offense.play_type == "PASS":
            #Check to see if rush gets there
            pass_rush_multiplier = defense.rush_vs_pass/offense.PBlock
            print("PASS_RUSH_MULTIPLIER: {}".format(pass_rush_multiplier))
            rush_value = pass_rush_multiplier*random.random()*100
            print("RUSH VALUE: {}".format(rush_value))
            if rush_value >= 60:
                yards = -10 + 8*random.random()
                self.update_field(yards)
                result = ("The QB is SACKED for {:.1f} yards.".format(yards))
                return result
            elif rush_value >= 40:
                print("The QB is PRESSURED...")
                QB.short_pass *= 0.8
                QB.medium_pass *= 0.8
                QB.deep_pass *= 0.8
                QB.intelligence *= 0.5
            #Check to see if/what receiver(s) are open
            for receiver in offense.eligibles:
                receiver.risk_factor = 1
                receiver.reward_factor = 0
                #Coverage from man
                if receiver.role == "SRR":
                    receiver.separation = receiver.speed_route/(
                                    1+receiver.covered_rating)
                elif receiver.role == "QRR":
                    receiver.separation = receiver.quick_route/(
                                    1+receiver.covered_rating)
                elif receiver.role == "PRR":
                    receiver.separation = receiver.possession_route/(
                                    1+receiver.covered_rating)
                elif receiver.role == "BRR":
                    receiver.separation = receiver.best_route/(
                                    1+receiver.covered_rating)
                else:
                    receiver.separation = 0
                    receiver.risk_v_reward = 0
                    continue

                #Coverage from zone
                if receiver.depth == "S":
                    receiver.separation /= (1 + defense.spacing["SZ"])
                    receiver.reward_factor = 5
                    receiver.risk_factor = 1
                    receiver.risk_factor *= QB.short_pass*0.01
                elif receiver.depth == "M":
                    receiver.separation /= (1 + defense.spacing["MZ"])
                    receiver.reward_factor = 10
                    receiver.risk_factor = 0.9
                    receiver.risk_factor *= QB.medium_pass*0.01
                elif receiver.depth == "D":
                    receiver.separation /= (1 + defense.spacing["DZ"])
                    receiver.reward_factor = 30
                    receiver.risk_factor = 0.8
                    receiver.risk_factor *= QB.deep_pass*0.01
                receiver.risk_factor *= receiver.separation
                receiver.risk_v_reward = (receiver.risk_factor *
                                            receiver.reward_factor)
                if receiver.risk_v_reward != 0:
                    risk_v_rewards.append(receiver)
            #Check to see if QB makes correct decision
            sorted(risk_v_rewards,key=lambda receiver : receiver.risk_v_reward)
            for i in range(0, len(risk_v_rewards)):
                read = random.random()*100
                if read <= QB.intelligence:
                    print("{}th best decision made!".format(i))
                    decision = risk_v_rewards[len(risk_v_rewards) -1 - i]
                    break
                if i == (len(risk_v_rewards)-1):
                    yards = -10 + 8*random.random()
                    self.update_field(yards)
                    result=("The QB is coverage SACKED for {:.1f} "
                            "yards.".format(yards))
                    return result
            #Check to see if pass is completed
            #0.5 is arbitrary base completion percentage
            print("RISK FACTOR: {}".format(decision.risk_factor))
            #completion chance is *8 to be more realistic
            completion_chance = 0.5 * decision.risk_factor * 8
            print("COMPLETION CHANCE: {}".format(completion_chance))
            reception = random.random()
            if reception > completion_chance:
                """
                #Interception
                is_interception = random.random()
                if is_interception >= 0.05:
                    result = ('{} pass to {} is INTERCEPTED!'
                        .format(receiver.depth, receiver))
                else: 
                """
                #Incompletion
                yards = 0
                self.update_field(yards)
                result = ("{} pass to {} resulted in an incompletion."
                        .format(receiver.depth, receiver))
                return result
            else:
                #Completion
                #Check air yards and YAC
                if decision.depth == "S":
                    air_yards = random.random()*5
                    #yac = random.random()*20
                    yac = 0  #yac disabled for now for simplicity
                elif decision.depth == "M":
                    air_yards = 5 + random.random()*15
                    #yac = random.random()*10
                    yac = 0  #yac disabled for now for simplicity
                elif decision.depth == "D":
                    air_yards = 20 + random.random()*30
                    #yac = random.random()*5
                    yac = 0  #yac disabled for now for simplicity
                else:
                    print("Whoops! Something went wrong!")
                
                if (air_yards + self.yard_line) >= 110:
                    result = ("{} pass to {} resulted in an incompletion"
                            "out the back of the endzone!"
                            .format(receiver.depth, receiver))
                    return result
                yards = air_yards + yac
                self.update_field(yards)
                result = ("{} pass to {} completed for {:.1f} yards"
                        .format(receiver.depth, receiver, yards))
                return result

    """
    Updates the field based on the result of the play.
    @yards The yards gained or lost on the play
    """
    def update_field(self, yards):
        self.yard_line += yards
        self.distance -= yards
        self.down += 1
        self.time -= 40
        if self.yard_line >= 100:  #Touchdown
            print("Touchdown!")
            self.down = 1
            self.distance = 10
            self.switch_possession()
        elif self.distance <= 0:    #First down
                print("First down!")
                self.down = 1
                if self.yard_line >= 90:
                    self.distance = 100-self.yard_line
                else:
                    self.distance = 10
        
        if self.down == 5:  #Turnover on downs
            print("Turnover on downs!")
            self.down = 1
            self.distance = 10
            self.switch_possession()
        if self.time <= 0:
            print("The game is over!")

    
    """
    Switches who has possession of the ball
    """
    def switch_possession(self):
        self.yard_line = 100 - self.yard_line
        if self.possession == "player1":
            self.possession = "player2"
        elif self.possession == "player2":
            self.possession = "player1"



    """
    Saves the current state of the field to the save file
    """
    def save_field(self):
        pass

