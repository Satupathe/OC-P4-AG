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
        
        return self.tournament_table #laisser en self ????

    def json_score_opponent_player(self, players_and_score, matchs_round):
        #télécharger le json en vue de faire des modifications dessus
        """self.jtournament = TinyDB('jtournament.json',ensure_ascii=False, encoding='utf8', indent=4)"""
        """tournament_table = self.jtournament.table('tournaments')"""
        jtournament = TinyDB('jtournament.json',ensure_ascii=False, encoding='utf8', indent=4)
        tournament_table = jtournament.table('tournaments')

        last = len(tournament_table) #Ok
        sorted_players = sorted(players_and_score, key=lambda x: x[1], reverse=False)
        """print("")
        print("tournamentmodel sorted_players: ", sorted_players, "par rank")
        print("") """
        self.players = tournament_table.get(doc_id=last)["players"]
        """print("matchs_round: ", matchs_round)
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
        """print("self.sorted_opponent: ", self.sorted_opponent) # sorted by rank
        print("")"""

        j = 0
        for i in sorted_players:
            self.players[j]["Score"] += i[3]
            j += 1
        
        k = 0
        for i in self.sorted_opponent:
            self.players[k]["Opponents"].append(i[1][0])
            self.players[k]["Opponents"].append(i[1][1])
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
        print("get previous players : sorted_players: ", sorted_players, "sorted by score")
        print("checkpoint 1")
        print('')

        already_took_opponent = [0]
          
        round_matchs_list = []
        
        for player in sorted_players:
            print(player)
            opponent_possibilities = []# rangés en focntion des scores
            pairing_number = int(player["Pairing number"]) #ici 6
            next_opponent = None
            print("pairing_number:", pairing_number)
            
            AD = None
            
            for i in already_took_opponent:
                if pairing_number is i:
                    AD =  None
                    print("AD if:", AD)
                    break
                else:
                    AD = pairing_number
            #print(AD)
            print("checkpoint 2")
            print("already_took_opponent early", already_took_opponent)
            
            if AD is not None: #le décaler dans la boucle précédente?
                print("je selectionne les adversaires potentiels 1")
                already_took_opponent.append(pairing_number)    
                print("already_took_opponent medium", already_took_opponent)

                for opponent in sorted_players: #comparaison avec l'ensemble des joueurs
                    provisional_number = None
                    for j in opponent["Opponents"]: # comparaison avec la liste des ancien adversaires

                        if j is pairing_number:
                            provisional_number = None # des choses qui ne vont pas!!
                            #print("provisional_number if: ", provisional_number)
                            break
                        else:
                            provisional_number = opponent["Pairing number"]
                            #print("provisional_number else: ", provisional_number)

                    if provisional_number is not None:
                        #print("already_took_opponent medium 2: ", already_took_opponent)
                        opponent_possibilities.append(int(provisional_number))
                    else:
                        pass
                #print("opponent_possibilities medium 1", opponent_possibilities)

                opponent_supression = []
                s = set(already_took_opponent)
                for i in opponent_possibilities:
                    if i not in s:
                        opponent_supression.append(i)
                        #print("add possibility")
                        break                            
                    
                    else:
                        #print("took = possibility")
                        pass

                #print("opponent_supression: ", opponent_supression)
                #print("opponent_possibilities intermediaire", opponent_possibilities)
                next_opponent = opponent_supression[0]
                already_took_opponent.append(int(next_opponent))
                match = (pairing_number, next_opponent)
                print(match)
                round_matchs_list.append(match)


            else:
                pass
        
            print("checkpoint 3")
            
            #print("opponent_possibilities", opponent_possibilities)
            #print("next opponent", next_opponent)
            #print("already_took_opponent late", already_took_opponent)
            print('')
        print("round_matchs_list: ", round_matchs_list)

        ids_list = []
        for i in range (4):
            Matchs_player_ids = []
            ids_list.append(round_matchs_list[i][0])
            ids_list.append(round_matchs_list[i][1])
        print(ids_list)
        print(type(ids_list[4]))
        
        results = []
        for j in range (8):
            for player in sorted_players:
                if int(player["Pairing number"]) == ids_list[j]:
                    results.append(player)
                else:
                    pass    
        


        print("results: ", results)
        return results             

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

         
           
#if provisional_opponent is not 0:



"""AD = None

for i in already_took_opponent:
if pairing_number == i:
    AD =  None
    print("AD if:", AD)
    break
else:
    AD = pairing_number
    print("AD else:", AD)"""

#faire une liste avant de prendre le prmeier conservé ?"
#si provisional_opponent = i Le code va forcement garder le dernier.
#si None retirer l'opponent possibility de la liste ? 
#opponent_possibilility.remove[0] ?