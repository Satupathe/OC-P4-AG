""" Player class. 
Used to store player informations.
Keep informations available for the User
"""

class Player:
	def __init__(self, name, first_name, birth_date, gender, ranking):
		self.name = name
		self.first_name = first_name
		self.birth_date = birth_date
		self.gender = gender
		self.ranking = ranking