""" Main file to launch every part of the MVC pattern"""

from Model import tournamentmodel
from View import view

from operator import itemgetter


class TournamentInput:

    def tournament_infos(self):
        """Appelle le module view et les input du tournoi"""
        
        """tournament_input = view.TournamentView()
        tournament = tournament_input.ask_tournament()"""
        
        
        tournament = {"Tournament's name": 'essai',
                      "Tournament's adress": 'Chassieu',
                      "Tournament's Date": 'Janvier',
                      "Total number of rounds": 4,
                      "Round number": 0,
                      "Time control": '300',
                      "Number of player": 8,
                      "Comments": 'Dictionnaire temporaire',
                      "Rounds": {},                   
                     } #tournoi factice comme raccourci

        
        
        return tournament
        

class PlayersInput:

    def players_infos(self):
        """Appelle le module view et les input joueurs"""


        """players_input = view.PlayersView() 
        self.players = players_input.ask_players()"""
        
        self.players = [{"Family name": 'Dupont', "First name": 'Alexandre', "Birthdate": '1972', "Gender": 'M', "Rank": 11, "Pairing number": '1', "Score": 0, "Opponents":[]},
                        {"Family name": 'Durand', "First name": 'Aurelie', "Birthdate": '1990', "Gender": 'F', "Rank": 14, "Pairing number": '2', "Score": 0, "Opponents":[]},
                        {"Family name": 'Dupuis', "First name": 'Monique', "Birthdate": '1965', "Gender": 'F', "Rank": 16, "Pairing number": '3', "Score": 0, "Opponents":[]},
                        {"Family name": 'Bepas', "First name": 'Marion', "Birthdate": '1987', "Gender": 'F', "Rank": 17, "Pairing number": '4', "Score": 0, "Opponents":[]},
                        {"Family name": 'Menant', "First name": 'laureen', "Birthdate": '1994', "Gender": 'F', "Rank": 13, "Pairing number": '5', "Score": 0, "Opponents":[]},
                        {"Family name": 'Liotard', "First name": 'David', "Birthdate": '1974', "Gender": 'X', "Rank": 12, "Pairing number": '6', "Score": 0, "Opponents":[]},
                        {"Family name": 'Roux', "First name": 'Cedric', "Birthdate": '1979', "Gender": 'M', "Rank": 15, "Pairing number": '7', "Score": 0, "Opponents":[]},
                        {"Family name": 'Gagnieu', "First name": 'Arnaud', "Birthdate": '1991', "Gender": 'M', "Rank": 18, "Pairing number": '8', "Score": 0, "Opponents":[]}
                       ]#liste des joueurs factice comme raccourci

              
        return self.players

    def sorted_rank(self): # à éliminer ? 
        """remet la liste des joueur dans l'ordre des ranks"""

        sorted_players = sorted(self.players, key=itemgetter("Pairing number")) 

        return sorted_players  
