""" Controller for creation and use of objects"""

from Controller import menu
from Model import tournamentmodel, player, rounds
from View import view
from operator import itemgetter


class ApplicationController:

    def call_controller(self):
        tournament = TournamentController()
        tournament.call_tournament()
        tournament.call_players()
        tournament.group_tournament_and_players()
        tournament.json_save()
        tournament.round_players()
        tournament.round_selection()
        tournament.call_final_score()


class TournamentController:

    def __init__(self): 
        self.tournament_input = menu.TournamentInput()
        self.players_input = menu.PlayersInput()

    def call_tournament(self):# inputs du tournoi OK
        self.tournament_dict = self.tournament_input.tournament_infos()
        return self.tournament_dict

    def call_players(self): # inputs des joueurs OK
        self.players_input.players_infos() 
        self.players_list = self.players_input.sorted_rank() 
        return(self.players_list)

    def group_tournament_and_players(self): # OK
        tournament_infos = tournamentmodel.TournamentModel()
        self.total_tournament = tournament_infos.add_tournament_and_players(self.tournament_dict, self.players_list)
        return self.total_tournament

    def json_save(self): # OK
        save = tournamentmodel.TournamentModel()
        save.json_save(self.total_tournament)

    def round_players(self): #liste des joueur  OK
        self.round_players = [] 
        for i in range(8):
            one_player = player.Player(self.players_list[i])
            player_i = one_player.match_player()
            self.round_players.append(player_i)
        #print("self.round_players: ", self.round_players)
        return self.round_players

    def round_selection(self):
        self.match_played = tournamentmodel.TournamentModel()
        played_matchs_list = self.match_played.get_match_list()
        players_and_score = []
        for r in range(4):
            one_round = RoundController()
            round_nb = r + 1            
            
            if len(played_matchs_list) == 0:
                matchs_round_1 = one_round.first_round(self.round_players, round_nb)
                self.match_played.add_to_match_list(matchs_round_1)

                for k in range(4):
                    players_and_score.append(matchs_round_1[k][0])
                    players_and_score.append(matchs_round_1[k][1])
                self.match_played.json_score_opponent_player(players_and_score, matchs_round_1)

            else:
                actual_round = self.match_played.get_previous_round_list()
                round_player_list = []
                matchs_other_round = []

                for i in range (8):
                    one_player = player.Player(actual_round[i])
                    round_player = one_player.match_player()
                    round_player_list.append(round_player)


                for j in range (1, 8, 2):
                    j1 = round_player_list[j-1]
                    j2 = round_player_list[j]
                    match = (j1, j2)
                    matchs_other_round.append(match)
                
                score_other_round = one_round.other_round(round_player_list, round_nb)
                self.match_played.add_to_match_list(score_other_round)
                self.players_and_score_other_round = []
                print ("players and score: ", self.players_and_score_other_round)
                for k in range (4):
                    self.players_and_score_other_round.append(score_other_round[k][0])
                    self.players_and_score_other_round.append(score_other_round[k][1]) 
                print("la liste des joueurs fin tour ", self.players_and_score_other_round)         

                
                self.match_played.json_score_opponent_player(self.players_and_score_other_round, score_other_round)

    def call_final_score(self):
        final_score_list = sorted(self.players_and_score_other_round, key=lambda x: x[3], reverse=True)
        print("final_score_list:", final_score_list)
        podium = view.FinalScore()
        podium.print_results(final_score_list)

class RoundController:
            

    def first_round(self, round_players, round_nb):
        
        first_round = rounds.Round()              
        match_list = first_round.pairing_first_round(round_players)

        for i in range(4):
            view_first_round = view.RoundView(i, round_nb, match_list[i])

        for i in range(4):
            score_player_1 = view_first_round.ask_results(match_list[i][0])
            score_player_2 = view_first_round.ask_results(match_list[i][1])
            match_list[i][0][3] += float(score_player_1)
            match_list[i][1][3] += float(score_player_2)          

        return match_list
 
    
        #appelle la fonction pairing du model qui utilise la liste des pairing
    
    def other_round(self, round_player, round_nb):
        #Permet de créer les autres rounds en fonction des matchs déjà effectués
        
        other_round = rounds.Round()
        match_list = other_round.pairing_other_round(round_player) 
        
        for i in range(4):
            view_other_round = view.RoundView(i, round_nb, match_list[i])

        for i in range(4):
            score_player_1 = view_other_round.ask_results(match_list[i][0])
            score_player_2 = view_other_round.ask_results(match_list[i][1])
            match_list[i][0][3] += float(score_player_1)
            match_list[i][1][3] += float(score_player_2)          

        return match_list
        # faire en premier un chemin vers round puis vers le json et le calcul ici.
