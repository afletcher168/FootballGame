"""
Roster.py

@author Andrew Fletcher
    Email: afletcher168@gmail.com
@since 08/16/2019

The object class for a 30 man roster.
"""
import Player

class Roster(object):

    def __init__(self, load_file, team):
        global roster
        roster = []
        try:
            f = open(load_file, "r")
            lines = f.readlines()
            line_number = 0
            counter = 0
            for line in lines:
                if ((team == "player") or (team == "player1")):
                    if 7  <= line_number < 37:
                        stats = line.split()
                        roster[counter] = Player.Player(stats[0], stats[1], 
                                        stats[2], stats[3], stats[4], stats[5])
                        counter += 1
                if ((team == "cpu") or (team == "player2")):
                    if 38 <= line_number < 67:
                        stats = line.split()
                        roster[counter] = Player.Player(stats[0], stats[1], 
                                        stats[2], stats[3], stats[4], stats[5])
                        counter += 1
                line_number += 1
            f.close()
        except:
            print("No valid load file given.")
            #Player(speed, strength, size, agility, intelligence)
            #All players are set to low defaults
            #15 Offensive players
            roster.append(Player.Player("QB", 40, 70, 60, 40, 70))   #QB
            roster.append(Player.Player("RB", 70, 40, 40, 70, 50))   #RB
            roster.append(Player.Player("WR", 70, 40, 70, 60, 60))   #WR1
            roster.append(Player.Player("WR", 70, 40, 60, 50, 40))   #WR2
            roster.append(Player.Player("WR", 50, 40, 40, 60, 60))   #WR3
            roster.append(Player.Player("TE", 50, 60, 60, 50, 50))   #TE1
            roster.append(Player.Player("OL", 40, 70, 70, 50, 50))   #OL1
            roster.append(Player.Player("OL", 40, 60, 70, 50, 50))   #OL2
            roster.append(Player.Player("OL", 40, 50, 50, 70, 60))   #OL3
            roster.append(Player.Player("OL", 40, 50, 60, 60, 50))   #OL4
            roster.append(Player.Player("OL", 40, 50, 50, 60, 50))   #OL5
            roster.append(Player.Player("WR", 50, 40, 40, 50, 40))   #WR4
            roster.append(Player.Player("TE", 40, 60, 60, 40, 50))   #TE2
            roster.append(Player.Player("TE", 50, 40, 40, 50, 50))   #TE3
            roster.append(Player.Player("FB", 50, 40, 50, 50, 60))   #FB

            #13 Defensive players
            roster.append(Player.Player("DL", 50, 70, 60, 60, 50))  #DL1
            roster.append(Player.Player("DL", 60, 40, 60, 60, 50))  #DL2
            roster.append(Player.Player("DL", 40, 70, 50, 50, 50))  #DL3
            roster.append(Player.Player("DL", 40, 60, 60, 60, 40))  #DL4
            roster.append(Player.Player("LB", 60, 60, 50, 60, 70))  #LB1
            roster.append(Player.Player("LB", 60, 50, 50, 60, 50))  #LB2
            roster.append(Player.Player("LB", 50, 60, 60, 50, 50))  #LB3
            roster.append(Player.Player("CB", 70, 40, 40, 70, 60))  #CB1
            roster.append(Player.Player("CB", 60, 40, 40, 60, 60))  #CB2
            roster.append(Player.Player("S", 60, 60, 60, 60, 60))  #SS
            roster.append(Player.Player("S", 70, 50, 50, 60, 70))  #FS
            roster.append(Player.Player("LB", 50, 50, 50, 40, 50))  #LB4
            roster.append(Player.Player("DB", 60, 40, 40, 50, 50))  #DB5

            #2 Special teams players
            roster.append(Player.Player("K", 40, 60, 40, 50, 70))  #K
            roster.append(Player.Player("P", 40, 70, 40, 40, 60))  #P

        self.QB = roster[0]
        self.RB = roster[1]
        self.WR1 = roster[2]
        self.WR2 = roster[3]
        self.WR3 = roster[4]
        self.TE1 = roster[5]
        self.OL1 = roster[6]
        self.OL2 = roster[7]
        self.OL3 = roster[8]
        self.OL4 = roster[9]
        self.OL5 = roster[10]
        self.WR4 = roster[11]
        self.TE2 = roster[12]
        self.TE3 = roster[13]
        self.FB = roster[14]
        self.DL1 = roster[15]
        self.DL2 = roster[16]
        self.DL3 = roster[17]
        self.DL4 = roster[18]
        self.LB1 = roster[19]
        self.LB2 = roster[20]
        self.LB3 = roster[21]
        self.CB1 = roster[22]
        self.CB2 = roster[23]
        self.SS = roster[24]
        self.FS = roster[25]
        self.LB4 = roster[26]
        self.DB5 = roster[27]
        self.K = roster[28]
        self.P = roster[29]
        self.roster = roster


    """
    Calculates the offensive rating for the offense based on each player's     
    roles and how good they are at them. (for a given play)
    @param roles an array transferring the information of each player's role
    @param actives an array transferring the information of active player's
    @return the offense's rating for the play
    """
    def calculate_offensive_rating(self, roles, actives):
        self.offense_11 = []
        self.eligibles = []
        for i in range(len(actives)):
            if actives[i] == 1:
                roster[i].role = roles[0][i]
                roster[i].depth = roles[1][i]
                self.offense_11.append(roster[i])
                if ((roster[i].position == "WR") or 
                    (roster[i].position == "TE") or 
                    (roster[i].position == "RB") or 
                    (roster[i].position == "FB")):
                    self.eligibles.append(roster[i])
        self.roles = roles[0]
        self.depth = roles[1]

        total = 0
        self.PBlock = 0   #Pass block
        self.RBlock = 0   #Run block
        num_of_actives = 0
        counter = 0
        for player in self.offense_11:
            if roles[0][counter] != 0:
                num_of_actives += 1
                if roles[0][counter] == "QBR":
                    total += player.qb_run
                elif roles[0][counter] == "SP":
                    total += player.short_pass
                elif roles[0][counter] == "MP":
                    total += player.medium_pass
                elif roles[0][counter] == "DP":
                    total += player.deep_pass

                elif roles[0][counter] == "SR":
                    total += player.speed_run
                elif roles[0][counter] == "PR":
                    total += player.power_run
                elif roles[0][counter] == "OZR":
                    total += player.outside_zone_run
                elif roles[0][counter] == "IZR":
                    total += player.inside_zone_run

                elif roles[0][counter] == "SRR":
                    total += player.speed_route
                elif roles[0][counter] == "QRR":
                    total += player.quick_route
                elif roles[0][counter] == "PRR":
                    total += player.possession_route
                elif roles[0][counter] == "BRR":
                    total += player.best_route

                elif roles[0][counter] == "PAB":
                    total += player.pass_block
                    self.PBlock += player.pass_block
                elif roles[0][counter] == "POB":
                    total += player.power_block
                    self.RBlock += player.power_block
                elif roles[0][counter] == "PUB":
                    total += player.pull_block
                    self.RBlock += player.pull_block
            counter += 1

        rating = total/num_of_actives
        self.offensive_rating = rating
        return rating

    """
    Calculates the offensive rating for the offense based on each player's     
    roles and how good they are at them. (for a given play)
    @param roles an array transferring the information of each player's role
    @param actives an array transferring the information of active player's
    @return the offense's rating for the play
    """
    def calculate_defensive_rating(self, roles, actives, offense):
        ##LOTS OF PROBLEMS HERE
        self.defense_11 = []
        for i in range(0,len(actives)):
            if actives[i] == 1:
                self.defense_11.append(roster[i+15])
        self.roles = roles

        self.spacing = {"SZ":0, "MZ":0, "DZ":0}
        vs_run_total = 0
        vs_pass_total = 0
        self.vs_run = 0
        self.vs_run_second_level =  0
        self.rush_vs_pass = 0
        self.cov_vs_pass = 0
        self.cov_short = 0
        self.cov_mid = 0
        self.cov_deep = 0
        #roles vs pass
        counter = 0
        for player in self.defense_11:
            if roles[0][counter] != 0:
                if roles[0][counter] == "PR":
                    if roles[1][counter] == "2G":
                        vs_pass_total += (player.pass_rush 
                            * player.play_recognition)
                        self.rush_vs_pass += (player.pass_rush 
                            * player.play_recognition)
                    else:
                        vs_pass_total += player.pass_rush
                        self.rush_vs_pass += player.pass_rush
                elif roles[0][counter] == "MC":
                    if ((roles[1][counter]=="2G") or (roles[1][counter]=="1G")
                        or (roles[1][counter] == "SR")):
                        #Assigning man coverage
                        biggest_mismatch = 0
                        index = 0
                        man_counter = 0
                        for receiver in offense.eligibles:
                            matchup = receiver.best_route/(
                                        .1+receiver.covered_rating)
                            if matchup > biggest_mismatch:
                                biggest_mismatch = matchup
                                index = man_counter
                            man_counter += 1
                        offense.eligibles[index].covered_rating += (
                            player.man_coverage*
                            player.play_recognition*0.01)

                        vs_pass_total += (player.man_coverage
                            * (player.play_recognition*0.01))
                        self.cov_vs_pass += (player.man_coverage
                            * (player.play_recognition*0.01))
                    else:
                        #Assigning man coverage
                        biggest_mismatch = 0
                        index = 0
                        man_counter = 0
                        for receiver in offense.eligibles:
                            matchup = receiver.best_route/(
                                        .1+receiver.covered_rating)
                            if matchup > biggest_mismatch:
                                biggest_mismatch = matchup
                                index = man_counter
                            man_counter += 1
                        offense.eligibles[index].covered_rating += (
                                        player.man_coverage)

                        vs_pass_total += player.man_coverage
                        self.cov_vs_pass += player.man_coverage
                elif roles[0][counter] == "SZ":
                    self.spacing["SZ"] += 1
                    if ((roles[1][counter]=="2G") or (roles[1][counter]=="1G")
                        or (roles[1][counter] == "RS")):
                        vs_pass_total += (player.zone_coverage
                            * (player.play_recognition*0.01))
                        self.cov_vs_pass += (player.zone_coverage
                            * (player.play_recognition*0.01))
                        self.cov_short += (player.zone_coverage
                            * (player.play_recognition*0.01))
                    else:
                        vs_pass_total += player.zone_coverage
                        self.cov_vs_pass += player.zone_coverage
                        self.cov_short += player.zone_coverage
                elif roles[0][counter] == "MZ":
                    self.spacing["MZ"] += 1
                    if ((roles[1][counter]=="2G") or (roles[1][counter]=="1G")
                        or (roles[1][counter] == "RS")):
                        vs_pass_total += (player.zone_coverage
                            * (player.play_recognition*0.01))
                        self.cov_vs_pass += (player.zone_coverage
                            * (player.play_recognition*0.01))
                        self.cov_mid += (player.zone_coverage
                            * (player.play_recognition*0.01))
                    else:
                        vs_pass_total += player.zone_coverage
                        self.cov_vs_pass += player.zone_coverage
                        self.cov_mid += player.zone_coverage
                elif roles[0][counter] == "DZ":
                    self.spacing["DZ"] += 1
                    if ((roles[1][counter]=="2G") or (roles[1][counter]=="1G")
                        or (roles[1][counter] == "RS")):
                        vs_pass_total += (player.zone_coverage
                            * (player.play_recognition*0.01))
                        self.cov_vs_pass += (player.zone_coverage
                            * (player.play_recognition*0.01))
                        self.cov_deep += (player.zone_coverage
                            * (player.play_recognition*0.01))
                    else:
                        vs_pass_total += player.zone_coverage
                        self.cov_vs_pass += player.zone_coverage
                        self.cov_deep += player.zone_coverage
            counter += 1

        gaps_filled = 0
        #roles vs run
        counter = 0
        for player in self.defense_11:
            if ((roles[1][counter] == "1G") or (roles[1][counter] == "SR")):
                vs_run_total += player.one_gap
                self.vs_run += player.one_gap
                gaps_filled += 1
            elif roles[1][counter] == "2G":
                vs_run_total += player.two_gap
                self.vs_run += player.two_gap
                gaps_filled += 2
            elif roles[1][counter] == "RS":
                vs_run_total += player.stuff_run
                self.vs_run += player.stuff_run
                gaps_filled += 1
            elif (((roles[0][counter] == "SZ")or(roles[0][counter] == "MZ")
                    or(roles[0][counter]=="MC")) and (player.position=="S")):
                self.vs_run += player.stuff_run
                gaps_filled += 1
            elif player.position == "S":
                self.vs_run_second_level += player.chase_run
            elif player.position == "CB":
                self.vs_run_second_level += player.chase_run*0.5
            counter += 1

        vs_run_total *= (1 - (6-gaps_filled)*0.2)

        vs_pass_rating = vs_pass_total/11  #11 = number of defenders on field
        vs_run_rating = vs_run_total/11
        rating = (vs_pass_rating + vs_run_rating)/2  #the average
        self.defensive_rating = rating
        return rating





        
        







