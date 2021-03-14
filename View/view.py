"""Controller to display menu and inputs"""
from Controller import menu

class TournamentView:
                     
    def ask_tournament(self):
        """Appelle les input du tournoi et renvoi un dictionnaire"""
        tour_infos = {}

        questions = ["Tournament's name:",
                     "Tournament's adress:",
                     "Tournament's Date:",
                     "Time control:",
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

        tour_infos["Round number"] = 0 
        tour_infos["Number of player"] = 8
        tour_infos["Round 1"] = None
        tour_infos["Round 2"] = None
        tour_infos["Round 3"] = None
        tour_infos["Round 4"] = None
        tour_infos["Tournament's matches"] = {}
        
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
                   
            one_player["Pairing number"] = int(i)
            one_player["Score"] = 0
            one_player["Opponents"] = []    

            players_infos.append(one_player)


        return players_infos # renvoie la liste des dictionnaires
        

class RoundView:

    def __init__(self, i, j, match):
        print("")
        print("Round "+str(j)+" Match "+str(i+1)+" : ")
        print(match)
        print('')
        self.score = 0
    
    def ask_result(self, player):
        ask_result = input("Resultat: "+player[0]+" : ")
        
        if ask_result == "v" or ask_result =="def" or ask_result =="d":

            if ask_result == "v":
                self.score = 1.0

            elif ask_result == "def":
                self.score = 0.0

            elif ask_result == "d":
                self.score = 0.5   #attention récursivité n'annule pas la fonction précédente

        else:
            print("Merci d'entrer: victory, defeat ou draw dans la console")
            self.ask_result(player)

        return self.score # mettre en dehors de la récursivité.
    
class FinalScore:

    def print_results(self, final_score_list):
        print("")
        print("Tournament results:")
        place = 1
        for i in final_score_list:
            print("Place "+str(place)+" : ", i)
            place += 1


class HomeMenuView:
    
    def __call__(self):
        print ("Menu de selection des options du logiciel")
        print("")
        print("Merci d'entrer un des mots suivant: ")
        print("start:         Permet de commencer un nouveau tournoi")
        print("continuation:  Permet de reprendre un ancien tournoi")
        print("show:          Permet d'afficher les informations d'anciens tournois")
        print("exit:          Permet de quitter le programme et fermer la console de commande")
        print("")
        ask_action = input("Action choisie: ")

        return ask_action

class CallTournamentNumber:

    def __call__(self):
        print("")
        print("Ecran de selection d'un tournoi a continuer")
        print("")
        print("Merci d'enter le numero du tournoi a poursuivre ou 'exit'")
        print("Vous pouvez le rechercher via la fonction show du menu principal")
        print("")
        
    def ask_number(self):
        try:
            ask_action = int(input("Numero du tournoi: "))
            pass

        except ValueError:
            print("Merci d'entrer un nombre entier")
            print("")
            self.__call__()

        return ask_action

class AskContinue:
    def ask_start_round(self):
        print("")
        input("Entrez 'GO' pour commencer le round: ")

    def ask_end_round(self):
        print("")
        input("Entrez END pour finir le round: ")

    def ask_go_next_round(self):
        print("")
        print("Voulez-vous passer au round suivant ?")
        print("")
        print("Pour passer au round suivant entrez 'yes'")
        print("Pour revenir au menu principal entrez 'menu', les actions précédentes sont enregistrées")
        ask_action = input("Voulez_vous continuer ?   ")
        print("")
        action = None

        if ask_action == "yes":
            action = "yes"

        elif ask_action =="menu":
            action = "menu"

        else:
            print("")
            print("Merci de rentrer la bonne commande comme indiqué dans les propositions ci-dessous")
            self.ask_go_next_round()

        return action