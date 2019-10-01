"""
Player.py

@author Andrew Fletcher
    Email: afletcher168@yahoo.com
@since 08/16/2019

The object class for a player that will be on the roster.
"""


class Player(object):

    """
    Constructor for the player class
    @param position the position that the player plays
    @param the speed of the player
    @param strength the strength of the player
    @param size the size of the player
    @param agility the agility of the player
    @param intelligence the intelligence of the player
    """
    def __init__(self, position, speed, strength, size, agility, intelligence):
        self.position = position
        self.speed = speed
        self.strength = strength
        self.size = size
        self.agility = agility
        self.intelligence = intelligence
        self.set_ratings()

    def __repr__(self):
        return (self.position)


    """
    Sets the rating of the player for particular actions based on base stats.
    """
    def set_ratings(self):
        #Offensive Ratings
        rating = (self.speed*0.5 + self.agility*0.2 
                  + self.size*0.2 + self.intelligence*0.1)
        self.qb_run = rating
        rating = (self.strength*0.6 + self.intelligence*0.4)
        self.deep_pass = rating
        rating = (self.strength*0.4 + self.intelligence*0.6)
        self.medium_pass = rating
        rating = (self.strength*0.2 + self.intelligence*0.8)
        self.short_pass = rating

        rating = (self.speed*0.8 + self.agility*0.1
                  + self.intelligence*0.1)
        self.speed_run = rating
        rating1 = (self.speed*0.2 + self.strength*0.1 + self.size*0.6
                   + self.agility*0.1)
        rating2 = (self.speed*0.3 + self.size*0.1 + self.agility*0.4
                   + self.intelligence*0.2)
        if rating1 > rating2:
            self.power_run = rating1
        else:
            self.power_run = rating2
        rating = (self.speed*0.5 + self.agility*0.2
                  + self.intelligence*0.3)
        self.outside_zone_run = rating
        rating = (self.speed*0.2 + self.agility*0.5 
                  + self.intelligence*0.3)
        self.inside_zone_run = rating

        rating = (self.speed*0.7 + self.agility*0.1 
                  + self.intelligence*0.2)
        self.speed_route = rating
        rating = (self.speed*0.3 + self.agility*0.4
                  + self.intelligence*0.3)
        self.quick_route = rating
        rating = (self.speed*0.1 + self.strength*0.2 + self.size*0.5
                  + self.intelligence*0.2)
        self.possession_route = rating
        self.best_route = max(self.speed_route, self.quick_route,
                            self.possession_route)  #best route run

        self.covered_rating = 0  #0 if no defender is assigned to them
        
        rating = (self.strength*0.2 + self.size*0.3 
                  + self.agility*0.2 + self.intelligence*0.3)
        self.pass_block = rating
        rating = (self.strength*0.5 + self.size*0.3
                  + self.intelligence*0.2)
        self.power_block = rating
        rating = (self.strength*0.2 + self.size*0.2 
                  + self.agility*0.3 + self.intelligence*0.3)
        self.pull_block = rating

        #Defensive Ratings
        rating1 = (self.strength*0.5 + self.size*0.4 + self.intelligence*0.1)
        rating2 = (self.speed*0.3 + self.strength*0.1 + self.size*0.1 
                    + self.agility*0.3 + self.intelligence*0.) 
        if rating1 > rating2:
            self.pass_rush = rating1
        else:
            self.pass_rush = rating2
        rating = (self.speed*0.3 + self.strength*0.1 + self.size* 0.1
                    + self.agility*0.3 + self.intelligence*0.2)
        self.one_gap = rating
        rating = (self.strength*0.4 + self.size*0.3 + self.intelligence*0.3)
        self.two_gap = rating

        rating = (self.speed*0.4 + self.size*0.3 + self.intelligence*0.3)
        self.stuff_run = rating
        rating = (self.speed*0.5 + self.agility*0.1 + self.intelligence*0.4)
        self.chase_run = rating

        rating = (self.speed*0.3 + self.agility*0.2 + self.intelligence*0.5)
        self.play_recognition = rating

        rating1 = (self.speed*0.4 + self.size*0.2 + self.agility*0.3
                    + self.intelligence*0.1)
        rating2 = (self.speed*0.2 + self.size*0.3 + self.agility*0.1
                    + self.intelligence*0.4)
        if rating1 > rating2:
            self.man_coverage = rating1
        else:
            self.man_coverage = rating2
        rating1 = (self.speed*0.4 + self.size*0.2 + + self.intelligence*0.4)
        rating2 = (self.speed*0.2 + self.size*0.4 + + self.intelligence*0.4)
        if rating1 > rating2:
            self.zone_coverage = rating1
        else:
            self.zone_coverage = rating2


