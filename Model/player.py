""" Player class. 
Used to store player informations.
Keep informations available for the User
"""

from collections import OrderedDict
from operator import getitem
from operator import itemgetter


class Player:
 
    def __init__(self, one_player_list):
        self.name = one_player_list["Player's family name:"]
        self.first_name = one_player_list["Player's first name:"]
        self.birth = one_player_list["Player's birthdate:"]
        self.gender = one_player_list["Player's gender:"]
        self.ranking = one_player_list["Player's rank:"]
        self.pairing_nb = one_player_list["Pairing number"]
        self.score = one_player_list["Score"]  
    
    def match_player(self):
        """Permet de garder les infos importantes d'un joueur pour un match"""
        match_player = [self.name+' '+self.first_name, self.score]
        return match_player
