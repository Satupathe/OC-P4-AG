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
      
    
    def add_tournament_and_players(self, tournament_dict, sorted_players_list):
        """combine les infos tournoi et joueurs ensemble"""
        self.total_tournament = tournament_dict
        self.total_tournament["players"] = sorted_players_list
        return self.total_tournament

    def json_save(self):
        """sauvegarde les infos tournoi et joueur dnas le json"""
        with open ('tournament.json', 'a', encoding='utf8') as tour:
            json.dump(self.total_tournament, tour, ensure_ascii=False, indent = 4)

    def get_matchs_list(self):
        self.played_matchs_list = []
        return self.played_matchs_list
        


    def matchs_creations(self):
        for i in range(4):
            self.one_round.match_creation()

#doit appeler plusieurs round

#creation d'un objet round 1 si liste vide