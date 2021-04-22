from human import Human
from computer import Computer
from player import Player

player1 = Human()
player2 = Human()
playerAI = Computer()



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
              'will be given a point! The first player with the most wins by the \n'
              '3rd Round wins!!')
        print('------------------------------------------------------------------')
        print('------------------------------------------------------------------')
        print('                        GOOD LUCK!                                ')

    def multiplayer(self):
        print('------------------------------------------------------------------')
        print('                     Select Game Mode                             ')
        print('------------------------------------------------------------------')
        game_mode = int(input('Would you like to play against me or a friend? To play against \n'
                              'against me type 1! To play a friend type 2! :'))
        print('------------------------------------------------------------------')
        print('------------------------------------------------------------------')
        if game_mode == 1:
            self.player_one = player1
            self.player_two = playerAI
            print('*angry BEEP BOOP BOPS* So you have chosen to face me!')
            print('------------------------------------------------------------------')
            self.run_game1()
        elif game_mode == 2:
            self.player_one = player1
            self.player_two = player2
            print("You've chosen to play with a friend! Good choice! You have a\n"
                  '0.00000000001% chance of defeating me!')
            print('------------------------------------------------------------------')
            self.run_game2()
        else:
            print('------------------------------------------------------------------')
            print('Error! Error! Please type 1 or 2 only!! Ill ask again...')
            print('------------------------------------------------------------------')
            self.multiplayer()

# I want to display the gesture list, then choose gestures, run them through the comparicon checker and display results

    def run_game1(self):
        while player1.score < 2 and playerAI.score < 2:
            print('------------------------------------------------------------------')
            print('                          Round 1                                 ')
            print(player1.gesture_list)
            print(player1.choose_gesture())
            print(playerAI.choose_gesture())
            self.gesture_comparison_vs_ai()
            self.show_score()
            if player1.gesture == playerAI.gesture:
                print(player1.gesture_list)
                print(player1.choose_gesture())
                print(playerAI.choose_gesture())
                self.gesture_comparison_vs_ai()
                self.show_score()
            print('------------------------------------------------------------------')
            print('                          Round 2                                 ')
            print(player1.gesture_list)
            print(player1.choose_gesture())
            print(playerAI.choose_gesture())
            self.gesture_comparison_vs_ai()
            self.show_score()
            if player1.gesture == playerAI.gesture:
                print(player1.gesture_list)
                print(player1.choose_gesture())
                print(playerAI.choose_gesture())
                self.gesture_comparison_vs_ai()
                self.show_score()
            if player1.score == 2:
                print('------------------------------------------------------------------')
                print('Player 1 Wins!!')
                print('------------------------------------------------------------------')
                print('------------------------------------------------------------------')
                break
            elif playerAI.score == 2:
                print('------------------------------------------------------------------')
                print('You lose HUMAN!! *excited BEEP BOOPs*!!')
                print('------------------------------------------------------------------')
                print('------------------------------------------------------------------')
                break
            print('------------------------------------------------------------------')
            print('                          Round 3                                 ')
            print(player1.gesture_list)
            print(player1.choose_gesture())
            print(playerAI.choose_gesture())
            self.gesture_comparison_vs_ai()
            self.show_score()
            if player1.gesture == playerAI.gesture:
                print(player1.gesture_list)
                print(player1.choose_gesture())
                print(playerAI.choose_gesture())
                self.gesture_comparison_vs_ai()
                self.show_score()
            if player1.score == 2:
                print('------------------------------------------------------------------')
                print('Player 1 Wins!!')
                print('------------------------------------------------------------------')
                print('------------------------------------------------------------------')
            elif playerAI.score == 2:
                print('------------------------------------------------------------------')
                print('You lose HUMAN!! *excited BEEP BOOPs*!!')
                print('------------------------------------------------------------------')
                print('------------------------------------------------------------------')

    def gesture_comparison_vs_ai(self):
        if player1.gesture == playerAI.gesture:
            print('------------------------------------------------------------------')
            print(f"We both chose {player1.gesture} so it's a tie!")
            print('------------------------------------------------------------------')
            print('------------------------------------------------------------------')
        elif player1.gesture == "Rock":
            if playerAI.gesture == "Scissors" or playerAI.gesture == 'Lizard':
                print('------------------------------------------------------------------')
                print('Player 1 wins!...Does not compute!! BEEP BOP!')
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
                print('Player 1 wins!...beginners luck if you ask me...')
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
                print('Player1 wins!....BEEP BOP!! You got lucky!')
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
                print('Must be a miscalculation... Player1 wins?!')
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
                print('Player 1 wins!...Wait that must be an error??...Lucky!')
                print('------------------------------------------------------------------')
                print('------------------------------------------------------------------')
                player1.score += 1
            elif playerAI.gesture == 'Lizard' or playerAI.gesture == 'Paper':
                print('------------------------------------------------------------------')
                print('BEEP BEEP BEEP! I WIN!!!! You Lose Human!!')
                print('------------------------------------------------------------------')
                print('------------------------------------------------------------------')
                playerAI.score += 1

