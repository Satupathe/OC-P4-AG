#!/usr/bin/env python
# -*- coding: utf-8 -*-


""" Tournament class. 
Used to store tournament informations.
Keep informations available for the User
"""

import json


class TournamentModel:
           
    def save(self, dictionnary):
        with open ('tournament.json', 'a', encoding='utf8') as tour:
            json.dump(dictionnary, tour, ensure_ascii=False, indent = 4)


