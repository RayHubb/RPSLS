import random
from player import Player


class Computer(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        cpu_gesture = random.randint(1, 5)
        self.gesture = self.gesture_list.get(cpu_gesture)
        print('---------------------------------------------------------------')
        print(f'Your opponent chose {self.gesture}!')
        print('---------------------------------------------------------------')

