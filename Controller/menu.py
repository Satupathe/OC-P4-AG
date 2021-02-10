""" Main file to launch every part of the MVC pattern"""

from Model import tournament
from View import view


class TournamentController:

    def tournament_infos(self):

        """one_tournament_infos = view.TournamentView()
        tour_infos = one_tournament_infos.ask_tournament()
        print(tour_infos)"""

        tournoi_bypass = {'Name': 'Expert', 'Adress': 'Chassieu', 'Date': 'Janvier', 'number of round' : 8, 'Time': '350', 'Nb Players': 8, 'comments': 'Dictionnaire temporaire'}
        # Doit normalement aller dans view.py
        print(tournoi_bypass)
        return tournoi_bypass

class PlayersController:

    def players_infos(self):

        """players = view.PlayersView(8) 
        players_infos = print(players.ask_players())"""
        
        joueurs_bypass = {}
        joueurs_bypass['1'] = {'nom': 'Dupont', 'prenom': 'Alexandre', 'anniversaire': '1972', 'genre': 'M', 'rank': '1'}
        joueurs_bypass['2'] = {'nom': 'Durand', 'prenom': 'Aurelie', 'anniversaire': '1990', 'genre': 'F', 'rank': '4'}
        joueurs_bypass['3'] = {'nom': 'Dupuis', 'prenom': 'Monique', 'anniversaire': '1965', 'genre': 'F', 'rank': '6'}
        joueurs_bypass['4'] = {'nom': 'Bepas', 'prenom': 'Marion', 'anniversaire': '1987', 'genre': 'F', 'rank': '7'}
        joueurs_bypass['5'] = {'nom': 'Menant', 'prenom': 'laureen', 'anniversaire': '1994', 'genre': 'F', 'rank': '3'}
        joueurs_bypass['6'] = {'nom': 'Liotard', 'prenom': 'David', 'anniversaire': '1974', 'genre': 'X', 'rank': '2'}
        joueurs_bypass['7'] = {'nom': 'Roux', 'prenom': 'Cedric', 'anniversaire': '1979', 'genre': 'M', 'rank': '5'}
        joueurs_bypass['8'] = {'nom': 'Gagnieu', 'prenom': 'Arnaud', 'anniversaire': '1991', 'genre': 'M', 'rank': '8'}
        # Doit normalement aller dans view.py

        """print(players_infos)"""

        print(joueurs_bypass)
        return joueurs_bypass