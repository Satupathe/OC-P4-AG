"""Controller to display menu and inputs"""
from Controller import menu

class TournamentView:
                     
    def ask_tournament(self):

        tour_infos = {}

        questions = ["Tournament's name:   ",
                     "Tournament's adress:   ",
                     "Tournament's Date:   ",
                     "Total number of rounds:   ",
                     "Time control:   ",
                     "Number of player:   ",
                     "comments:   "
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

        return tour_infos

class PlayersView:

    def ask_players(self):

        players_infos = {}

        questions = ["Player's family name:   ",
                     "Player's first name:   ",
                     "Player's birthdate:   ",
                     "Player's gender:   ",
                     "Player's rank:   "
                    ]

        for i in range(8): #changé pour 8 fixe de base
            One_player = {}
            print('Please enter informations of player number ' + str(i+1) + ':   ')

            for j in questions:
                if j is not questions[4]:
                    One_player[j] = input(j)

                else:
                    try:
                        One_player[questions[4]] = int(input(j))

                    except ValueError:
                        print('Please enter an integer')
                   
            players_infos[i+1] = One_player

        return players_infos