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
from tinydb.operations import delete
from operator import itemgetter


class TournamentModel:
    """Permet d'ajouter les données tournoi et joueurs et de sauvegarder en json"""
      
    
    def add_tournament_and_players(self, tournament_dict, players_list):
        """combine les infos tournoi et joueurs ensemble"""
        self.total_tournament = tournament_dict
        self.total_tournament["players"] = players_list
        return self.total_tournament

    def get_match_list(self):
        self.played_matchs_list = []#décomposer par round !!!!!!
        return self.played_matchs_list#prendre dans le json ?


    def add_to_match_list(self, round_matches):
        self.played_matchs_list.append(round_matches)

    def json_save(self, tournament_dict):
        """sauvegarde les infos tournoi et joueur dans le json"""
        self.jtournament = TinyDB('jtournament.json',ensure_ascii=False, encoding='utf8', indent=4)
        self.tournament_table = self.jtournament.table('tournaments')
        self.tournament_table.insert(tournament_dict)
                
        """self.jtournament.update({"Score":i}, all()[j])
        print(self.jtournament.get(_default[1]["Tournament's name"]))
        print(self.jtournament.get("_default"[:2]["players"][0]["Score"]))
        self.jtournament.update({"2": "chocolat"})
        self.jtournament.update(delete("3"))"""
        """self.jtournament.update(increment("1"["players"][0], 14))"""
        """with open ('tournament.json', 'a', encoding='utf8') as tour:
            json.dump(tournament_dict, tour, ensure_ascii=False, indent = 4)"""
        return self.tournament_table

    def json_score_opponent_player(self, players_and_score, matchs_round):
        #télécharger le json en vue de faire des modifications dessus
        """self.jtournament = TinyDB('jtournament.json',ensure_ascii=False, encoding='utf8', indent=4)"""
        """tournament_table = self.jtournament.table('tournaments')"""
        jtournament = TinyDB('jtournament.json',ensure_ascii=False, encoding='utf8', indent=4)
        tournament_table = jtournament.table('tournaments')

        last = len(tournament_table) #Ok
        sorted_players = sorted(players_and_score, key=lambda x: x[1], reverse=False) 
        self.players = tournament_table.get(doc_id=last)["players"]
        
        opponents_ids = {}
        j = 0
        for i in range(4): 
            key1 = matchs_round[i][0][1] 
            key2 = matchs_round[i][1][1] 
            value1 = matchs_round[i][1][1]
            value2 = matchs_round[i][0][1]
            opponents_ids[key1] = value1
            opponents_ids[key2] = value2

        self.sorted_opponent = sorted(opponents_ids.items(), reverse=False)

        j = 0
        for i in sorted_players:
            self.players[j]["Score"] += i[2]
            j += 1
        
        k = 0
        for i in self.sorted_opponent:
            self.players[k]["Opponents"].append(i[1])
            k += 1

        dict_player = {"players": self.players}
        tournament_table.update(dict_player, doc_ids=[last])


    def get_previous_round_list(self):
        jtournament = TinyDB('jtournament.json',ensure_ascii=False, encoding='utf8', indent=4)
        tournament_table = jtournament.table('tournaments')
        #récupérer les scores du round précédent
        last = len(tournament_table)
        players = tournament_table.get(doc_id=last)["players"]
        
        sorted_players = sorted(players, key=itemgetter("Score"), reverse=True)
        print('')
        print(sorted_players)
        print("checkpoint 1")
        print('')

        already_took_opponent = [0]
          
        matchs_list = []
        matchs = []
        for player in sorted_players:
            print(player)
            opponent_possibilities = []# rangés en focntion des scores
            pairing_number = int(player["Pairing number"]) # id du joueur ici 1
            next_opponent = None
            print("pairing_number:", pairing_number)
            
            AD = None
            
            for i in already_took_opponent:
                if pairing_number == i:
                    AD =  None
                    print("AD if:", AD)
                    break
                else:
                    AD = pairing_number
                    print("AD else:", AD)
            print("checkpoint 2")
            
            if AD is not None:
                print("je selectionne les anciens adversaires 1")
                already_took_opponent.append(pairing_number)    

                for opponent in sorted_players: #comparaison avec l'ensemble des joueurs
                    provisional_number = None
                    for j in opponent["Opponents"]: # comparaison avec la liste des ancien adversaires
                        
                        if j == pairing_number:
                            provisional_number = None # des choses qui ne vont pas!!
                            break
                        else:
                            provisional_number = opponent["Pairing number"]
                    
                    if provisional_number is not None:
                        opponent_possibilities.append(provisional_number)
                    else:
                        pass
                
                for i in opponent_possibilities:
                    provisional_opponent = None
                    
                    for j in already_took_opponent:
                       
                        if j == i:
                            provisional_opponent = None
                            print("possibilities break")
                            break

                        else:
                            provisional_opponent = i
                    print("provisional_opponent:", provisional_opponent)

                if provisional_opponent is not None:
                    next_opponent = provisional_opponent
                    already_took_opponent.append(provisional_opponent)
                else:
                    pass
            else:
                pass
        
            print("checkpoint 3")
            print("already_took_opponent", already_took_opponent)
            print("opponent_possibilities", opponent_possibilities)
            print('')

        for i in range(0, 8, 2):
            j = i+1
            playerinfos_i = tournament_table.get(doc_id=last)["players"].Query().Pairing_number == matchs[i]
                                                    #get(query().Pairing_number == matchs[i] in (doc_id=last))
            playerinfos_j = tournament_table.get(doc_id=last)["players"].Query().Pairing_number == matchs[j]
                                                    #get(query().Pairing_number == matchs[i+1] in (doc_id=last)) 
            player_1 = player.Player(playerinfos_i)
            player_2 = player.Player(playerinfos_j)

            matchplayer1 = player_1.match_player
            matchplayer2 = player_2.match_player
            
            one_match = match.Match(matchplayer1, matchplayer2)
            match = one_match.match_opponents
            matchs_list.append(match)

        print(matchs_list)
        return matchs_list
                #Comparer avec la liste des joueurs pris ce round   OK
                #si déjà pris prendre la possibilité de joueur suivante   OK
                #Comparer cette nouvelle possibilité avec la liste des joueurs pris   OK
                #etc...
                #si free ajouter ces joueurs à une instance de match [([j1,s1], [j2,s2])]
                #renvoyer la liste des matchs vers le controller
                #demander les résultats
                #les enregistrer
                #HOP un nouveau round!!
                #sortir les résultats de tous les rounds.



    
        """print(self.played_matchs_list)"""      

    """def matchs_creations(self):
        for i in range(4):
            self.one_round.match_creation() # mettre dans tController ou roundsmodel?

#doit appeler plusieurs round

#creation d'un objet round 1 si liste vide"""

""" 
créer un tournoi
dans le tournoi créer un premier round"""
