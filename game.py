from human import Human
from computer import Computer
from player import Player


player1 = Human()
player2 = Human()
playerAI = Computer()


# TODO create a run function
# TODO select gestures
# TODO compare the gestures
# TODO determine a winner or rerun if it is a tie
# TODO update score

class Game:
    def __init__(self):
        self.player_one = ''
        self.player_two = ''

    def welcome_display(self):
        print('------------------------------------------------------------------')
        print('Welcome to Rock Paper Scissors Lizard Spock!!')
        print('------------------------------------------------------------------')
        print('------------------------------------------------------------------')
        print('The rules are simple! Select a hand gesture by choosing the \n'
              'number associated with it!')
        print('------------------------------------------------------------------')
        print('------------------------------------------------------------------')
        print(player1.gesture_list)
        print('------------------------------------------------------------------')
        print('For example, choosing a 1 from the above choices will return Rock!')
        print('------------------------------------------------------------------')
        print('------------------------------------------------------------------')
        print('Your opponent will also choose a gesture! The winner of the round \n'
              'will be given a point! The first player to reach 2 points wins!')
        print('------------------------------------------------------------------')
        print('------------------------------------------------------------------')
        print('                        GOOD LUCK!                                ')

    def multiplayer(self):
        print('------------------------------------------------------------------')
        print('                     Select Game Mode                             ')
        print('------------------------------------------------------------------')
        game_mode = int(input('Would you like to play against me or a friend? To play against \n'
                              'a friend type 1! To play against me press 2!: '))
        print('------------------------------------------------------------------')
        print('------------------------------------------------------------------')
        if game_mode == 1:
            self.player_one = player1
            self.player_two = playerAI
            print('*angry BEEP BOOP BOPS* So you have chosen to face me!')
            print('------------------------------------------------------------------')
        elif game_mode == 2:
            self.player_one = player1
            self.player_two = player2
            print("You've chosen to play with a friend! Good choice! You have a\n"
                  '0.00000000001% chance of defeating me!')
            print('------------------------------------------------------------------')
        else:
            print('------------------------------------------------------------------')
            print('Error! Error! Please type 1 or 2 only!! Ill ask again...')
            print('------------------------------------------------------------------')
            self.multiplayer()


