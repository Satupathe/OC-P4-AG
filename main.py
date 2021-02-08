""" Main file to launch every part of the MVC pattern"""

from Model import tournament
from Controller import menu



def main ():
	one_tournament_infos = menu.TournamentInput()
	tour_infos = one_tournament_infos.t_input()
	print(tour_infos)
	tournament_obj = tournament.Tournament(tour_infos[0], 
										   tour_infos[1],
										   tour_infos[2],
										   tour_infos[3],
										   tour_infos[4],
										   tour_infos[5],
										   tour_infos[6]
										  )

	print(tournament_obj.tournament_dict())
	tournament_obj.save()




if __name__ == '__main__':
	main()
