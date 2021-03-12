""" Controller for creation and use of objects"""

from Controller import menu
from Model import tournamentmodel, player, rounds
from View import view
from operator import itemgetter
import os
import pendulum

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
            """une fois que l'utilisateur a retrouvé le numéro du tournoi qu'il souhaite avoir
            il peut demander la continuation de celui-ci
            fait en sorte de reprendre au bon numéro de round
            et de réaliser le bon nombre de tours en fonction de ce numéro """


        elif self.running == "show":
            print("")
            informations = ShowInformationsController()
            informations = informations()
            """retrouver un tournoi en fonction de non nom et de sa date
            afficher le numéro du tournoi (objet json) associé à sa date et à son nom.  """

            """elif exit du programme qui ferme la console windows"""

        elif self.running =="exit":
            os._exit("A bientot")


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
        print(lenght_db)
        print(type(lenght_db))

        if tournament_number > lenght_db:
            print("Merci d'entrer le numero valide d'un tournoi")
            self.__call__()
        
        else:
            tournament = TournamentController()
            tournament.round_players(tournament_number)
            tournament.round_selection(tournament_number)
            tournament.call_final_score()


class ShowInformationsController:
    def __call__(self):
        pass


class LaunchTournamentController:

    def __call__(self):
        tournament_number = 0
        tournament = TournamentController()
        tournament.call_tournament()
        tournament.call_players()
        tournament.group_tournament_and_players()
        tournament.json_save()
        tournament.round_players(tournament_number)
        tournament.round_selection(tournament_number)
        tournament.call_final_score()


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
        return(self.players_list)

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
            one_player = player.Player(players[i])
            player_i = one_player.match_player()
            self.round_players.append(player_i)
        #print("self.round_players: ", self.round_players)
        return self.round_players

    def round_selection(self, tournament_number):
        self.tournament = tournamentmodel.TournamentModel()
        """played_matchs_list = self.tournament.get_match_list()"""
        players_and_score = []
        previous_round_number = self.tournament.get_round_number(tournament_number)
        """print(previous_round_number)"""
        number_of_round = 4 - previous_round_number
        
        for r in range(number_of_round):
            one_round = RoundController()
            round_nb = previous_round_number + 1            
            
            if previous_round_number == 0:
                matchs_round_1 = one_round.first_round(self.round_players, round_nb)
                """self.tournament.add_to_match_list(matchs_round_1)"""

                for k in range(4):
                    players_and_score.append(matchs_round_1[k][0])
                    players_and_score.append(matchs_round_1[k][1])
                self.tournament.json_score_opponent_player(players_and_score, matchs_round_1, tournament_number)

            else:
                actual_round = self.tournament.get_previous_round_list(tournament_number)
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
                """self.tournament.add_to_match_list(score_other_round)"""
                self.players_and_score_other_round = []
                #print ("players and score: ", self.players_and_score_other_round)
                for k in range (4):
                    self.players_and_score_other_round.append(score_other_round[k][0])
                    self.players_and_score_other_round.append(score_other_round[k][1]) 
                #print("la liste des joueurs fin tour ", self.players_and_score_other_round)         
                
                self.tournament.json_score_opponent_player(self.players_and_score_other_round, score_other_round, tournament_number)
            previous_round_number += 1

    def call_final_score(self):
        sorted_list = sorted(self.players_and_score_other_round, key=lambda x: x[3], reverse=True)
        """print("sorted_list:", sorted_list) """
        
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


class RoundController:
            

    def first_round(self, round_players, round_nb):
        
        first_round = rounds.Round()              
        match_list = first_round.pairing_first_round(round_players)

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

        return match_list
    
    def other_round(self, round_player, round_nb):
        #Permet de créer les autres rounds en fonction des matchs déjà effectués
        
        other_round = rounds.Round()
        match_list = other_round.pairing_other_round(round_player) 
        
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

        return match_list
        # faire en premier un chemin vers round puis vers le json et le calcul ici.
