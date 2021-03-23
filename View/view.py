"""View module to display menu and ask informations through inputs"""

import colorama
from colorama import Fore, Back, Style
from colorama import init

from Controller import menu




class TournamentView:
    """class to ask tournamment informations to the user"""       
    def ask_tournament(self):
        """
        Function combining fixed informations on tournament and user inputs
        return a dictionary of those informations
        """
        colorama.init(autoreset=True)
        print(f"{Style.BRIGHT}{Fore.BLUE}Entrée des informations sur le nouveau tournoi{Fore.RESET}")
        print("")
        loop_infos = {}
        tour_infos = {}

        questions = ["Tournament's name",
                     "Tournament's adress",
                     "Tournament's Date",
                     "Time control",
                     "Comments"
                    ] 

        for i in questions:
            loop_infos[i] = input(f"{i}:  ")

        tour_infos["Tournament's name"] = loop_infos["Tournament's name"]
        tour_infos["Tournament's adress"] = loop_infos["Tournament's adress"]
        tour_infos["Tournament's Date"] = loop_infos["Tournament's Date"] 
        tour_infos["Total number of rounds"] = 4  
        tour_infos["Round number"] = 0 
        tour_infos["Time control"] = loop_infos["Time control"]
        tour_infos["Number of player"] = 8
        tour_infos["Comments"] = loop_infos["Comments"]
        tour_infos["Rounds"] = {}
        print("")

        return tour_infos

class PlayersView:
    """class to ask players informations to the user"""
    def ask_players(self):
        """
        Function combining user input informations abouts the players
        return a dictionary of those informations
        """
        colorama.init(autoreset=True)
        print(f"{Style.BRIGHT}{Fore.BLUE}Entrée des informations sur les joueurs{Fore.RESET}")

        players_infos = []

        questions = ["Family name",
                     "First name",
                     "Birthdate",
                     "Gender",
                     "Rank"
                    ]

        for i in range(8):
            one_player = {} #Dictionnaire pour 1 joueur
            print('Please enter informations of player number ' + str(i+1) + ':')

            for j in questions:
                if j is not questions[4]:
                    one_player[j] = input(f"{j}:  ")
                
                else:
                    try:
                        one_player[questions[4]] = int(input(f"{j}:  "))

                    except ValueError:
                        print('Please enter an integer')
                        one_player[questions[4]] = int(input(f"{j}:  "))
                  
            one_player["Pairing number"] = int(i+1)
            one_player["Score"] = 0
            one_player["Opponents"] = []    

            players_infos.append(one_player)
            print("")

        return players_infos
        

class RoundView:

    def __init__(self, i, j, match):
        print("")
        print("Round "+str(j)+" Match "+str(i+1)+" : ")
        print(match)
        print('')
        self.score = 0
        colorama.init(autoreset=True)
    
    def ask_result(self, player):
        ask_result = input("Resultat: "+player[0]+" : ")
        
        if ask_result == "victory" or ask_result =="defeat" or ask_result =="draw":

            if ask_result == "victory":
                self.score = 1.0

            elif ask_result == "defeat":
                self.score = 0.0

            elif ask_result == "draw":
                self.score = 0.5

        else:
            print("Merci d'entrer: victory, defeat ou draw dans la console")
            self.ask_result(player)

        return self.score
    
class FinalScore:

    def print_results(self, final_score_list):
        colorama.init(autoreset=True)
        print("")
        print(f"{Style.BRIGHT}{Fore.BLUE}Tournament results:")
        place = 1
        for i in final_score_list:
            print("Place "+str(place)+" : ", i)
            place += 1
        print("")

