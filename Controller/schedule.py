""" Controller for creation and use of objects"""

import os
import sys
import pendulum

from operator import itemgetter

from Controller import menu, show
from Model import tournamentmodel, playermodel, rounds
from View import view


class FrontController:
    def __init__(self):
        self.controller = None
        

    def start(self):
        self.running = MainMenuController()
        self.running = self.running()
            
        if self.running == "start":
            print("")
            new = LaunchTournamentController()
            new = new()
            """mettre la liste des matchs disputés dans le fichier json plutot que dans une liste random 
            demander si l'utilisateur veut commencer le round 
            --> afficher entre matchs du round et demande de résultats
            si réponse non demander si retourner au menu principal?
            si non redemander le début du round
            si oui retourner au menu principal"""

        elif self.running == "continuation":
            print("")
            continuation = ContinueTournamentController()
            continuation = continuation()

        elif self.running == "show":
            print("")
            informations = show.ShowInformationsController()
            informations = informations()
            """retrouver un tournoi en fonction de non nom et de sa date
            afficher le numéro du tournoi (objet json) associé à sa date et à son nom.  """

            """elif exit du programme qui ferme la console windows"""

        elif self.running =="exit":
            os.system("exit")


        else:
            print("Merci d'entrer: start, continuation ou show. Veiller a ne pas mettre de majuscules")
            self.start()


class MainMenuController:
    def __call__(self):
        self.action = view.HomeMenuView()
        self.action = self.action()
        
        return self.action
            

class ContinueTournamentController:
    def __call__(self):
        call = view.CallTournamentNumber()
        tournament_number = call.ask_number()
        lenght = tournamentmodel.TournamentModel()
        lenght_db = lenght.get_length_db()

        if tournament_number > lenght_db:
            print("Merci d'entrer le numero valide d'un tournoi") # remettre dnas la view
            self.__call__()
        
        else:
            tournament = TournamentController()
            tournament.round_players(tournament_number)
            action = tournament.round_selection(tournament_number)
            menu = FrontController()

            if action is not None:
                menu.start()
            else:
                tournament.call_final_score()
                ask_rank = view.RankChange()
                change_ranks = ask_rank.ask_ended_tournament()
           
                if change_ranks == "yes":
                    new_ranks = tournament.ask_rank_modification(action[1])
                    print("new ranks:  ", new_ranks)
                    tournament.final_rank_modification(new_ranks)
                else:
                    pass

        menu.start()


class LaunchTournamentController:

    def __call__(self):
        tournament_number = 0
        tournament = TournamentController()
        tournament.call_tournament()
        tournament.call_players()
        tournament.group_tournament_and_players()
        tournament.json_save()
        tournament.round_players(tournament_number)
        action = tournament.round_selection(tournament_number)
        print("action :  ", action)
        print("action 0:  ", action[0])
        print("action 1:  ", action[1])
        menu = FrontController()
        
        if action[0] == "menu":
            
            menu.start()
        else:
            tournament.call_final_score()
            ask_rank = view.RankChange()
            change_ranks = ask_rank.ask_ended_tournament()
           
            if change_ranks == "yes":
                new_ranks = tournament.ask_rank_modification(action[1])
                print("new ranks:  ", new_ranks)
                tournament.final_rank_modification(new_ranks)
            else:
                pass

        menu.start()

