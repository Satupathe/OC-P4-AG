""" Main file to launch every part of the MVC pattern"""

from Model import tournamentmodel
from View import view

from operator import itemgetter


class TournamentInput:

    def tournament_infos(self):
        """Appelle le module view et les input du tournoi"""
        
        """self.one_tournament_infos = view.TournamentView()
        self.one_tournament_infos.ask_tournament()
        print(self.one_tournament_infos)"""

        self.tournament_dict = {"Tournament's name:": 'Expert',
                           "Tournament's adress:": 'Chassieu',
                           "Tournament's Date:": 'Janvier',
                           "Total number of rounds:": 4,
                           "Time control:": '300',
                           "Number of player:": 8,
                           "players:" ''
                           "Comments:": 'Dictionnaire temporaire'
                          } #tournoi factice comme raccourci

        
        
        """return self.one_tournament_infos"""
        return self.tournament_dict

class PlayersInput:

    def players_infos(self):
        """Appelle le module view et les input joueurs"""


        """self.players_infos = view.PlayersView() 
        self.players_infos.ask_players()"""
        
        self.players_infos = [{"Player's family name:": 'Dupont', "Player's first name:": 'Alexandre', "Player's birthdate:": '1972', "Player's gender:": 'M', "Player's rank:": 1, "Pairing number": '', "Score": 0},
                        {"Player's family name:": 'Durand', "Player's first name:": 'Aurelie', "Player's birthdate:": '1990', "Player's gender:": 'F', "Player's rank:": 4, "Pairing number": '', "Score": 0},
                        {"Player's family name:": 'Dupuis', "Player's first name:": 'Monique', "Player's birthdate:": '1965', "Player's gender:": 'F', "Player's rank:": 6, "Pairing number": '', "Score": 0},
                        {"Player's family name:": 'Bepas', "Player's first name:": 'Marion', "Player's birthdate:": '1987', "Player's gender:": 'F', "Player's rank:": 7, "Pairing number": '', "Score": 0},
                        {"Player's family name:": 'Menant', "Player's first name:": 'laureen', "Player's birthdate:": '1994', "Player's gender:": 'F', "Player's rank:": 3, "Pairing number": '', "Score": 0},
                        {"Player's family name:": 'Liotard', "Player's first name:": 'David', "Player's birthdate:": '1974', "Player's gender:": 'X', "Player's rank:": 2, "Pairing number": '', "Score": 0},
                        {"Player's family name:": 'Roux', "Player's first name:": 'Cedric', "Player's birthdate:": '1979', "Player's gender:": 'M', "Player's rank:": 5, "Pairing number": '', "Score": 0},
                        {"Player's family name:": 'Gagnieu', "Player's first name:": 'Arnaud', "Player's birthdate:": '1991', "Player's gender:": 'M', "Player's rank:": 8, "Pairing number": '', "Score": 0}
                       ]#liste des joueurs factice comme raccourci

        """print(self.players_infos)
        return self.players_infos"""

        return self.players_infos

    def sorted_rank(self):
        """remet la liste des joueur dans l'ordre des ranks"""

        self.sorted_players = sorted(self.players_infos, key=itemgetter("Player's rank:")) 

        return self.sorted_players  
