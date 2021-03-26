"""
Controller to call mennus and manage tournaments:
Call view for user action and informations
Allow to start or continue a tournament
Call tournament number
Call informations on tournament and players
function to choose a round and go through it
"""
import sys
import os

import pendulum

from Controller import menu, show
from Model import tournamentmodel, playermodel, rounds
from View import view


class FrontController:
    """Class of the  main menu"""

    def __init__(self):
        self.controller = None

    def clear(self):
        """Function to clear the terminal"""
        os.system('CLS')

    def start(self):
        """
        Function Controller MainMenuController to ask action on the main menu
        Call other Controllers following user input
        """
        self.running = MainMenuController()
        self.running = self.running()

        if self.running == "start":
            print("")
            new = LaunchTournamentController()
            new = new()

        elif self.running == "continuation":
            print("")
            continuation = ContinueTournamentController()
            continuation = continuation()

        elif self.running == "show":
            print("")
            informations = show.ShowInformationsController()
            informations = informations()

        elif self.running == "exit":
            sys.exit()

        elif self.running == "clear":
            self.clear()
            self.start()


class MainMenuController:
    """Class calling view class to ask action on the main menu"""

    def __call__(self):
        self.action = view.HomeMenuView()
        self.action = self.action.call_first_action()

        return self.action


class ContinueTournamentController:
    """
    Class to continue a previous tournament
    Ask tournament number to continu through the view
    Launch functions in TournamentController
    Change of players rank if asked by the user
    """

    def __call__(self):
        lenght = tournamentmodel.TournamentModel()
        lenght_db = lenght.get_length_db()
        call = view.CallTournamentNumber()
        tournament_number = call.ask_number()

        if tournament_number > lenght_db:
            call.ask_again()
            self.__call__()

        else:
            tournament = TournamentController()
            tournament.round_players(tournament_number)
            action = tournament.round_selection(tournament_number)
            menu = FrontController()

            if action[0] is not None:
                menu.start()
            else:
                tournament.call_final_score()
                ask_rank = view.RankChange()
                change_ranks = ask_rank.ask_ended_tournament()

                if change_ranks == "yes":
                    new_ranks = tournament.ask_rank_modification(action[1])
                    tournament.final_rank_modification(new_ranks, tournament_number, action[1])

        menu.start()


class LaunchTournamentController:
    """
    Class to start a new tournament
    Launch functions in TournamentController
    Ask all informations about the new tournament
    Change of players rank if asked by the user
    """

    def __call__(self):
        tournament_number = 0
        tournament = TournamentController()
        tournament.call_tournament()
        tournament.call_players()
        tournament.group_tournament_and_players()
        tournament.json_save()
        tournament.round_players(tournament_number)
        action = tournament.round_selection(tournament_number)
        menu = FrontController()

        if action[0] is not None:
            menu.start()
        else:
            tournament.call_final_score()
            ask_rank = view.RankChange()
            change_ranks = ask_rank.ask_ended_tournament()

            if change_ranks == "yes":
                new_ranks = tournament.ask_rank_modification(action[1])
                tournament.final_rank_modification(new_ranks, tournament_number, action[1])

        menu.start()