class RankChange:

    def __init__(self):
        self.action_modif = None
        self.ended_action = None
        self.ongoing_action = None
        colorama.init(autoreset=True)
    
    def ask_ended_tournament(self):
        print(f"{Style.BRIGHT}Voulez-vous modifier les ranks des joueurs du tournoi venant de se terminer?")
        print("")
        print(f"{Style.BRIGHT}{Fore.RED}yes:              {Style.NORMAL}{Fore.WHITE}Permet de modifier le rank des joueurs du tournoi venant de se terminer")
        print(f"{Style.BRIGHT}{Fore.RED}menu:             {Style.NORMAL}{Fore.WHITE}Permet de revenir au menu principal, les actions précédentes sont enregistrées")
        ask_action = input("Action choisie: ")
        print("")
        
        if ask_action == "yes":
            self.ended_action = "yes"

        elif ask_action == "menu":
            self.ended_action = "menu"

        else:
            print("Merci de rentrer la bonne commande comme indiqué dans les propositions ci-dessus")
            self.ask_ended_tournament()

        return self.ended_action

    def ask_ongoing_tournament(self):
        print("")
        print(f"{Style.BRIGHT}Voulez-vous modifier les ranks des joueurs du tournoi en cours?")
        print(f"{Style.BRIGHT}{Fore.RED}yes:              {Style.NORMAL}{Fore.WHITE}Permet de modifier le rank des joueurs du tournoi actuel")
        print(f"{Style.BRIGHT}{Fore.RED}no:               {Style.NORMAL}{Fore.WHITE}Permet de continuer sans modifications")
        ask_action = input("Action choisie: ")
        print("")
        
        if ask_action == "yes":
            self.ongoing_action = "yes"

        elif ask_action == "no":
            self.ongoing_action = "no"

        else:
            print("Merci de rentrer la bonne commande comme indiqué dans les propositions ci-dessus")
            self.ask_ongoing_tournament()

        return self.ongoing_action

    def ask_all_player(self, player):
        print(f"{Style.BRIGHT}Voulez-vous changer le rank du joueur suivant? Merci d'entrer 'yes' ou 'no'")
        print(player)
        ask_action = input("Action choisie: ")
        
        if ask_action == "yes":
            self.action_modif = "yes"

        elif ask_action == "no":
            self.action_modif = "no"

        else:
            print("Merci de rentrer 'yes' ou 'no'")
            self.ask_all_player(player)

        print(self.action_modif)
        return self.action_modif

    def ask_one_player_number(self, players_list):
        i = 0
        for player in players_list:
            print(f"Joueur {i+1}: {player}")
            i += 1
    
        number = input("Numéro du joueur dont le rank est à changer: ")

        return number

    def ask_new_rank(self):

        new_rank = input("Nouveau rank du joueur: ")
        print("")

        return new_rank


class HomeMenuView:
    
    def __init__(self):
        colorama.init(autoreset=True)
        print (f"{Style.BRIGHT}{Fore.BLUE}Menu de selection des options du logiciel{Fore.RESET}")
        print(f"")
        print("Merci d'entrer un des mots suivant: ")
        print(f"{Style.BRIGHT}{Fore.RED}start:            {Style.NORMAL}{Fore.WHITE}Permet de commencer un nouveau tournoi")
        print(f"{Style.BRIGHT}{Fore.RED}continuation:     {Style.NORMAL}{Fore.WHITE}Permet de reprendre un ancien tournoi")
        print(f"{Style.BRIGHT}{Fore.RED}show:             {Style.NORMAL}{Fore.WHITE}Permet d'afficher les informations d'anciens tournois")
        print(f"{Style.BRIGHT}{Fore.RED}clear:            {Style.NORMAL}{Fore.WHITE}Permet d'effacer les informations précédentes présentes sur la console")
        print(f"{Style.BRIGHT}{Fore.RED}exit:             {Style.NORMAL}{Fore.WHITE}Permet de quitter le programme et fermer la console de commande")
        print("")
        self.action = None
    
    def call_first_action(self):
        ask_action = input("Action choisie: ")

        if ask_action == "start":
            self.action = "start"
        elif ask_action == "continuation":
            self.action = "continuation" 
        elif ask_action == "show":
            self.action = "show"
        elif ask_action == "clear":
            self.action = "clear"
        elif ask_action == "exit":
            self.action = "exit"
        else:
            print("")
            print("Merci de rentrer la bonne commande comme indiqué dans les propositions ci-dessous")
            self.call_first_action()

        return self.action


