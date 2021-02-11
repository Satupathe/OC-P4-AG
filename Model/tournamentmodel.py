#!/usr/bin/env python
# -*- coding: utf-8 -*-


""" Tournament class. 
Used to store tournament informations.
Keep informations available for the User
"""

from View import view
import json


class TournamentModel:
    """docstring"""
      
    def __init__(self, name, adress, date, number_of_round, time, number_of_players, comments = None):
        self.name = name
        self.adress = adress
        self.date = date
        self.number_of_round = number_of_round
        self.time = time
        self.number_of_players = number_of_players
        self.comments = None

    def save(self, dictionnary):
        with open ('tournament.json', 'a', encoding='utf8') as tour:
            json.dump(dictionnary, tour, ensure_ascii=False, indent = 4)


