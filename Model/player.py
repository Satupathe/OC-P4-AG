""" Player class. 
Used to store player informations.
Keep informations available for the User
"""

from collections import OrderedDict
from operator import getitem
from operator import itemgetter


class Player:
    """def __init__(self, name, first_name, birthdate, gender, ranking, pairing_nb=None, score=0):
        self.name = name
        self.first_name = first_name
        self.birth_date = birthdate
        self.gender = gender
        self.ranking = ranking
        self.pairing_nb = pairing_nb
        self.score = score"""


    def __init__(self, one_player_list):
        self.name = one_player_list["Player's family name:"]
        self.first_name = one_player_list["Player's first name:"]
        self.birth = one_player_list["Player's birthdate:"]
        self.gender = one_player_list["Player's gender:"]
        self.ranking = one_player_list["Player's rank:"]
        self.pairing_nb = one_player_list["Pairing number"]
        self.score = one_player_list["Score"]  
    
    def match_player(self):
        match_player = [self.name+''+self.first_name, self.score]
        return match_player
