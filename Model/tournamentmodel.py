#!/usr/bin/env python
# -*- coding: utf-8 -*-


""" Tournament class. 
Used to store tournament informations.
Keep informations available for the User
"""

from View import view
from Model import rounds
import json


class TournamentModel:
    """Permet d'ajouter les données tournoi et joueurs et de sauvegarder en json"""
      
    
    def add_tournament_and_players(self, tournament_dict, players_list):
        """combine les infos tournoi et joueurs ensemble"""
        self.total_tournament = tournament_dict
        self.total_tournament["players"] = players_list
        return self.total_tournament

    def json_save(self, tournament_dict):
        """sauvegarde les infos tournoi et joueur dnas le json"""
        with open ('tournament.json', 'a', encoding='utf8') as tour:
            json.dump(tournament_dict, tour, ensure_ascii=False, indent = 4)

    def json_score_player(self, players_and_score):
       #télécharger le json en vue de faire des modifications dessus
        with open('tournament.json') as f:
            data = json.load(f)
        for player in data[:1]["players"]:
            player["Score"].replace(0, players_and_score[nb][1])
            #commencer à regarder tinyDB!!!!!!!!!!

    def json_opponent(self, players_and_score): #voir si pas dans json_score
        pass

    def get_match_list(self):
        self.played_matchs_list = []#décomposer par round !!!!!!
        return self.played_matchs_list


    def add_to_match_list(self, round_matches):
        self.played_matchs_list.append(round_matches)
        """print(self.played_matchs_list)"""      

    """def matchs_creations(self):
        for i in range(4):
            self.one_round.match_creation() # mettre dans tController ou roundsmodel?

#doit appeler plusieurs round

#creation d'un objet round 1 si liste vide"""

""" 
créer un tournoi
dans le tournoi créer un premier round


#pairing en fonction des rank et en vérifiant que les joueurs n'ont pas déjà joué ensemble
#fonction du model qui va appeler les instances de match et de joueur
#propose un match et vérifie les paring déjà effectués"""