class CallTournamentNumber:

    def __init__(self):
        self.number = None

    def __call__(self):
        colorama.init(autoreset=True)
        print("")
        print(f"{Style.BRIGHT}{Fore.BLUE}Ecran de selection d'un tournoi a continuer{Fore.RESET}")
        print("")
        print("Merci d'enter le numero du tournoi a poursuivre ou 'exit'")
        print("Vous pouvez le rechercher via la fonction show du menu principal")
        print("")
        
    def ask_number(self):
        try:
            ask_number = int(input("Numero du tournoi: "))
            self.number = ask_number
            pass

        except ValueError:
            print("Merci d'entrer un nombre entier")
            print("")
            self.ask_number()

        return self.number

    def ask_again(self):
        print("Merci d'entrer le numero valide d'un tournoi")


class AskContinue:
    def __init__(self):
        self.go_next_round = None
        colorama.init(autoreset=True)

    def ask_start_round(self):
        print("")
        input(f"Appuyez sur ENTREE pour commencer le round")

    def ask_end_round(self):
        print("")
        input(f"Appuyez sur ENTREE pour ternimner le round")

    def ask_go_next_round(self): # attention vrifier et fixer la récursivité !!!!!!
        print("")
        print(f"{Style.BRIGHT}{Fore.RED}Voulez-vous passer au round suivant ?")
        print("")
        print(f"{Style.BRIGHT}{Fore.RED}yes:              {Style.NORMAL}{Fore.WHITE}Permet de passer au round suivant")
        print(f"{Style.BRIGHT}{Fore.RED}menu:             {Style.NORMAL}{Fore.WHITE}Permet de revenir au menu principal, les actions précédentes sont enregistrées")
        ask_action = input(f"Action choisie: ")
        print("")

        if ask_action == "yes":
            self.go_next_round = "yes"

        elif ask_action =="menu":
            self.go_next_round = "menu"

        else:
            print("")
            print("Merci de rentrer la bonne commande comme indiqué dans les propositions ci-dessous")
            self.ask_go_next_round()

        return self.go_next_round

