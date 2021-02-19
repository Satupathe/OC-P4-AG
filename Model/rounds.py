""" Round class. 
Used to store Round informations.
Keep informations available for the User
"""
from Model import match

class Round:
	"""match_list, start_date, end_date, start_hour, end_hour"""

	def __init__(self):
		pass
		
	def round_selection(self):
		

	def match_creation(self):
		one_match = match.Match()
		
	
	def pairing_first_round(selfn round_players):
		
		#contient la liste des matchs
		self.first_round_matches = []
		
		match_1 = match.Match(round_players[0], round_players[4])
        match_2 = match.Match(round_players[1], round_players[5])
        match_3 = match.Match(round_players[2], round_players[6])
        match_4 = match.Match(round_players[3], round_players[7])
        self.pairing_first_round.append(match_1.match_opponents())
        self.pairing_first_round.append(match_2.match_opponents())
        self.pairing_first_round.append(match_3.match_opponents())
        self.pairing_first_round.append(match_4.match_opponents())
        
		#les résultats de chaque match
		#la liste de chaque match (quel joueur contre quel joueur)
		#enregistrer des instances de match
		return self.first_round_matches

	def pairing_other_round(self):
		other_round_matches = []
		pass