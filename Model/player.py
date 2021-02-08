""" Player class. 
Used to store player informations.
Keep informations available for the User
"""

class Player:
	def __init__(self, name, first_name, birthdate, gender, ranking):
		self.name = name
		self.first_name = first_name
		self.birth_date = birth_date
		self.gender = gender
		self.ranking = ranking


		def player_dict(self):
        self.player = {}
        self.player['Name'] = self.name
        self.player['First name'] = self.place
        self.player['Birthdate'] = self.start_date
        self.player['Gender'] = self.number_of_round
        self.player['Ranking'] = self.players

        return self.player

    

    def save(self):
        dictionnary = self.player
        with open ('players.json', 'a', encoding='utf8') as play:
            json.dump(dictionnary, play, ensure_ascii=False, indent = 4)


def main():
    player1 = Player('Gagnieu', 
                      'Arnaud',
                      '11 Novembre 1991',
                      'M',
                      3
                      )

    dict_essai = player1.player_dict()
    player1.save()
    

main = main()