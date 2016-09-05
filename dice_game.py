from itertools import cycle
import random
import time


def print_header():
    print(''.center(30, '-'))
    print('Catan Dice Utility'.center(30, ' '))
    print(''.center(30, '-'))


def print_goodbye():
    print('Thank you for playing Catan!')


def get_players():
    players = []
    while True:
        number_of_players = input('How many are playing Catan? ').strip()
        try:
            number_of_players = int(number_of_players)
            break
        except ValueError:
            print('Invalid input. Please enter an integer')
    for i in range(1, number_of_players + 1):
        player = input("What is player {}'s name? ".format(i))
        players.append(player)
    print(players)
    return players


class DiceGame(object):
    def __init__(self, players, number_of_dice=2, sided_dice=6):
        self.sided_dice = sided_dice
        self.number_of_dice = number_of_dice
        self.players = players

    def roll_dice(self):
        players = cycle(self.players)
        number_of_dice = self.number_of_dice
        sided_dice = self.sided_dice

        for x in players:
            print("It is {}'s turn.".format(x))
            print('{} rolls:'.format(x))
            time.sleep(1)
            rolls = []
            for _ in range(number_of_dice):
                roll = random.randint(1, sided_dice)
                rolls.append(roll)
            roll_total = sum(rolls)
            print('{}'.format(roll_total))
            if roll_total == 7:
                print('You now have to move the thief.')
                time.sleep(5)

            cmd = input('Press Enter to continue, [Q] to quit. ')
            print()

#            if cmd.lower() == 'r':
#                print('{} re-rolls and gets:'.format(x))
#                time.sleep(1)
#                rolls = []
#                for _ in range(number_of_dice):
#                    roll = random.randint(1, sided_dice)
#                    rolls.append(roll)
#                roll_total = sum(rolls)
#                print('{}'.format(roll_total))
#                print()

            if cmd.lower() == 'q':
                break


def main():
    print_header()

    players = get_players()
    print()

    game = DiceGame(players)
    game.roll_dice()

    print_goodbye()


if __name__ == '__main__':
    main()
