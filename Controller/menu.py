""" Main file to launch every part of the MVC pattern"""

from View import view

from operator import itemgetter


class TournamentInput:
    """Controller calling view function with inputs of tournament informations"""
    def tournament_infos(self):
        """
        Call the ask_tournament function and informations about the new tournament
        return a dictionary of those informations
        """
        tournament_input = view.TournamentView()
        tournament = tournament_input.ask_tournament()

        return tournament


class PlayersInput:
    """Controller calling view function with inputs of players informations"""
    def players_infos(self):
        """
        Call the ask_players function and informations about players of the new tournament
        return a dictionary of those informations
        """
        players_input = view.PlayersView()
        self.players = players_input.ask_players()

        return self.players

    def sorted_rank(self):
        """Sort the players by their Pairing number"""

        sorted_players = sorted(self.players, key=itemgetter("Pairing number"))

        return sorted_players
