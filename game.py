from human import Human
from computer import Computer


player1 = Human()
player2 = Human()
playerAI = Computer()
playerAI.choose_gesture()



# TODO create a run function
# TODO create a welcome display with rules
# TODO choose game mode pvp or pvAI
# TODO select gestures
# TODO compare the gestures
# TODO determine a winner or rerun if it is a tie
# TODO update score

class Game:
    def __init__(self):
        self.player = ''
        self.player2 = ''

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

    def rock(self):
        pass







