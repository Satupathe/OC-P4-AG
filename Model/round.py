""" Round class. 
Used to store Round informations.
Keep informations available for the User
"""

class Round:
	def __init__(self, match_list, start_date, end_date, start_hour, end_hour):
		self.match_list = match_list
		self.start_date = start_date
		self.end_date = end_date
		self.start_hour = start_hour
		self.end_hour = end_hour