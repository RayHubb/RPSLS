class Player:
    def __init__(self):
        self.name = ''
        self.gesture_list = {1: 'Rock', 2: 'Paper', 3: 'Scissors', 4: 'Lizard', 5: 'Spock'}
        self.gesture = ''
        self.score = 0

    def create_gesture_list(self):
        print('---------------------------------------------------------------')
        print(self.gesture_list)
        print('---------------------------------------------------------------')

    def choose_gesture(self):
        user_gesture = int(input('Choose a number with the Gesture you want to use!: '))
        self.gesture = self.gesture_list.get(user_gesture)
        print('---------------------------------------------------------------')
        print('You chose ' + self.gesture + '!')