class TournamentController:

    def __init__(self): 
        self.tournament_input = menu.TournamentInput()
        self.players_input = menu.PlayersInput()
        self.tournament = tournamentmodel.TournamentModel()

    def call_tournament(self):# inputs du tournoi OK
        self.tournament_dict = self.tournament_input.tournament_infos()
        return self.tournament_dict

    def call_players(self): # inputs des joueurs OK
        self.players_input.players_infos() 
        self.players_list = self.players_input.sorted_rank() 
        return(self.players_list) #sorted by pairing number

    def group_tournament_and_players(self): # OK
        tournament_infos = tournamentmodel.TournamentModel()
        self.total_tournament = tournament_infos.add_tournament_and_players(self.tournament_dict, self.players_list)
        return self.total_tournament

    def json_save(self): # OK
        save = tournamentmodel.TournamentModel()
        save.json_save(self.total_tournament)

    def round_players(self, tournament_number): #liste des joueur  OK
        players = self.tournament.get_players(tournament_number)
        self.round_players = [] 
        for i in range(8):
            one_player = playermodel.Player(players[i])
            player_i = one_player.match_player()
            self.round_players.append(player_i)
        return self.round_players

    def round_selection(self, tournament_number):
        self.tournament = tournamentmodel.TournamentModel()
        self.rank_change = view.RankChange()
        players_and_score = []
        previous_round_number = self.tournament.get_round_number(tournament_number)
        number_of_round = 4 - previous_round_number
        action = None
        
        for r in range(number_of_round):
            one_round = RoundController()
            round_nb = previous_round_number + 1            
            next_round = view.AskContinue().ask_go_next_round()

            if next_round == "yes":
                pass

            else:
                action = "menu"
                break
            
            if previous_round_number == 0:
                matchs_round_1 = one_round.first_round(self.round_players, round_nb)
                start = matchs_round_1[1]
                end = matchs_round_1[2]
                #print("score_first_round ", matchs_round_1)

                for k in range(4):
                    players_and_score.append(matchs_round_1[0][k][0])
                    players_and_score.append(matchs_round_1[0][k][1])

                scores = sorted(players_and_score, key=lambda x: x[2], reverse=False) # by pairing number
                self.tournament.json_score_opponent_player(scores, matchs_round_1[0], tournament_number, round_nb, start, end)
                

                ask_rank_change = self.rank_change.ask_ongoing_tournament()
                if ask_rank_change == "yes":
                    pairing_and_rank = self.ask_rank_modification(players_and_score)
                    print("pairing and rank:  ", pairing_and_rank)
                    for i in range(8):
                        for element in pairing_and_rank:
                            if element[0] == players_and_score[i][2]:
                                players_and_score[i][1] = element[1]
                                
                            else:
                                pass
                    sorted_new_ranks = sorted(players_and_score, key=lambda x: x[2], reverse=False) # by pairing number
                    new_rank_players = self.tournament.get_players(tournament_number)
                    print("new_rank_players 1:  ", new_rank_players)
                    p = 0
                    for player in new_rank_players:
                        player["Rank"] = sorted_new_ranks[p][1]
                        p += 1
                    
                    print("new_rank_players 2:  ", new_rank_players)

                    self.tournament.save_new_ranks(new_rank_players)
                

                else:
                    pass
                

            else:
                actual_round = self.tournament.get_previous_round_list(tournament_number)
                print("actual_round: ", actual_round)
                round_player_list = []
                matchs_other_round = []

                for i in range (8):
                    one_player = playermodel.Player(actual_round[i])
                    round_player = one_player.match_player()
                    round_player_list.append(round_player)

                print("round_player_list:   ", round_player_list)

                for j in range (1, 8, 2):
                    j1 = round_player_list[j-1]
                    j2 = round_player_list[j]
                    match = (j1, j2)
                    matchs_other_round.append(match)

                print("Matchs other round:  ", matchs_other_round)
                
                score_other_round = one_round.other_round(round_player_list, round_nb)
                start = score_other_round[1]
                end = score_other_round[2]
                #print("score_other_round ", score_other_round)
                self.players_and_score_other_round = []
                #print ("players and score: ", self.players_and_score_other_round)
                for k in range (4):
                    self.players_and_score_other_round.append(score_other_round[0][k][0])
                    self.players_and_score_other_round.append(score_other_round[0][k][1]) 
                #print("la liste des joueurs fin tour ", self.players_and_score_other_round)         
                
                ask_rank_change = self.rank_change.ask_ongoing_tournament()
                if ask_rank_change == "yes":
                    to_change = self.ask_rank_modification(players_and_score_other_round)
                    for pairing_number in to_change:
                        # faire les modifications dans players_and_score...
                        pass
                else:
                    pass

                self.tournament.json_score_opponent_player(self.players_and_score_other_round, score_other_round[0], tournament_number, round_nb, start, end)
            previous_round_number += 1

        return action, self.players_and_score_other_round

    def call_final_score(self):
        
        sorted_list = sorted(self.players_and_score_other_round, key=lambda x: x[3], reverse=True)
        
        final_sorted_list = []
      
        score = 4.0
        while len(final_sorted_list)< 8: # permet de classer par score et par rank
            by_score = []
            for player in sorted_list:  
                if player[3] == score:
                    by_score.append(player)
            
            by_score.sort(key=lambda x: x[1], reverse=False)
            for item in by_score:
                final_sorted_list.append(item)
            score -= 0.5
        
        podium = view.FinalScore()
        podium.print_results(final_sorted_list)

    
    def ask_rank_modification(self, players_and_score):
        players_rank_modification = []#liste de listes avec pairing number et nouveau rank
        
        for player in players_and_score:
            answer = self.rank_change.ask_all_player(player)
            if answer == "yes":
                new_rank = self.rank_change.ask_new_rank()
                pairing_and_rank = (player[2], new_rank)
                players_rank_modification.append(pairing_and_rank)
            else:
                pass
        
        print("players_rank_modification:  ", players_rank_modification)
        return players_rank_modification

    def final_rank_modification(self, new_ranks, tournament_number, players_and_score):
        for i in range(8):
            for element in new_ranks:
                if element[0] == players_and_score[i][2]:
                    players_and_score[i][1] = element[1]
                    
                else:
                    pass

        new_rank_players = self.tournament.get_players(tournament_number)
        self.tournament.save_new_ranks(new_rank_players)


