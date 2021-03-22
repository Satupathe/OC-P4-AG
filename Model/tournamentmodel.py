#!/usr/bin/env python
# -*- coding: utf-8 -*-


""" Tournament class. 
Used to store tournament informations.
Keep informations available for the User
"""

from View import view
from Model import rounds, match
import json
from tinydb import TinyDB, Query, where 
from tinydb.operations import *
from operator import itemgetter


class TournamentModel:
    """Permet d'ajouter les données tournoi et joueurs et de sauvegarder en json"""
      
    
    def add_tournament_and_players(self, tournament_dict, players_list):
        """combine les infos tournoi et joueurs ensemble"""
        self.total_tournament = tournament_dict
        self.total_tournament["players"] = players_list
        return self.total_tournament

    """def get_match_list(self): # enlever cette fonction ? 
        self.played_matchs_list = []#décomposer par round !!!!!!
        return self.played_matchs_list#prendre dans le json ?


    def add_to_match_list(self, round_matches):
        self.played_matchs_list.append(round_matches) # enlever ces fonctions ?"""

    def json_save(self, tournament_dict):
        """sauvegarde les infos tournoi et joueur dans le json"""
        self.jtournament = TinyDB('jtournament.json',ensure_ascii=False, encoding='utf8', indent=4)
        self.tournament_table = self.jtournament.table('tournaments')
        self.tournament_table.insert(tournament_dict)
        
        return self.tournament_table #laisser en self ????

    def get_round_number(self, tournament_number):
        jtournament = TinyDB('jtournament.json',ensure_ascii=False, encoding='utf8', indent=4)
        tournament_table = jtournament.table('tournaments')

        tournament_id = None
        if tournament_number == 0:
            tournament_id = len(tournament_table)
        
        else:
            tournament_id = tournament_number

        round_number = tournament_table.get(doc_id=tournament_id)["Round number"]
        #print ("Round number else:", round_number)

        return round_number

    def get_length_db(self):
        jtournament = TinyDB('jtournament.json',ensure_ascii=False, encoding='utf8', indent=4)
        tournament_table = jtournament.table('tournaments')
        database_length = len(tournament_table)
        return database_length

    def get_players(self, tournament_number):
        jtournament = TinyDB('jtournament.json',ensure_ascii=False, encoding='utf8', indent=4)
        tournament_table = jtournament.table('tournaments')
        
        tournament_id = None
        if tournament_number == 0:
            tournament_id = len(tournament_table)
        
        else:
            tournament_id = tournament_number
        
        players = tournament_table.get(doc_id=tournament_id)["players"]

        return players

    def get_total_tournaments(self):
        jtournament = TinyDB('jtournament.json',ensure_ascii=False, encoding='utf8', indent=4)
        tournament_table = jtournament.table('tournaments')
        total_table = tournament_table.all()
        #print("total_table: ", total_table)
        all_tournaments = []
        
        for tournament in total_table:
            one_tournament = {}
            one_tournament["ID"] = tournament.doc_id
            one_tournament["Nom"] = tournament["Tournament's name"]
            one_tournament["Date"] = tournament["Tournament's Date"]
            one_tournament["Adresse"] = tournament["Tournament's adress"]
            all_tournaments.append(one_tournament)

        #print("all_tournaments", all_tournaments)
        return all_tournaments

    def get_unfinished_tournaments(self):
        jtournament = TinyDB('jtournament.json',ensure_ascii=False, encoding='utf8', indent=4)
        tournament_table = jtournament.table('tournaments')
        total_table = tournament_table.search(Query()["Round number"] != 4)
        #print("total_table: ", total_table)
        all_tournaments = []
        
        for tournament in total_table:
            one_tournament = {}
            one_tournament["ID"] = tournament.doc_id
            one_tournament["Nom"] = tournament["Tournament's name"]
            one_tournament["Date"] = tournament["Tournament's Date"]
            one_tournament["Adresse"] = tournament["Tournament's adress"]
            all_tournaments.append(one_tournament)

        #print("all_tournaments", all_tournaments)
        return all_tournaments

    def sorted_score_1T(self, tournament_id):
        jtournament = TinyDB('jtournament.json',ensure_ascii=False, encoding='utf8', indent=4)
        tournament_table = jtournament.table('tournaments')
        tid = int(tournament_id)   
        players_table = tournament_table.get(doc_id=tid)["players"]
        #print("players_table: ", players_table)
        sorted_list = []
      
        score = 4.0
        while len(sorted_list)< 8: # permet de classer par score et par rank
            by_score = []
            for player in players_table:
                if player["Score"] == score:
                    by_score.append(player)
            by_score.sort(key=itemgetter("Rank"), reverse=False)
            #print("by score", by_score)
            for item in by_score:
                sorted_list.append(item)
            score -= 0.5

        #print(sorted_list)
        return sorted_list
    

    def sorted_name_1T(self, tournament_id):
        jtournament = TinyDB('jtournament.json',ensure_ascii=False, encoding='utf8', indent=4)
        tournament_table = jtournament.table('tournaments')
        tid = int(tournament_id)   
        
        players_table = tournament_table.get(doc_id=tid)["players"]
        sorted_players_table = sorted(players_table, key=itemgetter("Family name"), reverse=False)

        return sorted_players_table
     
    def sorted_rounds_1T(self, tournament_id):#finir la mise en forme de l'affichage des rounds
        jtournament = TinyDB('jtournament.json',ensure_ascii=False, encoding='utf8', indent=4)
        tournament_table = jtournament.table('tournaments')
        tid = int(tournament_id)   

        rounds_table = tournament_table.get(doc_id=tid)["Rounds"]
        #print("rounds_table: ", rounds_table)
        rounds_list = []
        for one_round in rounds_table:
            rounds_list.append(rounds_table[one_round])

        #print("round list: ", rounds_list)
        return rounds_list

    def sorted_matches_1T(self, tournament_id):
        jtournament = TinyDB('jtournament.json',ensure_ascii=False, encoding='utf8', indent=4)
        tournament_table = jtournament.table('tournaments')
        tid = int(tournament_id)   

        rounds_table = tournament_table.get(doc_id=tid)["Rounds"]
        matchs_list = []
        for one_round in rounds_table:
            for i in range(4):# définir en fonction du nombre de rounds déja passés (sinon erreur avec tournoi inachevé)
                one_match = rounds_table[one_round][2][i][0], rounds_table[one_round][2][i][1] 
                matchs_list.append(one_match)

        return matchs_list

    def total_players_name(self):
        jtournament = TinyDB('jtournament.json',ensure_ascii=False, encoding='utf8', indent=4)
        tournament_table = jtournament.table('tournaments')
        name = Query()
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
        jtournament = TinyDB('jtournament.json',ensure_ascii=False, encoding='utf8', indent=4)
        tournament_table = jtournament.table('tournaments')
        name = Query()
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
        jtournament = TinyDB('jtournament.json',ensure_ascii=False, encoding='utf8', indent=4)
        tournament_table = jtournament.table('tournaments')
        total_table = tournament_table.all()  
        
        #récupérer le doc_id
        #s'en servir pour l'enregistrement

        for player in new_rank_players:
            identification_1 = f'{player["Family name"]} {player["First name"]} {player["Birthdate"]}'
            print("identification 1", identification_1)

            for tournament in total_table:
                tournament_id = tournament.doc_id
                table_id = tournament_id - 1
                
                for list_player in tournament["players"]:
                    identification_2 = f'{list_player["Family name"]} {list_player["First name"]} {list_player["Birthdate"]}'
                    print("identification 2", identification_2)
                
                    if identification_1 == identification_2:
                        list_player["Rank"] = int(player["Rank"])
                        
                    else:
                        pass

                tournament_table.update(total_table[table_id], doc_ids=[tournament_id])

    def json_score_opponent_player(self, players_and_score, matchs_round, tournament_number, round_nb, start, end):
        jtournament = TinyDB('jtournament.json',ensure_ascii=False, encoding='utf8', indent=4)
        tournament_table = jtournament.table('tournaments')        
        tournament_id = None
        
        
        if tournament_number == 0:
            tournament_id = len(tournament_table)
        else:
            tournament_id = tournament_number
    
        round_number = tournament_table.get(doc_id=tournament_id)["Round number"] # à garder ? 
        round_number = 1
        dict_round_number = {"Round number": round_number}
        print("dict_round_number:", dict_round_number)
        tournament_table.update(add("Round number", round_number), doc_ids=[tournament_id])
        print( "vérif mid enregistrement round number", tournament_table.get(doc_id=tournament_id)["Round number"])
        print("")
        print("players_and_score:  ", players_and_score)
        sorted_players = sorted(players_and_score, key=lambda x: x[2], reverse=False) # par pairing number ? 
        print("")
        print("tournamentmodel sorted_players: ", sorted_players, "par pairing number")
        print("")
        
        self.players = tournament_table.get(doc_id=tournament_id)["players"] # par pairing number
        print("matchs_round: ", matchs_round, "par match")
        print("")


        #Mettre dans une autre fonction ?
        saved_rounds = tournament_table.get(doc_id=tournament_id)["Rounds"]
        print("one round 1: ", saved_rounds)
        print('')
        round_id = "Round number " + str(round_nb)
        round_infos = [start, end, matchs_round]
        saved_rounds[round_id] = round_infos
        print("one round 2: ", saved_rounds)
        print('')
        tournament_table.update(set("Rounds", saved_rounds), doc_ids=[tournament_id])

        opponents_ids = {}

        for i in range(4): #ajouter  le rank à partir des listes fournies.
            opponents_ids[matchs_round[i][0][2]] = matchs_round[i][1][2]
            opponents_ids[matchs_round[i][1][2]] = matchs_round[i][0][2]
        
        print("opponents_ids: ", opponents_ids)
        print("")
        self.sorted_opponent = sorted(opponents_ids.items(), reverse=False)
        print("self.sorted_opponent: ", self.sorted_opponent, "by Pairing number")
        print("")

        j = 0
        for i in sorted_players:
            self.players[j]["Score"] = i[3]
            j += 1
        
        k = 0
        for i in self.sorted_opponent:
            self.players[k]["Opponents"].append(i[1])
            k += 1

        dict_player = {"players": self.players}
        print("dict_player:  ", dict_player)
        tournament_table.update(dict_player, doc_ids=[tournament_id])

        print( "vérif fin enregistrement round number", tournament_table.get(doc_id=tournament_id)["Round number"])

    def get_previous_round_list(self, tournament_number): #appeler pairing ?
        jtournament = TinyDB('jtournament.json',ensure_ascii=False, encoding='utf8', indent=4)
        tournament_table = jtournament.table('tournaments')
        
        tournament_id = None
        if tournament_number == 0:
            tournament_id = len(tournament_table)

        else:
            tournament_id = tournament_number

        players = tournament_table.get(doc_id=tournament_id)["players"]
        
        sorted_players = sorted(players, key=itemgetter("Score"), reverse=True)
        print('')
        print("get previous players : sorted_players: ", sorted_players, "sorted by score")
        print("")
        print("checkpoint 1")
        print('')

        sorted_list = []
        round_matchs_list = []
        round_match_players = []
        score = 4.0
        while len(sorted_list)< 8: # permet de classer par score et par rank
            by_score = []
            for player in sorted_players:
                if player["Score"] == score:
                    by_score.append(player)
            by_score.sort(key=itemgetter("Rank"), reverse=False)
            for item in by_score:
                sorted_list.append(item)
            score -= 0.5
        
        print("sorted list by score and rank", sorted_list)
        print("checkpoint 1")
        
        already_took_players = [0] 
        
        for player in sorted_list:
            print("player = ", player)
            pairing_number = int(player["Pairing number"])
            print("pairing_number:", pairing_number)
            next_opponent = None
            opponent = None
            if len(already_took_players) != 9:         

                if pairing_number not in already_took_players:
                    already_took_players.append(int(pairing_number))
                    round_match_players.append(pairing_number)

                    for other_player in sorted_list:
                        if int(other_player["Pairing number"]) not in already_took_players:
                            if pairing_number not in other_player["Opponents"]:
                                opponent = other_player["Pairing number"]
                                print("opponent: ", opponent)
                                already_took_players.append(int(opponent))
                                round_match_players.append(int(opponent))
                                round_matchs_list.append((pairing_number, int(opponent)))
                                break

                            else:
                                print("pairing number in other_player opponent")
                                pass
                        else:
                            print("other player pairing number in already_took player")
                            pass
                else:
                    print("pairing number in already_took_player")
                    pass
            else:
                print("longueur already took player == 9")
                break

            print("checkpoint 2")
            print("already_took_players early", already_took_players)
            print("round_matchs_list: ", round_matchs_list)
            print("round_match_players: ",round_match_players)
        
        results = []
        for j in range (8):
            for player in sorted_players:
                if int(player["Pairing number"]) == round_match_players[j]:
                    results.append(player)
                else:
                    pass    
        
        #print("results: ", results)
        return results  
