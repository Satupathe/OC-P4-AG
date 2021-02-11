""" Controller for creation and use of objects"""

from Controller import menu
from Model import tournamentmodel, player
from View import view


class Schedule:
    
    def objects(self):   
        tournoi_input = menu.TournamentController()
        tournoi_bypass = tournoi_input.tournament_infos()
        tournoi_initialise = tournamentmodel.TournamentModel(tournoi_bypass["Tournament's name:"],
                                                             tournoi_bypass["Tournament's adress:"],
                                                             tournoi_bypass["Tournament's Date:"],
                                                             tournoi_bypass["Total number of rounds:"],
                                                             tournoi_bypass["Time control:"],
                                                             tournoi_bypass["Number of player:"],
                                                             tournoi_bypass["Comments:"],
                                                            )
        
        essai = menu.PlayersController() #Changer le nom
        retour_dict = essai.players_infos(2) #Penser à l'enlever avant futures modifications

        player_dict = player.Players()
        
        dictionnary = player_dict.dict_construction(retour_dict['1'], retour_dict['2'], retour_dict['3'], retour_dict['4'], retour_dict['5'], retour_dict['6'], retour_dict['7'], retour_dict['8'])
        print(dictionnary)

        sorted_players = player_dict.sorting(dictionnary)
        print(sorted_players)

        """tournoi_initialise.save(t_dict)"""
        



