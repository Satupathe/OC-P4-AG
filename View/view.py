"""Controller to display menu and inputs"""
from Controller import menu

class TournamentView:
                     
    def ask_tournament(self):
        """Appelle les input du tournoi et renvoi un dictionnaire"""
        tour_infos = {}

        questions = ["Tournament's name:",
                     "Tournament's adress:",
                     "Tournament's Date:",
                     "Total number of rounds:",
                     "Time control:",
                     "Number of player:",
                     "Comments:"
                    ] 

        for i in questions:
            if i is questions[3]:
                try:
                    tour_infos[i] = int(input(i))

                except ValueError:
                    print('Please enter an integer')
                    tour_infos[i] = int(input(i))

            elif i is questions[5]:
                try:
                    tour_infos[i] = int(input(i))

                except ValueError:
                    print('Please enter an integer')
                    tour_infos[i] = int(input(i))


            elif i is questions[4]:
                try:
                    tour_infos[i] = int(input(i))

                except ValueError:
                    print('Please enter an integer')
                    tour_infos[i] = int(input(i))

            else:
                tour_infos[i] = input(i)

        
        return tour_infos # renvoi le dictionnaire du tournoi

class PlayersView:

    def ask_players(self):
        """Appelle les input pour chaque joueur et renvoi une liste de dictionnaires"""
        players_infos = []

        questions = ["Player's family name:",
                     "Player's first name:",
                     "Player's birthdate:",
                     "Player's gender:",
                     "Player's rank:"
                    ]

        for i in range(8):
            one_player = {} #Dictionnaire pour 1 joueur
            print('Please enter informations of player number ' + str(i+1) + ':')

            for j in questions:
                if j is not questions[4]:
                    one_player[j] = input(j)

                else:
                    try:
                        one_player[questions[4]] = int(input(j))

                    except ValueError:
                        print('Please enter an integer')
                   
            one_player["Pairing number"] = ''
            one_player["Score"] = 0       

            players_infos.append(one_player)


        return players_infos # renvoie la liste des dictionnaires
        

class RoundView:

    def __init__(self, i):
        print("Matchs du round " + i + " : ")

    def __str__(self):
        return "member of Test" #laisser dans view ou dans RoundController ??

    def ask_results(self, player):
            print(player)
            #rappeler le nom du joueur
            #faire un input pour demander le résultat    


