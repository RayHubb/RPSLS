from human import Human
from computer import Computer
from player import Player

player1 = Human()
player2 = Human()
playerAI = Computer()


# TODO create a run function
# TODO select gestures
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

    # I want to display the gesture list, then choose gestures, run them through the comparicon checker and display results

    def run_game(self):
        print(player1.gesture_list)
        print(player1.choose_gesture())
        print(playerAI.choose_gesture())
        self.gesture_comparison_vs_ai()

    def gesture_comparison_vs_ai(self):
        if player1.gesture == playerAI.gesture:
            print('------------------------------------------------------------------')
            print(f"We both chose {player1.gesture} so it's a tie!")
            print('------------------------------------------------------------------')
            print('------------------------------------------------------------------')
        elif player1.gesture == "Rock":
            if playerAI.gesture == "Scissors" or playerAI.gesture == 'Lizard':
                print('------------------------------------------------------------------')
                print(f'{player1} wins!...Does not compute!! BEEP BOP!')
                print('------------------------------------------------------------------')
                print('------------------------------------------------------------------')
                player1.score += 1
            elif playerAI.gesture == 'Paper' or playerAI.gesture == 'Spock':
                print('------------------------------------------------------------------')
                print("*Happy BEEP BOOP BOPS* You lose human!")
                print('------------------------------------------------------------------')
                print('------------------------------------------------------------------')
                playerAI.score += 1
        elif player1.gesture == "Paper":
            if playerAI.gesture == "Rock" or playerAI.gesture == 'Spock':
                print('------------------------------------------------------------------')
                print(f'{player1} wins!...beginners luck if you ask me...')
                print('------------------------------------------------------------------')
                print('------------------------------------------------------------------')
                player1.score += 1
            elif playerAI.gesture == 'Scissors' or playerAI.gesture == 'Lizard':
                print('------------------------------------------------------------------')
                print("You lose human! BOOP BEEP!")
                print('------------------------------------------------------------------')
                print('------------------------------------------------------------------')
                playerAI.score += 1
        elif player1.gesture == "Scissors":
            if playerAI.gesture == "Paper" or playerAI.gesture == 'Lizard':
                print('------------------------------------------------------------------')
                print(f'{player1} wins!....BEEP BOP!! You got lucky!')
                print('------------------------------------------------------------------')
                print('------------------------------------------------------------------')
                player1.score += 1
            elif playerAI.gesture == 'Rock' or playerAI.gesture == 'Spock':
                print('------------------------------------------------------------------')
                print("BEEP BOP! Poor Human! You lose!")
                print('------------------------------------------------------------------')
                print('------------------------------------------------------------------')
                playerAI.score += 1
        elif player1.gesture == 'Lizard':
            if playerAI.gesture == 'Spock' or playerAI.gesture == 'Paper':
                print('------------------------------------------------------------------')
                print(f'Must be a miscalculation... {player1} wins?!')
                print('------------------------------------------------------------------')
                print('------------------------------------------------------------------')
                player1.score += 1
            elif playerAI.gesture == 'Scissors' or playerAI.gesture == 'Rock':
                print('------------------------------------------------------------------')
                print('uploading victory dance....*does the robot* You lose!!')
                print('------------------------------------------------------------------')
                print('------------------------------------------------------------------')
                playerAI.score += 1
        elif player1.gesture == 'Spock':
            if playerAI.gesture == 'Scissors' or playerAI.gesture == 'Rock':
                print('------------------------------------------------------------------')
                print(f'{player1} wins!...Wait that must be an error??...Lucky!')
                print('------------------------------------------------------------------')
                print('------------------------------------------------------------------')
                player1.score += 1
            elif playerAI.gesture == 'Lizard' or playerAI.gesture == 'Paper':
                print('------------------------------------------------------------------')
                print('BEEP BEEP BEEP! I WIN!!!! You Lose Human!!')
                print('------------------------------------------------------------------')
                print('------------------------------------------------------------------')
                playerAI.score += 1