sorted_new_ranks = sorted(players_and_score, key=lambda x: x[2], reverse=False) # by pairing number
                    new_rank_players = self.tournament.get_players(tournament_number)
                    print("new_rank_players 1:  ", new_rank_players)
                    p = 0
                    for player in new_rank_players:
                        player["Rank"] = sorted_new_ranks[p][1]
                        p += 1
                    
                    print("new_rank_players 2:  ", new_rank_players)

                    self.tournament.save_new_ranks(new_rank_players)

        """all_players = self.tournament.total_players_name()
        print("all_players:  ", all_players)
        rank = view.RankChange()
        player_number = rank.ask_one_player_number(all_players)
        new_rank = rank.ask_new_rank()
        all_players[player_number]["Rank"] = new_rank"""





class RoundController:
            

    def first_round(self, round_players, round_nb):
        
        first_round = rounds.Round()              
        rank_players = sorted(round_players, key=lambda x: x[1], reverse=False)
        match_list = first_round.pairing_first_round(rank_players) 

        for i in range(4):
            view_first_round = view.RoundView(i, round_nb, match_list[i])

        round_actions = view.AskContinue()
        round_actions.ask_start_round()
        begin = pendulum.now().to_cookie_string()
        print(begin)
        
        round_actions.ask_end_round()
        end = pendulum.now().to_cookie_string()
        print(end)
        print("")
        #retourner cette information, la combiner avec la liste des matchs --> enregistrer pour chaque round !!!!

        for i in range(4):
            score_player_1 = view_first_round.ask_result(match_list[i][0])
            score_player_2 = view_first_round.ask_result(match_list[i][1])
            match_list[i][0][3] += float(score_player_1)
            match_list[i][1][3] += float(score_player_2)          

        return match_list, begin, end #match_list par rank
    
    def other_round(self, round_players, round_nb):
        #Permet de créer les autres rounds en fonction des matchs déjà effectués
        
        other_round = rounds.Round()
        #rank_players = sorted(round_players, key=lambda x: x[1], reverse=False)
        match_list = other_round.pairing_other_round(round_players) 
        
        for i in range(4):
            view_other_round = view.RoundView(i, round_nb, match_list[i])
        
        round_actions = view.AskContinue()
        round_actions.ask_start_round()
        begin = pendulum.now().to_cookie_string()
        print(begin)
        
        round_actions.ask_end_round()
        end = pendulum.now().to_cookie_string()
        print(end)
        print("")

        for i in range(4):
            score_player_1 = view_other_round.ask_result(match_list[i][0])
            score_player_2 = view_other_round.ask_result(match_list[i][1])
            match_list[i][0][3] += float(score_player_1)
            match_list[i][1][3] += float(score_player_2)          

        return match_list, begin, end #match_list par rank
