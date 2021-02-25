""" Player class. 
Used to store player informations.
Keep informations available for the User
"""


class Player:
 
    def __init__(self, one_player_infos, i):
        self.name = one_player_infos["Player's family name:"]
        self.first_name = one_player_infos["Player's first name:"]
        self.birth = one_player_infos["Player's birthdate:"]
        self.gender = one_player_infos["Player's gender:"]
        self.ranking = one_player_infos["Player's rank:"]
        self.pairing_nb = one_player_infos["Pairing number"]
        self.score = one_player_infos["Score"]
        self.opponents = one_player_infos["Opponents"]
        self.ID = i+1 
        #attention au doublon de score avec match player

    
    def match_player(self):
        """Permet de garder les infos importantes d'un joueur pour un match"""
        match_player = [self.name +' '+self.first_name+' ID = '+str(self.ID), float(self.score)]
        return match_player #référence player est son ID (changer dans view ID = nom)
        
        #une liste pour chaque joueur issu de self.pairing
        #créer une liste pour savoir qui a joué contre qui en fonction du rank
        #si liste vide, c'est le premier round
 
#prévoir un id spécifique pour chaque joueur 1 à 8. 

