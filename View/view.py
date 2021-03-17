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
        tour_infos["Rounds"] = {}
        tour_infos["Tournament's matches"] = {}
        
        return tour_infos # renvoi le dictionnaire du tournoi

class PlayersView:

    def ask_players(self):
        """Appelle les input pour chaque joueur et renvoi une liste de dictionnaires"""
        players_infos = []

        questions = ["Player's family name",
                     "Player's first name",
                     "Player's birthdate",
                     "Player's gender",
                     "Player's rank"
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
        print("")

class HomeMenuView:
    
    def __call__(self):
        print ("Menu de selection des options du logiciel")
        print("")
        print("Merci d'entrer un des mots suivant: ")
        print("start:            Permet de commencer un nouveau tournoi")
        print("continuation:     Permet de reprendre un ancien tournoi")
        print("show:             Permet d'afficher les informations d'anciens tournois")
        print("exit:             Permet de quitter le programme et fermer la console de commande")
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

    def ask_go_next_round(self): # attention vrifier et fixer la récursivité !!!!!!
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

class CallShowAction:
    def ask_show_action(self):
        print ("Menu d'affichage des rapports de données")
        print("")
        print("Merci d'entrer un des mots suivant: ")
        print("tournaments:      Permet de sélectionner un tournoi spécifique")
        print("total players:    Permet d'afficher l'ensemble des joueurs")
        print("menu:             Permet de retourner au menu principal")
        print("")
        ask_action = input("Action choisie: ")
        print("")

        return ask_action

    def ask_type_tournament(self):
        print ("Voulez-vous afficher les tournois en cours ou l'ensemble des tournois?")
        print("")
        print("Merci d'entrer un des mots suivant: ")
        print("total:            Permet d'afficher la liste de tous les tournois enregistrés")
        print("unfinished:       Permet d'afficher seulement les tournoi en cours")
        print("back:             Permet de retourner au menu précédent")
        print("")
        ask_action = input("Action choisie: ")
        print("")

        return ask_action

    def ask_players_sorting(self):
        print ("Voulez-vous afficher la liste des joueurs par rank ou ordre alphabétique?")
        print("")
        print("Merci d'entrer un des mots suivant: ")
        print("rank:             Permet d'afficher la liste des joueurs par rank")
        print("name:             Permet d'afficher la liste des joueurs par ordre alphabétique")
        print("back:             Permet de retourner au menu précédent")
        print("")
        ask_action = input("Action choisie: ")
        print("")

        return ask_action

    def print_sorted_players(self, info_type, informations):
        print("liste de l'ensemble des joueurs triés par " + info_type + " :")
        print(informations)
        print("")


    def print_tournaments_list(self, all_tournaments):
        print ("Liste de l'ensemble des tournois enregistrés")
        print("")
        for tournament in all_tournaments:
            print(tournament)
        print("")

    def print_unfinished_tournaments(self, all_tournaments):
        print ("Liste de l'ensemble des tournois en cours")
        print("")
        for tournament in all_tournaments:
            print(tournament)
        print("")

    def ask_tournament_id(self):
        print ("Merci de renseigner le numéro du tournoi sélectionné")
        print("")
        ask_action = input("Numéro du tournoi: ")
        print("")

        return ask_action

    def ask_tournament_action(self, tournament_id):
        print ("Veuillez sélectionner les informations à afficher pour le tournoi numéro " + tournament_id)
        print("")
        print("Merci d'entrer un des mots suivant: ")
        print("score:            Permet d'afficher la liste des joueurs du tournoi par score")
        print("name:             Permet d'afficher la liste des joueurs du tournoi par ordre alphabétique")
        print("rounds:           Permet d'afficher les rounds du tournoi")
        print("matchs:           Permet d'afficher la liste des matchs du tournoi")
        print("back:             Permet de changer le numéro du tournoi sélectionné")
        print("menu:             Permet de retourner à la racine du menu show")
        print("")
        ask_action = input("Action choisie: ")
        print("")

        return ask_action

    def print_specific_informations(self, tournament_id, info_type, informations):
        print("liste " + info_type + " pour le tournoi " + tournament_id)
        for element in informations:
            print(element)
        print("")

        # attention retour au menu !!!!!