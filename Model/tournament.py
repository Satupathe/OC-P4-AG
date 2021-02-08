#!/usr/bin/env python
# -*- coding: utf-8 -*-


""" Tournament class. 
Used to store tournament informations.
Keep informations available for the User
"""

import json


class Tournament:
    def __init__(self, name, place, start_date, number_of_round, control_time, nb_players, comments):
        """save tournament attributes"""
        self.name = name
        self.place = place
        self.start_date = start_date
        self.number_of_round = number_of_round
        self.time = control_time
        self.players = nb_players
        self.comments = comments

    def tournament_dict(self):
        self.tournament = {}
        self.tournament['name'] = self.name
        self.tournament['place'] = self.place
        self.tournament['start_date'] = self.start_date
        self.tournament['number_of_round'] = self.number_of_round
        self.tournament['players'] = self.players
        self.tournament['time'] = self.time
        self.tournament['comments'] = self.comments
        return self.tournament

    

    def save(self):
        dictionnary = self.tournament
        with open ('tournament.json', 'a', encoding='utf8') as tour:
            json.dump(dictionnary, tour, ensure_ascii=False, indent = 4)


