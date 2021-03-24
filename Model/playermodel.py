"""
Player class
Used to initialize players.
Keep usefull informations.
return player with name, first name, rank, pairing number and score
"""


class Player:
    """initialize player and kepp selected informations"""
    def __init__(self, one_player_infos):
        """initialise one player"""
        self.name = one_player_infos["Family name"]
        self.first_name = one_player_infos["First name"]
        self.birth = one_player_infos["Birthdate"]
        self.gender = one_player_infos["Gender"]
        self.ranking = one_player_infos["Rank"]
        self.pairing_nb = one_player_infos["Pairing number"]
        self.score = one_player_infos["Score"]
        self.opponents = one_player_infos["Opponents"]

    def match_player(self):
        """Keep useful informations for on player"""
        match_player = [f"{self.name} {self.first_name} (Rank, Pairing number, Score): ",
                        int(self.ranking), int(self.pairing_nb), float(self.score)
                        ]

        return match_player
