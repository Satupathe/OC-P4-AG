""" Main file to launch the Front Controller"""

from Controller import schedule


def main():
    """Call the Front Controller and the menu of this program"""
    app = schedule.FrontController()
    app.start()


if __name__ == '__main__':
    main()
