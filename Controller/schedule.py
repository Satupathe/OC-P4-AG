""" Controller for creation and use of objects"""

from Controller import menu, roundscontroller
from Model import tournamentmodel, player, rounds
from View import view


class ApplicationController:

    def call_controller(self):
        self.tournament = tournamentmodel.TournamentModel()
        self.tournament_infos = TournamentController()
        self.tournament_infos.call_tournament()
        self.players_infos = TournamentController()
        self.players_infos.call_players()
        json_save = JsonSave(self.tournament_infos, self.players_infos)
        json_save.group_tournament_and_players()
        json_save.save_in_json()
        round_players = TournamentController()
        round_players.round_players_object()
        

class JsonSave:

    def __init__(self, tournament, players):
        self.tournament = tournament
        self.players = players

        
    def group_tournament_and_players(self):
        self.tournament.add_tournament_and_players(self.tournament, self.players)
    
    def save_in_json(self):
        self.tournament.json_save()        


class TournamentController:

    def __init__(self): 
        self.tournament_dict = menu.TournamentInput()
        self.players_list = menu.PlayersInput()

    def call_tournament(self):# inputs du tournoi
        self.tournament_dict.tournament_infos()
        print(self.tournament_dict)
        return self.tournament_dict

    def call_players(self): # inputs des joueurs
        self.players_list.players_infos() 
        self.players_list.sorted_rank() 
        print(self.players_list)
        return(self.players_list)     

    def round_players_object(self): #liste d'instances de joueur
        self.round_players = [] 
        for i in range(8):
            player_i = player.Player(self.players_list[i])
            round_players.append(player_i.match_player())
        return self.round_players

    def round_selection(self):
        self.played_matchs_list = tournamentmodel.TournamentModel()
        self.played_matchs_list.get_matchs_list
        
        for i in range(4): #faire des modifications
            one_round = RoundController(self.round_players)
            if len(self.played_matchs_list) == 0:
                one_round.first_round(self.round_players)

            else:
                one_round.other_round()
                # modifier la ligne suivante
                one_round.round_creation(self.round_players, self.played_matchs_list)# IMPORTANT!!
                # Envoyer les informations à la view


    #boucle for (à placer) (range(4)) pour appeler les 4 rounds
#--> on arrive sur round controller
#--> on choisit la bonne fonction
#--> on vérifie le pairing

class RoundController:

    def __init__(self, round_players):
        one_round = tournamentmodel.TournamentModel()
        self.played_matchs_list = TournamentModel()
        self.played_matchs_list.get_matchs_list()
        
    def first_round(self, round_players):
        # sélectionne les instances de joueurs en fonction du rank initial
        
        first_round = rounds.Round()              
        self.match_list = first_round.pairing_first_round(round_players)
        
        #demander pour score des matchs à l'utilisateur
        for i in range(self.match_list):
            view_first_round = view.RoundView(i)
            view_first_round.ask_results(self.match_list[i][0])
            match_tupple = ()
            #récupérer les résultats du premier joueur
            #garder ce résultat
            #récupérer les infos du 
    
        #appelle la fonction pairing du model qui utilise la liste des pairing
    
    def other_round(self):
        #Permet de créer les autres rounds en fonction des matchs déjà effectués
            other_round = rounds.Round()
            other_round.pairing_other_round()
        pass        


        
    def __repr__(self):
        pass
        #surcharger le fonction print(voir dicord et surcharge)

    def send_round_1(self):

        view_round_1 = view.RoundView()
        view_round_1.first_round(self.match_list)


    

#pairing en fonction des rank et en vérifiant que les joueurs n'ont pas déjà joué ensemble
#fonction du model qui va appeler les instances de match et de joueur
#propose un match et vérifie les paring déjà effectués

roundlist = tournamentmodel.TournamentModel()
roundlist.played_matchs_list()



#lors d'une reprise récupérer le round en cours dans le json.
#informations trouvable dans la liste des pairing.  

        #initialiser un round
        #donner un identifiant de match à chaque joueur
        #initialiser un match
        #initialier l'ensemble des matchs
        #ajouter les match au round
        #envoyer la liste des matchs du premier round à l'utilisateur
        #demander les résultats pour chaque match dans l'ordre
        #Ajouter les résultats(scores) obtenus aux tuples des matchs 
        #Ajouter les tuples des matchs au round
        #reclasser les joueurs en fonctions des points obtenus dans la liste """