class CallShowAction:
    def __init__(self):
        colorama.init(autoreset=True)
        self.action = None

    def ask_show_action(self):
        print (f"{Style.BRIGHT}{Fore.BLUE}Menu d'affichage des rapports de données{Fore.RESET}")
        print("")
        print("Merci d'entrer un des mots suivant: ")
        print(f"{Style.BRIGHT}{Fore.RED}tournaments:      {Style.NORMAL}{Fore.WHITE}Permet de sélectionner un tournoi spécifique")
        print(f"{Style.BRIGHT}{Fore.RED}total players:    {Style.NORMAL}{Fore.WHITE}Permet d'afficher l'ensemble des joueurs")
        print(f"{Style.BRIGHT}{Fore.RED}menu:             {Style.NORMAL}{Fore.WHITE}Permet de retourner au menu principal")
        print("")
        ask_action = input("Action choisie: ")
        print("")

        self.action = ask_action
        return self.action

    def ask_type_tournament(self):
        print (f"{Style.BRIGHT}Voulez-vous afficher les tournois en cours ou l'ensemble des tournois?")
        print("")
        print(f"{Style.NORMAL}Merci d'entrer un des mots suivant: ")
        print(f"{Style.BRIGHT}{Fore.RED}total:            {Style.NORMAL}{Fore.WHITE}Permet d'afficher la liste de tous les tournois enregistrés")
        print(f"{Style.BRIGHT}{Fore.RED}unfinished:       {Style.NORMAL}{Fore.WHITE}Permet d'afficher seulement les tournoi en cours")
        print(f"{Style.BRIGHT}{Fore.RED}back:             {Style.NORMAL}{Fore.WHITE}Permet de retourner au menu précédent")
        print("")
        ask_action = input("Action choisie: ")
        print("")

        self.action = ask_action
        return self.action

    def ask_players_sorting(self):
        print (f"{Style.BRIGHT}Voulez-vous afficher la liste des joueurs par rank ou ordre alphabétique?")
        print("")
        print("Merci d'entrer un des mots suivant: ")
        print(f"{Style.BRIGHT}{Fore.RED}rank:             {Style.NORMAL}{Fore.WHITE}Permet d'afficher la liste des joueurs par rank")
        print(f"{Style.BRIGHT}{Fore.RED}name:             {Style.NORMAL}{Fore.WHITE}Permet d'afficher la liste des joueurs par ordre alphabétique")
        print(f"{Style.BRIGHT}{Fore.RED}back:             {Style.NORMAL}{Fore.WHITE}Permet de retourner au menu précédent")
        print("")
        ask_action = input("Action choisie: ")
        print("")

        self.action = ask_action
        return self.action

    def print_sorted_players(self, info_type, informations):
        print(f"{Style.BRIGHT}liste de l'ensemble des joueurs triés par {info_type} :")
        lenght = len(informations)
        print(f"Nombre total de joueurs: {lenght}")
        for player in informations:
            print(player)
        print("")


    def print_tournaments_list(self, all_tournaments):
        print (f"{Style.BRIGHT}Liste de l'ensemble des tournois enregistrés")
        print("")
        for tournament in all_tournaments:
            print(tournament)
        print("")

    def print_unfinished_tournaments(self, all_tournaments):
        print (f"{Style.BRIGHT}Liste de l'ensemble des tournois en cours")
        print("")
        for tournament in all_tournaments:
            print(tournament)
        print("")

    def ask_tournament_id(self):
        print (f"{Style.BRIGHT}Merci de renseigner le numéro du tournoi sélectionné")
        print("")

    def ask_tournament_action(self, tournament_id):
        print (f"{Style.BRIGHT}Veuillez sélectionner les informations à afficher pour le tournoi numéro {tournament_id}")
        print("")
        print("Merci d'entrer un des mots suivant: ")
        print(f"{Style.BRIGHT}{Fore.RED}score:            {Style.NORMAL}{Fore.WHITE}Permet d'afficher la liste des joueurs du tournoi par score")
        print(f"{Style.BRIGHT}{Fore.RED}name:             {Style.NORMAL}{Fore.WHITE}Permet d'afficher la liste des joueurs du tournoi par ordre alphabétique")
        print(f"{Style.BRIGHT}{Fore.RED}rounds:           {Style.NORMAL}{Fore.WHITE}Permet d'afficher les rounds du tournoi")
        print(f"{Style.BRIGHT}{Fore.RED}matchs:           {Style.NORMAL}{Fore.WHITE}Permet d'afficher la liste des matchs du tournoi")
        print(f"{Style.BRIGHT}{Fore.RED}back:             {Style.NORMAL}{Fore.WHITE}Permet de changer le numéro du tournoi sélectionné")
        print(f"{Style.BRIGHT}{Fore.RED}menu:             {Style.NORMAL}{Fore.WHITE}Permet de retourner à la racine du menu show")
        print("")
        ask_action = input("Action choisie: ")
        print("")

        self.action = ask_action
        return self.action

    def print_specific_informations(self, tournament_id, info_type, informations):
        print(f"{Style.BRIGHT} Liste des {info_type} pour le tournoi {tournament_id}")
        if len(informations) == 0:
            null_informations = "Il n'y a eu aucun round de terminé pour ce tournoi"
            print(null_informations)
        else:
            if info_type == "rounds":
                for element in informations:
                    print(f"Heure du début du round:   {element[0]}")
                    print(f"Heure de fin du round:     {element[1]}")
                    for match in element[2]:
                        print(match)
                    print("")
            else:
                for element in informations:
                    print(element)
        print("")

        # attention retour au menu !!!!!