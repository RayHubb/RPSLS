class Player:
    def __init__(self):
        self.name = ''
        self.gesture_list = {1: 'Rock', 2: 'Paper', 3: 'Scissors', 4: 'Lizard', 5: 'Spock'}
        self.gesture = ''
        self.gesture2 = ''
        self.score = 0


# Name method?
    #def enter_name(self):
      #  print('---------------------------------------------------------------')
      #  self.name = input('What would player1 like to be called? :')
      #  print('---------------------------------------------------------------')
      #  print('---------------------------------------------------------------')
      #  print(f'Ok {self.name}!')

    def create_gesture_list(self):
        print('---------------------------------------------------------------')
        print(self.gesture_list)
        print('------------------------------------------------------------------')

    def choose_gesture(self):
        user_gesture = int(input('Choose a number with the Gesture you want to use!: '))
        while user_gesture > 5 or user_gesture <= 0:
            user_gesture = int(input('Choose a number with the Gesture you want to use!: '))
        self.gesture = self.gesture_list.get(user_gesture)
        print('------------------------------------------------------------------')
        print(f'You have chosen {self.gesture}!')
        print('------------------------------------------------------------------')

    def choose_gesture_humans(self):
        user_gesture = int(input('Hey Player 1! Choose a number with the Gesture you want to use!: '))
        while user_gesture > 5 or user_gesture <= 0:
            user_gesture = int(input('Hey Player 1! Choose a number with the Gesture you want to use!: '))
            self.gesture = self.gesture_list.get(user_gesture)

    def choose_gesture_humans2(self):
        user_gesture2 = int(input('Hey Player 2! Choose a number with the Gesture you want to use!: '))
        while user_gesture2 > 5 or user_gesture2 < 0:
            user_gesture2 = int(input('Hey Player 2! Choose a number with the Gesture you want to use!: '))
            self.gesture2 = self.gesture_list.get(user_gesture2)




