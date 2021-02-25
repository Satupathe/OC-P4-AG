""" Controller for creation and use of objects"""

from Controller import menu, roundscontroller
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

    def round_players(self): #liste des joueur
        self.round_players = [] 
        for i in range(8):
            one_player = player.Player(self.players_list[i], i)
            player_i = one_player.match_player()
            self.round_players.append(player_i)
        return self.round_players

    def round_selection(self):
        match_played = tournamentmodel.TournamentModel()
        played_matchs_list = match_played.get_match_list()
        players_and_score = [] # possibilité de l'ajouter à la boucle else
        #chercher le nom du joueur en fonction de l'id dans le json
        for i in range(4):
            one_round = RoundController()
            if len(played_matchs_list) == 0:
                matches_round_1 = one_round.first_round(self.round_players)
                match_played.add_to_match_list(matches_round_1)
                for i in range(4):
                    players_and_score.append(matches_round_1[i][0])
                    players_and_score.append(matches_round_1[i][1])
                print("players and score: " + players_and_score)
                match_played.json_score_player(players_and_score)
                #ajouter l'adversaire pour chaque joueur 
                #enregistrer dans le json
            else:
                players_and_score.sort(key=lambda x: x[1], reverse=True)
                print("players and score: " + players_and_score)
                one_round.other_round(players_and_score)                    

    #boucle for (à placer) (range(4)) pour appeler les 4 rounds
#--> on arrive sur round controller OK
#--> on choisit la bonne fonction OK
#--> on propose un match
#--> on vérifie le pairing
#--> si match déjà joué, on propose le joueur suivant


class RoundController:
            

    def first_round(self, round_players):
        # sélectionne les instances de joueurs en fonction du rank initial
        
        first_round = rounds.Round()              
        self.match_list = first_round.pairing_first_round(round_players)

        self.j = 1
        for i in range(4):
            view_first_round = view.RoundView(i, self.j, self.match_list[i])
        self.j += 1
        for i in range(4):
            score_player_1 = view_first_round.ask_results(self.match_list[i][0])
            score_player_2 = view_first_round.ask_results(self.match_list[i][1])
            self.match_list[i][0][1] += float(score_player_1)
            self.match_list[i][1][1] += float(score_player_2)          
            print(score_player_1)
            print(score_player_2)
        return self.match_list
            #enregistrer les adversaires dans chaque joueur
            #garder ce résultat
            #récupérer les infos du 
    
        #appelle la fonction pairing du model qui utilise la liste des pairing
    
    def other_round(self, players_and_score):
        #Permet de créer les autres rounds en fonction des matchs déjà effectués
        
        other_round = rounds.Round()
        other_round.pairing_other_round(players_and_score)
        pass

    def send_round_1(self):
        pass


        #donner un identifiant de match à chaque joueur
        #initialiser un match
        #initialier l'ensemble des matchs
        #ajouter les match au round
        #envoyer la liste des matchs du premier round à l'utilisateur
        #demander les résultats pour chaque match dans l'ordre
        #Ajouter les résultats(scores) obtenus aux tuples des matchs 
        #Ajouter les tuples des matchs au round
        #reclasser les joueurs en fonctions des points obtenus dans la liste """