class TournamentController:
    """Controller of all actions on a tournament and its informations"""

    def __init__(self):
        """create object about other modules in the code (model, view and menu controller)"""
        self.tournament_input = menu.TournamentInput()
        self.players_input = menu.PlayersInput()
        self.tournament = tournamentmodel.TournamentModel()

    def call_tournament(self):
        """Call menu controller to ask tournament informations"""
        self.tournament_dict = self.tournament_input.tournament_infos()
        return self.tournament_dict

    def call_players(self):
        """Call menu controller to ask players informations"""
        self.players_input.players_infos()
        self.players_list = self.players_input.sorted_rank()
        return self.players_list

    def group_tournament_and_players(self):
        """Call a model function to group tournament and players informations"""
        tournament_infos = tournamentmodel.TournamentModel()
        self.total_tournament = tournament_infos.add_tournament_and_players(self.tournament_dict, self.players_list)
        return self.total_tournament

    def json_save(self):
        """Call the model funciton to save bases informations about the new tournament"""
        save = tournamentmodel.TournamentModel()
        save.json_save(self.total_tournament)

    def round_players(self, tournament_number):
        """Create round players with only usefull informations to show"""
        players = self.tournament.get_players(tournament_number)
        self.round_players = []
        for i in range(8):
            one_player = playermodel.Player(players[i])
            player_i = one_player.match_player()
            self.round_players.append(player_i)
        return self.round_players

    def round_selection(self, tournament_number):
        """
        Function to work through rounds
        Recognize if you're on the first round or another
        Create round objects
        Call model functions to decide on the paring
        Call for results through the RoundController
        Ask for rank change through view function
        Save rounds results through model function
        """

        self.tournament = tournamentmodel.TournamentModel()
        self.rank_change = view.RankChange()
        players_and_score = []
        players_and_score_other_round = []
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

                for k in range(4):
                    players_and_score.append(matchs_round_1[0][k][0])
                    players_and_score.append(matchs_round_1[0][k][1])

                scores = sorted(players_and_score, key=lambda x: x[2], reverse=False)
                self.tournament.json_score_opponent_player(
                    scores, matchs_round_1[0], tournament_number, round_nb, start, end
                )

                ask_rank_change = self.rank_change.ask_ongoing_tournament()
                if ask_rank_change == "yes":
                    pairing_and_rank = self.ask_rank_modification(players_and_score)
                    self.final_rank_modification(pairing_and_rank, tournament_number, players_and_score)

            else:
                actual_round = self.tournament.get_previous_round_list(tournament_number)
                round_player_list = []
                matchs_other_round = []

                for i in range(8):
                    one_player = playermodel.Player(actual_round[i])
                    round_player = one_player.match_player()
                    round_player_list.append(round_player)

                for j in range(1, 8, 2):
                    j1 = round_player_list[j - 1]
                    j2 = round_player_list[j]
                    match = (j1, j2)
                    matchs_other_round.append(match)

                score_other_round = one_round.other_round(round_player_list, round_nb)
                start = score_other_round[1]
                end = score_other_round[2]
                self.score_other_round = []

                for k in range(4):
                    self.score_other_round.append(score_other_round[0][k][0])
                    self.score_other_round.append(score_other_round[0][k][1])

                ask_rank_change = self.rank_change.ask_ongoing_tournament()
                if ask_rank_change == "yes":
                    to_change = self.ask_rank_modification(self.score_other_round)
                    self.final_rank_modification(to_change, tournament_number, self.score_other_round)

                players_and_score_other_round = self.score_other_round
                self.tournament.json_score_opponent_player(
                    self.score_other_round, score_other_round[0], tournament_number, round_nb, start, end
                )
            previous_round_number += 1

        return action, players_and_score_other_round

    def call_final_score(self):
        """Show final ranking and scores to the user"""
        sorted_score = sorted(self.score_other_round, key=lambda x: x[3], reverse=True)
        final_sorted_list = []

        score = 4.0
        while len(final_sorted_list) < 8:
            by_score = []
            for player in sorted_score:
                if player[3] == score:
                    by_score.append(player)
            by_score.sort(key=lambda x: x[1], reverse=False)
            for item in by_score:
                final_sorted_list.append(item)
            score -= 0.5

        podium = view.FinalScore()
        podium.print_results(final_sorted_list)

    def ask_rank_modification(self, players_and_score):
        """ask for players rank modifications"""
        players_rank_modification = []

        for player in players_and_score:
            answer = self.rank_change.ask_all_player(player)
            if answer == "yes":
                new_rank = self.rank_change.ask_new_rank()
                pairing_and_rank = (player[2], new_rank)
                players_rank_modification.append(pairing_and_rank)

        return players_rank_modification

    def final_rank_modification(self, new_ranks, tournament_number, players_and_score):
        """Function to change players rank at the end of the tournament"""
        for i in range(8):
            for element in new_ranks:
                if element[0] == players_and_score[i][2]:
                    players_and_score[i][1] = element[1]

        sorted_new_ranks = sorted(players_and_score, key=lambda x: x[2], reverse=False)
        new_rank_players = self.tournament.get_players(tournament_number)

        index = 0
        for player in new_rank_players:
            player["Rank"] = sorted_new_ranks[index][1]
            index += 1

        self.tournament.save_new_ranks(new_rank_players)


class RoundController:
    """Controller To ask rounds results"""

    def first_round(self, round_players, round_nb):
        """ask results for the first round"""
        first_round = rounds.Round()
        rank_players = sorted(round_players, key=lambda x: x[1], reverse=False)
        match_list = first_round.pairing_first_round(rank_players)

        for i in range(4):
            view_first_round = view.RoundView(i, round_nb, match_list[i])

        round_actions = view.AskContinue()
        round_actions.ask_start_round()
        begin = pendulum.now().to_cookie_string()

        round_actions.ask_end_round()
        end = pendulum.now().to_cookie_string()

        for i in range(4):
            score_player_1 = view_first_round.ask_result(match_list[i][0])
            score_player_2 = view_first_round.ask_result(match_list[i][1])
            match_list[i][0][3] += float(score_player_1)
            match_list[i][1][3] += float(score_player_2)

        return match_list, begin, end

    def other_round(self, round_players, round_nb):
        """ask results for the other rounds"""
        other_round = rounds.Round()
        match_list = other_round.pairing_other_round(round_players)

        for i in range(4):
            view_other_round = view.RoundView(i, round_nb, match_list[i])

        round_actions = view.AskContinue()
        round_actions.ask_start_round()
        begin = pendulum.now().to_cookie_string()

        round_actions.ask_end_round()
        end = pendulum.now().to_cookie_string()

        for i in range(4):
            score_player_1 = view_other_round.ask_result(match_list[i][0])
            score_player_2 = view_other_round.ask_result(match_list[i][1])
            match_list[i][0][3] += float(score_player_1)
            match_list[i][1][3] += float(score_player_2)

        return match_list, begin, end
