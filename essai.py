from collections import OrderedDict
from operator import getitem

joueurs_bypass = {}
joueurs_bypass['1'] = {'nom': 'Dupont', 'prenom': 'Alexandre', 'anniversaire': '1972', 'genre': 'M', 'rank': 1, 'pairing_nb': '', 'score': 0}
joueurs_bypass['2'] = {'nom': 'Durand', 'prenom': 'Aurelie', 'anniversaire': '1990', 'genre': 'F', 'rank': 4, 'pairing_nb': '', 'score': 0}
joueurs_bypass['3'] = {'nom': 'Dupuis', 'prenom': 'Monique', 'anniversaire': '1965', 'genre': 'F', 'rank': 6, 'pairing_nb': '', 'score': 0}
joueurs_bypass['4'] = {'nom': 'Bepas', 'prenom': 'Marion', 'anniversaire': '1987', 'genre': 'F', 'rank': 7, 'pairing_nb': '', 'score': 0}
joueurs_bypass['5'] = {'nom': 'Menant', 'prenom': 'laureen', 'anniversaire': '1994', 'genre': 'F', 'rank': 3, 'pairing_nb': '', 'score': 0}
joueurs_bypass['6'] = {'nom': 'Liotard', 'prenom': 'David', 'anniversaire': '1974', 'genre': 'X', 'rank': 2, 'pairing_nb': '', 'score': 0}
joueurs_bypass['7'] = {'nom': 'Roux', 'prenom': 'Cedric', 'anniversaire': '1979', 'genre': 'M', 'rank': 5, 'pairing_nb': '', 'score': 0}
joueurs_bypass['8'] = {'nom': 'Gagnieu', 'prenom': 'Arnaud', 'anniversaire': '1991', 'genre': 'M', 'rank': 8, 'pairing_nb': '', 'score': 0}


print(joueurs_bypass)

res = OrderedDict(sorted(joueurs_bypass.items(),
				  key=lambda x: getitem(x[1], 'rank'))
				 )

print(res)


"""players = {}
        for i in range (1,9,1):
            p_input_i = menu.PlayersController()
            joueurs_bypass = p_input_i.players_infos(i)
            
            joueur_i = player.Player(joueurs_bypass["Player's family name:"],
                                     joueurs_bypass["Player's first name:"],
                                     joueurs_bypass["Player's birthdate:"],
                                     joueurs_bypass["Player's gender:"],
                                     joueurs_bypass["Player's rank:"],
                                     joueurs_bypass["Pairing number"],
                                     joueurs_bypass['Score']
                                     )
            players[i] = joueur_i"""