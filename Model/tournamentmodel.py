#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tournament model:
Used to import and export tournament informations in json
Keep informations available for the User
Functions to retreive informations on rounds, players tournament...
Pairing function with data from previous round
"""

from tinydb import TinyDB, Query
from tinydb.operations import add, set
from operator import itemgetter


class TournamentModel:
    """Class with all functions to save and retreive informations in json file plus pairing function"""

    def add_tournament_and_players(self, tournament_dict, players_list):
        """Combine tournament and players informations"""
        self.total_tournament = tournament_dict
        self.total_tournament["players"] = players_list
        return self.total_tournament

    def json_save(self, tournament_dict):
        """save early tournament and players informations in json"""
        jtournament = TinyDB("jtournament.json", ensure_ascii=False, encoding="utf8", indent=4)
        tournament_table = jtournament.table("tournaments")
        tournament_table.insert(tournament_dict)
        return tournament_table

    def get_round_number(self, tournament_number):
        """Get the actuel round number of a tournament with the entry number in json(tournament id)"""
        jtournament = TinyDB("jtournament.json", ensure_ascii=False, encoding="utf8", indent=4)
        tournament_table = jtournament.table("tournaments")
        tournament_id = None

        if tournament_number == 0:
            tournament_id = len(tournament_table)
        else:
            tournament_id = tournament_number

        round_number = tournament_table.get(doc_id=tournament_id)["Round number"]
        return round_number

    def get_length_db(self):
        """get the number of entry in the json database"""
        jtournament = TinyDB("jtournament.json", ensure_ascii=False, encoding="utf8", indent=4)
        tournament_table = jtournament.table("tournaments")
        database_length = len(tournament_table)
        return database_length

    def get_players(self, tournament_number):
        """get all the players of a tournament by it's id"""
        jtournament = TinyDB("jtournament.json", ensure_ascii=False, encoding="utf8", indent=4)
        tournament_table = jtournament.table("tournaments")
        tournament_id = None

        if tournament_number == 0:
            tournament_id = len(tournament_table)
        else:
            tournament_id = tournament_number

        players = tournament_table.get(doc_id=tournament_id)["players"]
        return players

    def get_total_tournaments(self):
        """get all the saved tournament in the json database"""
        jtournament = TinyDB("jtournament.json", ensure_ascii=False, encoding="utf8", indent=4)
        tournament_table = jtournament.table("tournaments")
        total_table = tournament_table.all()
        all_tournaments = []

        for tournament in total_table:
            one_tournament = {}
            one_tournament["ID"] = tournament.doc_id
            one_tournament["Nom"] = tournament["Tournament's name"]
            one_tournament["Date"] = tournament["Tournament's Date"]
            one_tournament["Adresse"] = tournament["Tournament's adress"]
            all_tournaments.append(one_tournament)

        return all_tournaments

    def get_unfinished_tournaments(self):
        """Get all unfinished tournament in json database"""
        jtournament = TinyDB("jtournament.json", ensure_ascii=False, encoding="utf8", indent=4)
        tournament_table = jtournament.table("tournaments")
        total_table = tournament_table.search(Query()["Round number"] != 4)
        all_tournaments = []

        for tournament in total_table:
            one_tournament = {}
            one_tournament["ID"] = tournament.doc_id
            one_tournament["Nom"] = tournament["Tournament's name"]
            one_tournament["Date"] = tournament["Tournament's Date"]
            one_tournament["Adresse"] = tournament["Tournament's adress"]
            all_tournaments.append(one_tournament)

        return all_tournaments

    def sorted_score_1T(self, tournament_id):
        """Get players sorted by score for one tournament"""
        jtournament = TinyDB("jtournament.json", ensure_ascii=False, encoding="utf8", indent=4)
        tournament_table = jtournament.table("tournaments")
        tid = int(tournament_id)
        players_table = tournament_table.get(doc_id=tid)["players"]
        sorted_list = []

        score = 4.0
        while len(sorted_list) < 8:
            by_score = []
            for player in players_table:
                if player["Score"] == score:
                    by_score.append(player)
            by_score.sort(key=itemgetter("Rank"), reverse=False)
            for item in by_score:
                sorted_list.append(item)
            score -= 0.5

        return sorted_list

    def sorted_name_1T(self, tournament_id):
        """Get players sorted by name for one tournament"""
        jtournament = TinyDB("jtournament.json", ensure_ascii=False, encoding="utf8", indent=4)
        tournament_table = jtournament.table("tournaments")
        tid = int(tournament_id)

        players_table = tournament_table.get(doc_id=tid)["players"]
        sorted_players_table = sorted(players_table, key=itemgetter("Family name"), reverse=False)

        return sorted_players_table

    def sorted_rounds_1T(self, tournament_id):
        """Get all rounds for one tournament"""
        jtournament = TinyDB("jtournament.json", ensure_ascii=False, encoding="utf8", indent=4)
        tournament_table = jtournament.table("tournaments")
        tid = int(tournament_id)

        rounds_table = tournament_table.get(doc_id=tid)["Rounds"]
        rounds_list = []
        for one_round in rounds_table:
            rounds_list.append(rounds_table[one_round])

        return rounds_list

    def sorted_matches_1T(self, tournament_id):
        """Get all matchs for one tournament"""
        jtournament = TinyDB("jtournament.json", ensure_ascii=False, encoding="utf8", indent=4)
        tournament_table = jtournament.table("tournaments")
        tid = int(tournament_id)

        rounds_table = tournament_table.get(doc_id=tid)["Rounds"]
        matchs_list = []
        for one_round in rounds_table:
            for i in range(4):
                one_match = rounds_table[one_round][2][i][0], rounds_table[one_round][2][i][1]
                matchs_list.append(one_match)

        return matchs_list

    def total_players_name(self):
        """Get all saved players in the json database sorted by name"""
        jtournament = TinyDB("jtournament.json", ensure_ascii=False, encoding="utf8", indent=4)
        tournament_table = jtournament.table("tournaments")
        total_table = tournament_table.all()
        final_name_players = []

        for element in total_table:
            for player in element["players"]:
                polished_player = {}
                polished_player["Family name"] = player["Family name"]
                polished_player["First name"] = player["First name"]
                polished_player["Birthdate"] = player["Birthdate"]
                polished_player["Gender"] = player["Gender"]
                polished_player["Rank"] = player["Rank"]

                if polished_player in final_name_players:
                    pass
                else:
                    final_name_players.append(polished_player)

        final_name_players.sort(key=itemgetter("Family name"), reverse=False)

        return final_name_players

    def total_players_actual_rank(self):
        """Get all saved players in the json database sorted by rank"""
        jtournament = TinyDB("jtournament.json", ensure_ascii=False, encoding="utf8", indent=4)
        tournament_table = jtournament.table("tournaments")
        total_table = tournament_table.all()
        final_name_players = []

        for element in total_table:
            for player in element["players"]:
                polished_player = {}
                polished_player["Family name"] = player["Family name"]
                polished_player["First name"] = player["First name"]
                polished_player["Birthdate"] = player["Birthdate"]
                polished_player["Gender"] = player["Gender"]
                polished_player["Rank"] = player["Rank"]

                if polished_player in final_name_players:
                    pass
                else:
                    final_name_players.append(polished_player)

        final_name_players.sort(key=itemgetter("Rank"), reverse=False)

        return final_name_players

    def save_new_ranks(self, new_rank_players):
        """Save new players's ranks in the database"""
        jtournament = TinyDB("jtournament.json", ensure_ascii=False, encoding="utf8", indent=4)
        tournament_table = jtournament.table("tournaments")
        total_table = tournament_table.all()

        for player in new_rank_players:
            identification_1 = f'{player["Family name"]} {player["First name"]} {player["Birthdate"]}'
            for tournament in total_table:
                tournament_id = tournament.doc_id
                table_id = tournament_id - 1
                for list_player in tournament["players"]:
                    identification_2 = (
                        f'{list_player["Family name"]} {list_player["First name"]} {list_player["Birthdate"]}'
                    )

                    if identification_1 == identification_2:
                        list_player["Rank"] = int(player["Rank"])
                    else:
                        pass

                tournament_table.update(total_table[table_id], doc_ids=[tournament_id])

    def json_score_opponent_player(self, players_and_score, matchs_round, tournament_number, round_nb, start, end):
        """
        Save last round informations in the jason database:
        save opponents, score, round number, rounds
        """
        jtournament = TinyDB("jtournament.json", ensure_ascii=False, encoding="utf8", indent=4)
        tournament_table = jtournament.table("tournaments")
        tournament_id = None

        if tournament_number == 0:
            tournament_id = len(tournament_table)
        else:
            tournament_id = tournament_number

        round_number = tournament_table.get(doc_id=tournament_id)["Round number"]
        round_number = 1
        tournament_table.update(add("Round number", round_number), doc_ids=[tournament_id])
        sorted_players = sorted(players_and_score, key=lambda x: x[2], reverse=False)

        self.players = tournament_table.get(doc_id=tournament_id)["players"]

        saved_rounds = tournament_table.get(doc_id=tournament_id)["Rounds"]
        round_id = "Round number " + str(round_nb)
        round_infos = [start, end, matchs_round]
        saved_rounds[round_id] = round_infos
        tournament_table.update(set("Rounds", saved_rounds), doc_ids=[tournament_id])

        opponents_ids = {}
        for i in range(4):
            opponents_ids[matchs_round[i][0][2]] = matchs_round[i][1][2]
            opponents_ids[matchs_round[i][1][2]] = matchs_round[i][0][2]

        self.sorted_opponent = sorted(opponents_ids.items(), reverse=False)

        j = 0
        for i in sorted_players:
            self.players[j]["Score"] = i[3]
            j += 1

        k = 0
        for i in self.sorted_opponent:
            self.players[k]["Opponents"].append(i[1])
            k += 1

        dict_player = {"players": self.players}
        tournament_table.update(dict_player, doc_ids=[tournament_id])

    def get_previous_round_list(self, tournament_number):
        """
        Get previous opponent and score informations
        pairing algorithm to put opponents against each others
        """
        jtournament = TinyDB("jtournament.json", ensure_ascii=False, encoding="utf8", indent=4)
        tournament_table = jtournament.table("tournaments")
        tournament_id = None
        if tournament_number == 0:
            tournament_id = len(tournament_table)
        else:
            tournament_id = tournament_number

        players = tournament_table.get(doc_id=tournament_id)["players"]
        sorted_players = sorted(players, key=itemgetter("Score"), reverse=True)

        sorted_list = []
        round_matchs_list = []
        round_match_players = []
        score = 4.0
        while len(sorted_list) < 8:
            by_score = []
            for player in sorted_players:
                if player["Score"] == score:
                    by_score.append(player)
            by_score.sort(key=itemgetter("Rank"), reverse=False)
            for item in by_score:
                sorted_list.append(item)
            score -= 0.5

        already_took_players = [0]

        for player in sorted_list:
            pairing_number = int(player["Pairing number"])
            opponent = None
            if len(already_took_players) != 9:

                if pairing_number not in already_took_players:
                    already_took_players.append(int(pairing_number))
                    round_match_players.append(pairing_number)

                    for other_player in sorted_list:
                        if int(other_player["Pairing number"]) not in already_took_players:
                            if pairing_number not in other_player["Opponents"]:
                                opponent = other_player["Pairing number"]
                                already_took_players.append(int(opponent))
                                round_match_players.append(int(opponent))
                                round_matchs_list.append((pairing_number, int(opponent)))
                                break
                            else:
                                pass
                        else:
                            pass
                else:
                    pass
            else:
                break

        results = []
        for j in range(8):
            for player in sorted_players:
                if int(player["Pairing number"]) == round_match_players[j]:
                    results.append(player)
                else:
                    pass

        return results
