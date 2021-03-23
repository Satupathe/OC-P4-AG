from View import view
from Model import tournamentmodel
from Controller import schedule

class ShowInformationsController:
    def __call__(self):
        self.level = view.CallShowAction()
        answer = self.level.ask_show_action()
        self.number = view.CallTournamentNumber()
        
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
            self.__call__()

        else:
            print("Merci d'entrer: 'total', 'unfinished' ou 'back'. Veiller à ne pas mettre de majuscules")
            self.show_tournaments()

    def show_specific_informations(self):
        self.level.ask_tournament_id()
        tournament_id = self.number.ask_number()
        print("tournament id:  ", tournament_id)
        answer = self.level.ask_tournament_action(tournament_id)
        informations = None
        info_type = None
        if answer == "score":
            informations = self.model.sorted_score_1T(tournament_id)
            info_type = "Scores"

        elif answer == "name":
            informations = self.model.sorted_name_1T(tournament_id)
            info_type = "Noms"

        elif answer == "rounds":#finir la mise en forme
           informations = self.model.sorted_rounds_1T(tournament_id)
            
           info_type = "rounds"

        elif answer == "matchs":
            informations = self.model.sorted_matches_1T(tournament_id)  
            info_type = "matchs"

        elif answer == "back":
            self.show_specific_informations()

        elif answer == "menu":
            self.__call__() #attention à la bonne fonction de retour
            #attentions aux erreur à vérifier!!!!!

        else:
            print("Merci d'entrer: 'score', 'name', 'rounds', 'matchs', 'back' ou 'menu'. Veiller à ne pas mettre de majuscules")
            self.show_specific_informations()

        self.level.print_specific_informations(tournament_id, info_type, informations)
        self.show_specific_informations()

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
        self.model = tournamentmodel.TournamentModel()
        informations = self.model.total_players_actual_rank() 
        info_type = "rank"
        self.level.print_sorted_players(info_type, informations)
        self.__call__()

    def show_players_name(self):
        self.model = tournamentmodel.TournamentModel()
        informations = self.model.total_players_name()
        info_type = "nom"
        self.level.print_sorted_players(info_type, informations)
        self.__call__()