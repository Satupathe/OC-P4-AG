from View import view
from Model import tournamentmodel

class ShowInformationsController:
    def __call__(self):
        self.level = view.CallShowAction()
        answer = self.level.ask_show_action()
        
        if answer == "tournaments":
            self.show_tournaments()

        elif answer == "total players":
            self.show_total_players()

        elif answer == "menu":
            menu = schedule.FrontController()
            menu.start()
           
        else:
            print("Merci d'entrer: 'tournaments', 'total players' ou 'menu'. Veiller à ne pas mettre de majuscules")
            self.__call__()

    def show_tournaments(self):# mettre des nom d'objet ? ou variables ?
        answer = self.level.ask_type_tournament()
        self.model = tournamentmodel.TournamentModel()

        if answer == "total":
            all_tournaments = self.model.get_total_tournaments()
            self.level.print_tournaments_list(all_tournaments)
            self.show_specific_informations()

        elif answer == "unfinished":
            unfinished_tournaments = self.model.get_unfinished_tournaments()
            self.level.print_unfinished_tournaments(unfinished_tournaments)
            self.show_specific_informations()

        elif answer == "back":
            __call__()

        else:
            print("Merci d'entrer: 'total', 'unfinished' ou 'back'. Veiller à ne pas mettre de majuscules")
            self.show_tournaments()

    def show_specific_informations(self):
        tournament_id = self.level.ask_tournament_id()
        answer = self.level.ask_tournament_action(tournament_id)
        informations = None
        info_type = None
        if answer == "score":
            informations = self.model.sorted_score_1T(tournament_id)
            #print("informations", informations)
            info_type = "score"

        elif answer == "name":
            informations = self.model.sorted_name_1T()
            info_type = "name"

        elif answer == "rounds":
           informations = self.model.sorted_rounds_1T()
           info_type = "rounds"

        elif answer == "matchs":
            informations = self.model.sorted_matches_1T()  
            info_type = "matchs"

        elif answer == "back":
            self.show_specific_informations()

        elif answer == "menu":
            self.__call__()

        else:
            print("Merci d'entrer: 'score', 'name', 'rounds', 'matchs', 'back' ou 'menu'. Veiller à ne pas mettre de majuscules")
            self.show_specific_informations()

        self.level.print_specific_informations(tournament_id, info_type, informations)

    def show_total_players(self):
        answer = self.level.ask_players_sorting()
        
        if answer == "rank":
            self.show_players_ranks()

        elif answer == "name":
            self.show_players_name()

        elif answer == "back":
            self.__call__()
           
        else:
            print("Merci d'entrer: 'rank', 'name' ou 'back'. Veiller à ne pas mettre de majuscules")
            self.show_total_players()

    def show_players_ranks(self):
        self.model.total_players_actual_rank() 
        #fait le tri et élimine les doublons
        info_type = "rank"
        #les classe en fonction des ranks actuels
        #affiche la liste
        pass

    def show_players_name(self):
        self.model.total_players_name()
        info_type = "nom"
        #récupère tous les joueurs en enlevant les doublons (rank actuel)
        #les classe par ordre alphabétique
        #affiche la liste
        pass