""" Controller for creation and use of objects"""

from Controller import menu, roundscontroller
from Model import tournamentmodel, player, rounds
from View import view




class Schedule:
    
    def objects(self):   
        tournoi_input = menu.TournamentController()
        tournament_dict = tournoi_input.tournament_infos()

        players = menu.PlayersController() #créé l'objet players issu du controller menu
         
        sorted_players = players.sorting_rank(players.players_infos())
        print(sorted_players)

        tournament_save = tournamentmodel.TournamentModel()
        total_tournament = tournament_save.add_tournament_and_players(tournament_dict, sorted_players)
        """tournament_save.json_save(total_tournament)"""
        
        round_1 = rounds.Round()

        player_1 = player.Player(sorted_players[0])
        player_2 = player.Player(sorted_players[1])
        player_3 = player.Player(sorted_players[2])
        player_4 = player.Player(sorted_players[3])
        player_5 = player.Player(sorted_players[4])
        player_6 = player.Player(sorted_players[5])
        player_7 = player.Player(sorted_players[6])
        player_8 = player.Player(sorted_players[7])

        match_players_list = [player_1.match_player(),
                              player_2.match_player(),
                              player_3.match_player(),
                              player_4.match_player(),
                              player_5.match_player(),
                              player_6.match_player(),
                              player_7.match_player(),
                              player_8.match_player()
                             ]

        one_round = roundscontroller.RoundController()
        first_round = one_round.round_creation(match_players_list)
        view_first_round = one_round.send_round_1(first_round)
        
        #initialiser un round
        #donner un identifiant de match à chaque joueur
        #initialiser un match
        #initialier l'ensemble des matchs
        #ajouter les match au round
        #envoyer la liste des matchs du premier round à l'utilisateur
        #demander les résultats pour chaque match dans l'ordre
        #Ajouter les résultats(scores) obtenus aux tuples des matchs 
        #Ajouter les tuples des matchs au round
        #reclasser les joueurs en fonctions des points obtenus dans la liste 
        #proposer les nouveaux matchs
        #faire attention à ne pas opposer des joueurs ayant déjà joués ensemble.