""" Main file to launch each controller according to user needs"""

from Controller import schedule



def main ():
	tournament = schedule.Schedule()
	tournament.objects()

if __name__ == '__main__':
    main()