# I need to make separate game methods that allow a player to play against another human user.
    def display_human_gestures(self):
        print('------------------------------------------------------------------')
        print(f'Player 1 chose {player1.gesture}! and Player 2 chose {player2.gesture}!')

    def run_game2(self):
        while player1.score < 2 and player2.score < 2:
            print('------------------------------------------------------------------')
            print('                          Round 1                                 ')
            print(player1.gesture_list)
            print('------------------------------------------------------------------')
            print(player1.choose_gesture_humans())
            print(player2.gesture_list)
            print('------------------------------------------------------------------')
            print(player2.choose_gesture_humans2())
            print('------------------------------------------------------------------')
            print('------------------------------------------------------------------')
            self.gesture_comparison_humans()
            print('------------------------------------------------------------------')
            print('------------------------------------------------------------------')
            self.show_score()
            if player1.gesture == player2.gesture:
                continue
            print('                          Round 2                                 ')
            print(player1.gesture_list)
            print('------------------------------------------------------------------')
            print(player1.choose_gesture_humans())
            print(player2.gesture_list)
            print('------------------------------------------------------------------')
            print(player2.choose_gesture_humans2())
            self.display_human_gestures()
            print('------------------------------------------------------------------')
            print('------------------------------------------------------------------')
            self.gesture_comparison_humans()
            print('------------------------------------------------------------------')
            print('------------------------------------------------------------------')
            self.show_score()
            if player1.gesture == player2.gesture:
                continue
            if player1.score == 2:
                print('------------------------------------------------------------------')
                print('Player 1 Wins!!')
                print('------------------------------------------------------------------')
                print('------------------------------------------------------------------')
                break
            elif player2.score == 2:
                print('------------------------------------------------------------------')
                print('Player 1 Wins!!')
                print('------------------------------------------------------------------')
                print('------------------------------------------------------------------')
                break
            print('------------------------------------------------------------------')
            print('                          Round 3                                 ')
            print(player1.gesture_list)
            print('------------------------------------------------------------------')
            print(player1.choose_gesture_humans())
            print(player2.gesture_list)
            print('------------------------------------------------------------------')
            print(player2.choose_gesture_humans2())
            self.display_human_gestures()
            print('------------------------------------------------------------------')
            print('------------------------------------------------------------------')
            self.gesture_comparison_vs_humans()
            print('------------------------------------------------------------------')
            print('------------------------------------------------------------------')
            self.show_score()
            if player1.gesture == player2.gesture:
                continue
        if player1.score == 2:
            print('------------------------------------------------------------------')
            print('PLAYER 1 WINS!!')
            print('------------------------------------------------------------------')
            print('------------------------------------------------------------------')
        elif player2.score == 2:
            print('------------------------------------------------------------------')
            print('PLAYER 2 WINS!!')
            print('------------------------------------------------------------------')
            print('------------------------------------------------------------------')

    def gesture_comparison_humans(self):
        if player1.gesture == player2.gesture:
            print('------------------------------------------------------------------')
            print(f"We both chose the same thing so it's a tie!")
            print('------------------------------------------------------------------')
            print('------------------------------------------------------------------')
        elif player1.gesture == "Rock":
            if player2.gesture == "Scissors" or player2.gesture == 'Lizard':
                print('------------------------------------------------------------------')
                print('Player 1 wins!')
                print('------------------------------------------------------------------')
                print('------------------------------------------------------------------')
                player1.score += 1
            elif player2.gesture == 'Paper' or player2.gesture == 'Spock':
                print('------------------------------------------------------------------')
                print("*Player 2 Wins!")
                print('------------------------------------------------------------------')
                print('------------------------------------------------------------------')
                player2.score += 1
        elif player1.gesture == "Paper":
            if player2.gesture == "Rock" or player2.gesture == 'Spock':
                print('------------------------------------------------------------------')
                print('Player 1 Wins!')
                print('------------------------------------------------------------------')
                print('------------------------------------------------------------------')
                player1.score += 1
            elif player2.gesture == 'Scissors' or player2.gesture == 'Lizard':
                print('------------------------------------------------------------------')
                print("Player 2 Wins!")
                print('------------------------------------------------------------------')
                print('------------------------------------------------------------------')
                player2.score += 1
        elif player1.gesture == "Scissors":
            if player2.gesture == "Paper" or player2.gesture == 'Lizard':
                print('------------------------------------------------------------------')
                print('Player 1 Wins!')
                print('------------------------------------------------------------------')
                print('------------------------------------------------------------------')
                player1.score += 1
            elif player2.gesture == 'Rock' or player2.gesture == 'Spock':
                print('------------------------------------------------------------------')
                print("Player 2 Wins!")
                print('------------------------------------------------------------------')
                print('------------------------------------------------------------------')
                player2.score += 1
        elif player1.gesture == 'Lizard':
            if player2.gesture == 'Spock' or player2.gesture == 'Paper':
                print('------------------------------------------------------------------')
                print('Player 1 Wins!')
                print('------------------------------------------------------------------')
                print('------------------------------------------------------------------')
                player1.score += 1
            elif player2.gesture == 'Scissors' or player2.gesture == 'Rock':
                print('------------------------------------------------------------------')
                print('Player 2 Wins!')
                print('------------------------------------------------------------------')
                print('------------------------------------------------------------------')
                player2.score += 1
        elif player1.gesture == 'Spock':
            if player2.gesture == 'Scissors' or player2.gesture == 'Rock':
                print('------------------------------------------------------------------')
                print('Player 1 wins!')
                print('------------------------------------------------------------------')
                print('------------------------------------------------------------------')
                player1.score += 1
            elif player2.gesture == 'Lizard' or player2.gesture == 'Paper':
                print('------------------------------------------------------------------')
                print('Player 2!')
                print('------------------------------------------------------------------')
                print('------------------------------------------------------------------')
                player2.score += 1

    def show_score(self):
        print(f'The score is {player1.score} to {playerAI.score}!')
