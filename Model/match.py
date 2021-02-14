""" Match class. 
Used to store match informations.
Keep informations available for the User
"""

class Match:
	def __init__(self, player_1, player_2, results_player_1=0, result_player_2=0):
		self.player_1 = player_1
		self.player_2 = player_2
		self.result_player_1 = 0
		self.result_player_2 = 0