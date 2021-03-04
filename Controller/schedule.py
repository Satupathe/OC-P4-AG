""" Controller for creation and use of objects"""

from Controller import menu
from Model import tournamentmodel, player, rounds
from View import view


class ApplicationController:

    def call_controller(self):
        tournament = TournamentController()
        tournament.call_tournament()
        tournament.call_players()
        tournament.group_tournament_and_players()
        tournament.json_save()
        tournament.round_players()
        tournament.round_selection()


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
        match_played = tournamentmodel.TournamentModel()
        played_matchs_list = match_played.get_match_list()
        players_and_score = [] # possibilité de l'ajouter à la boucle else
        #chercher le nom du joueur en fonction de l'id dans le json
        for i in range(4):
            one_round = RoundController()
            j = 1
            if len(played_matchs_list) == 0:
                matchs_round_1 = one_round.first_round(self.round_players, j)
                match_played.add_to_match_list(matchs_round_1)
                for k in range(4):
                    players_and_score.append(matchs_round_1[i][0])
                    players_and_score.append(matchs_round_1[i][1])
                #print("la liste des joueurs fin tour 1", players_and_score)
                match_played.json_score_opponent_player(players_and_score, matchs_round_1)
                j += 1
                #ajouter l'adversaire pour chaque joueur 
                #enregistrer dans le json
            else:
                actual_round = match_played.get_previous_round_list()
                round_player_list = []
                for i in range (8):
                    one_player = player.Player(actual_round[i])
                    round_player = one_player.match_player()
                    round_player_list.append(round_player)
                print(round_player_list)
                matchs_other_round = []
                for j in range (0,8,2):
                    match = (round_player_list[int(i/2)],round_player_list[int(i/2+1)])
                    matchs_other_round.append(match)
                print("match matchs_other_round: ", matchs_other_round)
                score_other_round = one_round.other_round(round_player_list, j)
                #print("players and score la suite: " + str(players_and_score))
                   
                match_played.add_to_match_list(score_other_round)
                players_and_score = []
                print ("players and score: ", players_and_score)
                for k in range (4):
                    players_and_score.append(matchs_round_1[i][0])
                    players_and_score.append(matchs_round_1[i][1]) 
                print("la liste des joueurs fin tour ", players_and_score)         
                j += 1
                match_played.json_score_opponent_player(players_and_score, matchs_other_round)


class RoundController:
            

    def first_round(self, round_players, j):
        # sélectionne les instances de joueurs en fonction du rank initial
        
        first_round = rounds.Round()              
        match_list = first_round.pairing_first_round(round_players)

        nb_round = j
        for i in range(4):
            view_first_round = view.RoundView(i, nb_round, match_list[i])

        for i in range(4):
            score_player_1 = view_first_round.ask_results(match_list[i][0])
            score_player_2 = view_first_round.ask_results(match_list[i][1])
            match_list[i][0][3] += float(score_player_1)
            match_list[i][1][3] += float(score_player_2)          
        #print("self.match list: ", self.match_list)
        return match_list
            #enregistrer les adversaires dans chaque joueur
            #garder ce résultat
            #récupérer les infos du 
    
        #appelle la fonction pairing du model qui utilise la liste des pairing
    
    def other_round(self, round_player, j):
        #Permet de créer les autres rounds en fonction des matchs déjà effectués
        
        other_round = rounds.Round()
        match_list = other_round.pairing_other_round(round_player) 
        print("match list:", match_list)
        # faire en premier un chemin vers round puis vers le json et le calcul ici.
        
        nb_round = j
        for i in range(4):
            view_other_round = view.RoundView(i, nb_round, match_list[i])

        for i in range(4):
            score_player_1 = view_other_round.ask_results(match_list[i][0])
            score_player_2 = view_other_round.ask_results(match_list[i][1])
            match_list[i][0][3] += float(score_player_1)
            match_list[i][1][3] += float(score_player_2)          
        #print("self.match list: ", self.match_list)
        return match_list
        # faire en premier un chemin vers round puis vers le json et le calcul ici.
    



        #donner un identifiant de match à chaque joueur
        #initialiser un match
        #initialier l'ensemble des matchs
        #ajouter les match au round
        #envoyer la liste des matchs du premier round à l'utilisateur
        #demander les résultats pour chaque match dans l'ordre
        #Ajouter les résultats(scores) obtenus aux tuples des matchs 
        #Ajouter les tuples des matchs au round
        #reclasser les joueurs en fonctions des points obtenus dans la liste """
