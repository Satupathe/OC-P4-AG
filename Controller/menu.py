""" Main file to launch every part of the MVC pattern"""

from Model import tournamentmodel
from View import view

from operator import itemgetter


class TournamentInput:

    def tournament_infos(self):
        """Appelle le module view et les input du tournoi"""
        
        """tournament_input = view.TournamentView()
        tournament = tournament_input.ask_tournament()"""
        
        
        tournament = {"Tournament's name:": 'essai',
                      "Tournament's adress:": 'Chassieu',
                      "Tournament's Date:": 'Janvier',
                      "Total number of rounds:": 4,
                      "Round number": 0,
                      "Time control:": '300',
                      "Number of player": 8,
                      "Comments:": 'Dictionnaire temporaire',
                      "Round 1": None,
                      "Round 2": None,
                      "Round 3": None,
                      "Round 4": None,
                      "Tournament's matches": {}
                      
                      
                      } #tournoi factice comme raccourci

        
        
        return tournament
        

class PlayersInput:

    def players_infos(self):
        """Appelle le module view et les input joueurs"""


        """players_input = view.PlayersView() 
        self.players = players_input.ask_players()"""
        
        self.players = [{"Player's family name:": 'Dupont', "Player's first name:": 'Alexandre', "Player's birthdate:": '1972', "Player's gender:": 'M', "Player's rank:": 11, "Pairing number": '1', "Score": 0, "Opponents":[]},
                        {"Player's family name:": 'Durand', "Player's first name:": 'Aurelie', "Player's birthdate:": '1990', "Player's gender:": 'F', "Player's rank:": 14, "Pairing number": '2', "Score": 0, "Opponents":[]},
                        {"Player's family name:": 'Dupuis', "Player's first name:": 'Monique', "Player's birthdate:": '1965', "Player's gender:": 'F', "Player's rank:": 16, "Pairing number": '3', "Score": 0, "Opponents":[]},
                        {"Player's family name:": 'Bepas', "Player's first name:": 'Marion', "Player's birthdate:": '1987', "Player's gender:": 'F', "Player's rank:": 17, "Pairing number": '4', "Score": 0, "Opponents":[]},
                        {"Player's family name:": 'Menant', "Player's first name:": 'laureen', "Player's birthdate:": '1994', "Player's gender:": 'F', "Player's rank:": 13, "Pairing number": '5', "Score": 0, "Opponents":[]},
                        {"Player's family name:": 'Liotard', "Player's first name:": 'David', "Player's birthdate:": '1974', "Player's gender:": 'X', "Player's rank:": 12, "Pairing number": '6', "Score": 0, "Opponents":[]},
                        {"Player's family name:": 'Roux', "Player's first name:": 'Cedric', "Player's birthdate:": '1979', "Player's gender:": 'M', "Player's rank:": 15, "Pairing number": '7', "Score": 0, "Opponents":[]},
                        {"Player's family name:": 'Gagnieu', "Player's first name:": 'Arnaud', "Player's birthdate:": '1991', "Player's gender:": 'M', "Player's rank:": 18, "Pairing number": '8', "Score": 0, "Opponents":[]}
                       ]#liste des joueurs factice comme raccourci

              
        return self.players

    def sorted_rank(self):
        """remet la liste des joueur dans l'ordre des ranks"""

        sorted_players = sorted(self.players, key=itemgetter("Player's rank:")) 

        return sorted_players  
