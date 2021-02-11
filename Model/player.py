""" Player class. 
Used to store player informations.
Keep informations available for the User
"""

from collections import OrderedDict
from operator import getitem


class Player:
    def __init__(self, name, first_name, birthdate, gender, ranking, pairing_nb=None, score=0):
        self.name = name
        self.first_name = first_name
        self.birth_date = birthdate
        self.gender = gender
        self.ranking = ranking
        self.pairing_nb = pairing_nb
        self.score = score

    
class Players: 

    def dict_construction(self, joueur_1, joueur_2, joueur_3, joueur_4, joueur_5, joueur_6, joueur_7, joueur_8):
        players_dict = {}
        players_dict[1] = joueur_1
        players_dict[2] = joueur_2
        players_dict[3] = joueur_3
        players_dict[4] = joueur_4
        players_dict[5] = joueur_5
        players_dict[6] = joueur_6
        players_dict[7] = joueur_7
        players_dict[8] = joueur_8

        return players_dict


    def sorting(self, players_dict):

        sorted_players = OrderedDict(sorted(players_dict.items(),
                      key=lambda x: getitem(x[1], "Player's rank:"))
                     ) 
        print(sorted_players)
        return sorted_players  
