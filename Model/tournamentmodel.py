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

    def get_match_list(self): # enlever cette fonction ? 
        self.played_matchs_list = []#décomposer par round !!!!!!
        return self.played_matchs_list#prendre dans le json ?


    def add_to_match_list(self, round_matches):
        self.played_matchs_list.append(round_matches) # enlever ces fonctions ?

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

    def json_score_opponent_player(self, players_and_score, matchs_round, tournament_number):
        #télécharger le json en vue de faire des modifications dessus
        """self.jtournament = TinyDB('jtournament.json',ensure_ascii=False, encoding='utf8', indent=4)"""
        """tournament_table = self.jtournament.table('tournaments')"""
        jtournament = TinyDB('jtournament.json',ensure_ascii=False, encoding='utf8', indent=4)
        tournament_table = jtournament.table('tournaments')
        #print("players_and_score:", players_and_score)
        
        tournament_id = None
        if tournament_number == 0:
            tournament_id = len(tournament_table)

        else:
            tournament_id = tournament_number
    

        round_number = tournament_table.get(doc_id=tournament_id)["Round number"]
        #print ("Round number:", round_number)
        round_number = 1
        dict_round_number = {"Round number": round_number}
        #print("dict_round_number:", dict_round_number)
        tournament_table.update(add("Round number", round_number), doc_ids=[tournament_id])
        #print( "vérif mid enregistrement round number", tournament_table.get(doc_id=tournament_id)["Round number"])
        
        sorted_players = sorted(players_and_score, key=lambda x: x[1], reverse=False)
        """print("")
        print("tournamentmodel sorted_players: ", sorted_players, "par rank")
        print("")"""
        
        self.players = tournament_table.get(doc_id=tournament_id)["players"]
        """print("matchs_round: ", matchs_round, "par match")
        print("")"""
        


        opponents_ids = {}

        for i in range(4): 
            id_and_opponent1 = []
            id_and_opponent2 = []
            key1 = matchs_round[i][0][1] 
            key2 = matchs_round[i][1][1] 
            id_and_opponent1.append(matchs_round[i][0][2]) 
            id_and_opponent2.append(matchs_round[i][1][2])
            id_and_opponent1.append(matchs_round[i][1][2])
            id_and_opponent2.append(matchs_round[i][0][2])
            opponents_ids[key1] = id_and_opponent1
            opponents_ids[key2] = id_and_opponent2
       
        """print("opponents_ids: ", opponents_ids)
        print("")"""
        self.sorted_opponent = sorted(opponents_ids.items(), reverse=False)
        """print("self.sorted_opponent: ", self.sorted_opponent, "by rank")
        print("")"""

        j = 0
        for i in sorted_players:
            self.players[j]["Score"] = i[3]
            j += 1
        
        k = 0
        for i in self.sorted_opponent:
            self.players[k]["Opponents"].append(i[1][1])
            k += 1

        dict_player = {"players": self.players}
        #print(dict_player)
        tournament_table.update(dict_player, doc_ids=[tournament_id])

        #print( "vérif fin enregistrement round number", tournament_table.get(doc_id=tournament_id)["Round number"])

    def get_previous_round_list(self, tournament_number): #appeler pairing ?
        jtournament = TinyDB('jtournament.json',ensure_ascii=False, encoding='utf8', indent=4)
        tournament_table = jtournament.table('tournaments')
        #récupérer les scores du round précédent
        
        tournament_id = None
        if tournament_number == 0:
            tournament_id = len(tournament_table)

        else:
            tournament_id = tournament_number

        #print("tournament_id: ", tournament_id)

        players = tournament_table.get(doc_id=tournament_id)["players"]
        
        sorted_players = sorted(players, key=itemgetter("Score"), reverse=True)
        """print('')
        print("get previous players : sorted_players: ", sorted_players, "sorted by score")
        print("checkpoint 1")
        print('')"""

        sorted_list = []
        round_matchs_list = []
        round_match_players = []
        score = 4.0
        while len(sorted_list)< 8: # permet de classer par score et par rank
            by_score = []
            for player in sorted_players:
                if player["Score"] == score:
                    by_score.append(player)
            by_score.sort(key=itemgetter("Player's rank:"), reverse=False)
            for item in by_score:
                sorted_list.append(item)
            score -= 0.5
        
        """print("sorted list by score and rank", sorted_list)
        print("checkpoint 1")
        """
        already_took_players = [0] 

        
        for player in sorted_list:
            #print("player = ", player)
            pairing_number = int(player["Pairing number"])
            #print("pairing_number:", pairing_number)
            next_opponent = None
            opponent = None
            if len(already_took_players) != 9:         

                if pairing_number not in already_took_players:
                    already_took_players.append(pairing_number)
                    round_match_players.append(pairing_number)

                    for other_player in sorted_list:
                        if int(other_player["Pairing number"]) not in already_took_players:
                            if pairing_number not in other_player["Opponents"]:
                                opponent = other_player["Pairing number"]
                                #print("opponent: ", opponent)
                                already_took_players.append(int(opponent))
                                round_match_players.append(int(opponent))
                                round_matchs_list.append((pairing_number, int(opponent)))
                                break

                            else:
                                #print("pairing number in other_player opponent")
                                pass
                        else:
                            #print("other player pairing number in already_took player")
                            pass
                else:
                    #print("pairing number in already_took_player")
                    pass
            else:
                #print("longueur already took player == 9")
                break

            
            """print("checkpoint 2")
            print("already_took_players early", already_took_players)
            print("round_matchs_list: ", round_matchs_list)
            print("round_match_players: ",round_match_players)"""
        
        results = []
        for j in range (8):
            for player in sorted_players:
                if int(player["Pairing number"]) == round_match_players[j]:
                    results.append(player)
                else:
                    pass    
        


        """print("results: ", results)"""
        return results  

#doit appeler plusieurs round

#creation d'un objet round 1 si liste vide"""

""" 
créer un tournoi
dans le tournoi créer un premier round"""

         
           
#if provisional_opponent is not 0: