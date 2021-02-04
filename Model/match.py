""" Match class. 
Used to store match informations.
Keep informations available for the User
"""

class Match:
	def __init__(self, player_pair, results = None):
		self.player_pair = player_pair
		self.results = results