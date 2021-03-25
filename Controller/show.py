"""
Controller of the show menu
Ask for wanted type of informations
Call saved informations in the database through trounamntmodel functions
Send those informations to the view
"""

from View import view
from Model import tournamentmodel
from Controller import schedule


class ShowInformationsController:
    """class to control show menu and interactions with view and model/database"""

    def __call__(self):
        """create objects useful for other functions, Display show menu and ask for action"""
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

    def show_tournaments(self):
        """sub menu of the tournament choice in main show menu"""
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
        """
        Ask for the wanted type of tournament's informations
        Call tournamentmodel functions to get those informations
        Display them to the user through the view
        """
        self.level.ask_tournament_id()
        tournament_id = self.number.ask_number()
        answer = self.level.ask_tournament_action(tournament_id)
        informations = None
        info_type = None
        if answer == "score":
            informations = self.model.sorted_score_1T(tournament_id)
            info_type = "Scores"
        elif answer == "name":
            informations = self.model.sorted_name_1T(tournament_id)
            info_type = "Noms"
        elif answer == "rounds":
            informations = self.model.sorted_rounds_1T(tournament_id)
            info_type = "rounds"
        elif answer == "matchs":
            informations = self.model.sorted_matches_1T(tournament_id)
            info_type = "matchs"
        elif answer == "back":
            self.show_specific_informations()
        elif answer == "menu":
            self.__call__()
        else:
            print(
                "Merci d'entrer: 'score', 'name', 'rounds', 'matchs', 'back' ou 'menu'.",
                "Veiller à ne pas mettre de majuscules"
            )
            self.show_specific_informations()

        self.level.print_specific_informations(tournament_id, info_type, informations)
        self.show_specific_informations()

    def show_total_players(self):
        """
        Sub menu of the total players choice in main show menu
        Ask for wanted format of all saved players through view
        """
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
        """
        Call tournamentmodel functions to get all saved players sort by rank
        Display them to the user through the view
        """
        self.model = tournamentmodel.TournamentModel()
        informations = self.model.total_players_actual_rank()
        info_type = "rank"
        self.level.print_sorted_players(info_type, informations)
        self.__call__()

    def show_players_name(self):
        """
        Call tournamentmodel functions to get all saved players sort by name
        Display them to the user through the view
        """
        self.model = tournamentmodel.TournamentModel()
        informations = self.model.total_players_name()
        info_type = "nom"
        self.level.print_sorted_players(info_type, informations)
        self.__call__()
