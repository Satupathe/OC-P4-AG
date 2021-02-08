"""Controller to display menu and inputs"""


class TournamentInput:
                     
    def t_input(self):

        tour_infos = []

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
                    tour_infos.append(int(input(i)))

                except ValueError:
                    print('Please enter an integer')
                    tour_infos.append(int(input(i)))

            elif i is questions[5]:
                try:
                    tour_infos.append(int(input(i)))

                except ValueError:
                    print('Please enter an integer')
                    tour_infos.append(int(input(i)))

            else:
                tour_infos.append(input(i))

        return tour_infos
