from player import Player
from computer import Computer


class Game:
    def __init__(self):
        self.player = ''
        self.player2 = ''
        self.game_mode = None

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


player1 = Player()
ai_player = Computer()

