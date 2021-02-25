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
                        #appel recursif faire uen fonction qui accepte le try except et dans le except rappeler la fonction
                   
            one_player["Pairing number"] = ''
            one_player["Score"] = 0       

            players_infos.append(one_player)


        return players_infos # renvoie la liste des dictionnaires
        

class RoundView:

    def __init__(self, i, j, match):
        print("Round "+str(j)+" Match "+str(i+1)+" : ")
        print(match)
        print('')
        print("")
        self.score = 0
    
    def ask_results(self, player):
        ask_result = input("Resultat: "+player[0]+" : ")
        
        if ask_result == "victory" or ask_result =="defeat" or ask_result =="draw":

            if ask_result == "victory":
                self.score = 1.0

            elif ask_result == "defeat":
                self.score = 0.0

            elif ask_result == "draw":
                self.score = 0.5   
                print(self.score)

        else:
            print("Merci d'entrer: victory, defeat ou draw")
            self.ask_results(player)

        print(self.score)
        print(type(self.score))
        return self.score
        

        """if ask_results == "victory":
            score = 1

        elif ask_results == "defeat":
            score = 0

        elif ask_results == "draw":
            score = 0.5   
        
        else:
            print("Merci d'entrer le résultat suivant: victory, defeat ou draw")
            ask_results = input("Resultat: "+player[0]+" : ")
            if ask_results == "victory":
                score = 1

            elif ask_results == "defeat":
                score = 0

            elif ask_results == "draw":
                score = 0.5       

        return score
        


            #rappeler le nom du joueur
            #faire un input pour demander le résultat    

#ATTENTION !!!!
# pour l'affichage des informations partir de la sauvegarde du json.
#ça sera peut être plus simple que d'utiliser la mémoire ram."""