""" Main file to launch every part of the MVC pattern"""

from Model import tournamentmodel
from View import view


class TournamentController:

    def tournament_infos(self):

        """one_tournament_infos = view.TournamentView()
        tour_infos = one_tournament_infos.ask_tournament()
        print(tour_infos)"""

        tournoi_bypass = {"Tournament's name:": 'Expert',
                          "Tournament's adress:": 'Chassieu',
                          "Tournament's Date:": 'Janvier',
                          "Total number of rounds:": 4,
                          "Time control:": '300',
                          "Number of player:": 8,
                          "Comments:": 'Dictionnaire temporaire'
                          }

        
        print(tournoi_bypass)
        """return tour_infos"""
        return tournoi_bypass

class PlayersController:

    def players_infos(self, i):

        """players = view.PlayersView() 
        players_infos = players.ask_players(i)"""
        
        joueurs_bypass = {}
        joueurs_bypass['1'] = {"Player's family name:": 'Dupont', "Player's first name:": 'Alexandre', "Player's birthdate:": '1972', "Player's gender:": 'M', "Player's rank:": 1, "Pairing number": '', 'Score': 0}
        joueurs_bypass['2'] = {"Player's family name:": 'Durand', "Player's first name:": 'Aurelie', "Player's birthdate:": '1990', "Player's gender:": 'F', "Player's rank:": 4, "Pairing number": '', 'Score': 0}
        joueurs_bypass['3'] = {"Player's family name:": 'Dupuis', "Player's first name:": 'Monique', "Player's birthdate:": '1965', "Player's gender:": 'F', "Player's rank:": 6, "Pairing number": '', 'Score': 0}
        joueurs_bypass['4'] = {"Player's family name:": 'Bepas', "Player's first name:": 'Marion', "Player's birthdate:": '1987', "Player's gender:": 'F', "Player's rank:": 7, "Pairing number": '', 'Score': 0}
        joueurs_bypass['5'] = {"Player's family name:": 'Menant', "Player's first name:": 'laureen', "Player's birthdate:": '1994', "Player's gender:": 'F', "Player's rank:": 3, "Pairing number": '', 'Score': 0}
        joueurs_bypass['6'] = {"Player's family name:": 'Liotard', "Player's first name:": 'David', "Player's birthdate:": '1974', "Player's gender:": 'X', "Player's rank:": 2, "Pairing number": '', 'Score': 0}
        joueurs_bypass['7'] = {"Player's family name:": 'Roux', "Player's first name:": 'Cedric', "Player's birthdate:": '1979', "Player's gender:": 'M', "Player's rank:": 5, "Pairing number": '', 'Score': 0}
        joueurs_bypass['8'] = {"Player's family name:": 'Gagnieu', "Player's first name:": 'Arnaud', "Player's birthdate:": '1991', "Player's gender:": 'M', "Player's rank:": 8, "Pairing number": '', 'Score': 0}
       

        """print(players_infos)
        return players_infos"""

        print(joueurs_bypass)
        return joueurs_bypass