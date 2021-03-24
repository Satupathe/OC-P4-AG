"""
Round class
Used to store Round informations.
Keep informations available for the User
"""

from Model import match


class Round:
    """match creation for paired players"""
    def pairing_first_round(self, round_players):
        """Pairing and match creation for the firste round"""
        first_round_matches = []

        match_1 = match.Match(round_players[0], round_players[4])
        match_2 = match.Match(round_players[1], round_players[5])
        match_3 = match.Match(round_players[2], round_players[6])
        match_4 = match.Match(round_players[3], round_players[7])
        first_round_matches.append(match_1.match_opponents())
        first_round_matches.append(match_2.match_opponents())
        first_round_matches.append(match_3.match_opponents())
        first_round_matches.append(match_4.match_opponents())

        return first_round_matches

    def pairing_other_round(self, round_players):
        """Match creation of paired players for rounds others than the first one"""
        other_round_matches = []

        match_1 = match.Match(round_players[0], round_players[1])
        match_2 = match.Match(round_players[2], round_players[3])
        match_3 = match.Match(round_players[4], round_players[5])
        match_4 = match.Match(round_players[6], round_players[7])
        other_round_matches.append(match_1.match_opponents())
        other_round_matches.append(match_2.match_opponents())
        other_round_matches.append(match_3.match_opponents())
        other_round_matches.append(match_4.match_opponents())

        return other_round_matches
