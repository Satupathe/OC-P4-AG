"""
Match class:
Used to create matches
"""


class Match:
    """combine to players to make a match"""
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def match_opponents(self):
        match = (self.player_1, self.player_2)
        return match
