from player import Player


class Human(Player):
    def __init__(self):
        super().__init__()

    def enter_name(self):
        print('---------------------------------------------------------------')
        self.name = input('What would you like to be called? :')
        print('---------------------------------------------------------------')
        print('---------------------------------------------------------------')
        print(f'Ok {self.name}!')



