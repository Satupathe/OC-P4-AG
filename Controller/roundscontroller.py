from Model import match
from Controller import schedule
from View import view


class RoundController:
	def round_creation(self, match_players_list):

		match_1 = match.Match(match_players_list[0], match_players_list[4])
		match_2 = match.Match(match_players_list[1], match_players_list[5])
		match_3 = match.Match(match_players_list[2], match_players_list[6])
		match_4 = match.Match(match_players_list[3], match_players_list[7])

		match_list = [match_1, match_2, match_3, match_4]
		print(match_list)
		return match_list

	def send_round_1(self, first_round):

		view_round_1 = view.RoundView()
		view_round_1.first_round(first_round)