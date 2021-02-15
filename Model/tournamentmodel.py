#!/usr/bin/env python
# -*- coding: utf-8 -*-


""" Tournament class. 
Used to store tournament informations.
Keep informations available for the User
"""

from View import view
import json


class TournamentModel:
    """Permet d'ajouter les données tournoi et joueurs et de sauvegarder en json"""
      
    def add_tournament_and_players(self, tournament_dict, sorted_players):
        """combine les infos tournoi et joueurs ensemble"""
        total_tournament = tournament_dict
        total_tournament['players'] = sorted_players

        return total_tournament

    def json_save(self, dictionnary):
        """sauvegarde les infos tournoi et joueur dnas le json"""
        with open ('tournament.json', 'a', encoding='utf8') as tour:
            json.dump(dictionnary, tour, ensure_ascii=False, indent = 4)


