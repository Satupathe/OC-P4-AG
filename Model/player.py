""" Player class. 
Used to store player informations.
Keep informations available for the User
"""


class Player:
 
    def __init__(self, one_player_infos):
        self.name = one_player_infos["Player's family name:"]
        self.first_name = one_player_infos["Player's first name:"]
        self.birth = one_player_infos["Player's birthdate:"]
        self.gender = one_player_infos["Player's gender:"]
        self.ranking = one_player_infos["Player's rank:"]
        self.pairing_nb = one_player_infos["Pairing number"]
        self.score = one_player_infos["Score"]
        self.pairing_list = None  
        #attention au doublon de score avec match player
    
    def add ??
    
    def match_player(self):
        """Permet de garder les infos importantes d'un joueur pour un match"""
        match_player = [self, self.score]
        return match_player
        
        #une liste pour chaque joueur issu de self.pairing
        #créer une liste pour savoir qui a joué contre qui en fonction du rank
        #si liste vide, c'est le premier round



""" 
créer un tournoi
dans le tournoi créer un premier round


#pairing en fonction des rank et en vérifiant que les joueurs n'ont pas déjà joué ensemble
#fonction du model qui va appeler les instances de match et de joueur
#propose un match et vérifie les paring déjà effectués