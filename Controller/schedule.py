""" Controller for creation and use of objects"""

from Controller import menu
from Model import tournament


class Schedule:
	
	def objects(self):
		tournoi = menu.TournamentController()
		players = menu.PlayersController()
		t_dict = tournoi.tournament_infos()
		p_dict = players.players_infos()
		t_dict['players'] = p_dict
		tournoi = t_dict
		essai_save = tournament.TournamentModel()
		essai_save.save(tournoi)
		



