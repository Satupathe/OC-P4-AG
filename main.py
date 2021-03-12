""" Main file to launch each controller according to user needs"""

from Controller import schedule



def main ():
	"""Appelle le controller schedule"""
	app = schedule.FrontController()
	app.start()

if __name__ == '__main__':
    main()

""" en mettant main.add('une lettre', 'quelque chose à écrire ou un fichiier à consulter')
cela permettra de mettre des options d'appel des modules
pour par exemple afficher les rapports ou changer le classement des joueurs
webinaire pendu p2 à 1h de vidéo"""