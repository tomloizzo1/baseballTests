# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from pypitchfx.scrape import scrape_games_players


def main():
    x,y  =  scrape_games_players(start='2013-06-01',end='2013-06-01')
    return (x,y)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
